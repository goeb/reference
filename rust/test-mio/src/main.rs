use std::error::Error;
use std::io::Write;

use mio::net::{TcpListener, TcpStream};
use mio::{Events, Interest, Poll, Token};
use std::io::prelude::*;
// Some tokens to allow us to identify which event is for which socket.
const SERVER: Token = Token(0);
const CLIENT: Token = Token(1);

fn main() -> Result<(), Box<dyn Error>> {
    // Create a poll instance.
    let mut poll = Poll::new()?;
    // Create storage for events.
    let mut events = Events::with_capacity(128);

    // Setup the server socket.
    let addr = "127.0.0.1:4455".parse()?;
    let mut server: TcpListener = TcpListener::bind(addr)?;
    println!("Start listening on {addr}");
    // Start listening for incoming connections.
    poll.registry()
        .register(&mut server, SERVER, Interest::READABLE)?;

    // Setup the client socket.
    println!("Connecting to port {addr}");
    let mut client: TcpStream = TcpStream::connect(addr)?;
    // Register the socket.
    poll.registry()
        .register(&mut client, CLIENT, Interest::READABLE | Interest::WRITABLE)?;

    // Start an event loop.
    loop {
        // Poll Mio for events, blocking until we get an event.
        match poll.poll(&mut events, None) {
            Ok(_) => {}
            // Polling can be interrupted (e.g. by a debugger) - retry if so.
            Err(e) if e.kind() == std::io::ErrorKind::Interrupted => continue,
            Err(e) => {
                panic!("poll failed: {e:?}")
            }
        }

        // Process each event.
        for event in events.iter() {
            // We can use the token we previously provided to `register` to
            // determine for which socket the event is.
            match event.token() {
                SERVER => {
                    // If this is an event for the server, it means a connection
                    // is ready to be accepted.
                    //
                    // Accept the connection and drop it immediately. This will
                    // close the socket and notify the client of the EOF.
                    println!("SERVER: accept");
                    let mut connection: std::io::Result<(TcpStream, std::net::SocketAddr)> = server.accept();
                    match connection {
                        Ok((mut conn, addr)) => {
                            conn.write(b"hello");
                        },
                        Err(err) => println!("Err: {err}")
                    }
                }
                CLIENT => {
                    println!("CLIENT...");
                    if event.is_writable() {
                        // We can (likely) write to the socket without blocking.
                        println!("CLIENT: is_writable");
                    }

                    if event.is_readable() {
                        // We can (likely) read from the socket without blocking.
                        println!("CLIENT: is_readable");
                        let mut buffer: [u8; 128] = [0; 128];
                        let result: std::io::Result<usize> = client.read(&mut buffer);
                        match result {
                            Ok(n) => {
                                println!("CLIENT: {:?}", &buffer[..n]);
                            },
                            Err(err) => { println!("read: err={err}"); }
                        };
                    }
                    println!("CLIENT: end event...");

                    // Since the server just shuts down the connection, let's
                    // just exit from our event loop.
                    //return Ok(());
                }
                // We don't expect any events with tokens other than those we provided.
                _ => unreachable!(),
            }
        }
    }
}

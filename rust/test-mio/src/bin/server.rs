// Build:
//     cargo build --bin server
//
// Terminal-1:
//     ./target/debug/server
//     Start listening on 127.0.0.1:4455
//
// Terminal-2:
//     echo the quick brown fox jumps over the lazy dog | socat - TCP:127.0.0.1:4455
//     got 10 bytes
//     got 10 bytes
//     got 10 bytes
//     got 10 bytes
//     got 4 bytes
//
// Terminal-1:
//     SERVER: accept
//     SERVER: register accepted socket (from client 127.0.0.1:59816)
//     1: got event
//     1: is_writable
//     1: is_readable
//     1: the quick
//     1: wrote 13 bytes
//     1: brown fox
//     1: wrote 13 bytes
//     1: jumps over
//     1: wrote 13 bytes
//     1:  the lazy
//     1: wrote 13 bytes
//     1: dog\x0A
//     1: wrote 12 bytes
//     1: peer closed
//     1: end event
//
use std::collections::HashMap;
use std::error::Error;
use std::io::Write;

use mio::net::{TcpListener, TcpStream};
use mio::{Events, Interest, Poll, Token};
use std::io::prelude::*;
// Some tokens to allow us to identify which event is for which socket.
const SERVER: Token = Token(0);

fn bytes_to_string(bytes: &[u8]) -> String {
    let mut string = String::new();
    for &byte in bytes {
        if byte >= 0x20 && byte < 0x7F {
            string.push(std::char::from_u32(byte as u32).unwrap());
        } else {
            string += format!("\\x{byte:02X}").as_str();
        }
    }
    string
}

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

    // Register the socket.
    //poll.registry()
    //    .register(&mut client, CLIENT, Interest::READABLE | Interest::WRITABLE)?;

    // Start an event loop.
    let mut next_client_id: usize = 1;
    let mut clients: HashMap<usize, TcpStream> = HashMap::new();
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
                    println!("SERVER: accept");
                    let conn: std::io::Result<(TcpStream, std::net::SocketAddr)> = server.accept();
                    match conn {
                        Ok((mut conn, addr)) => {
                            println!("SERVER: register accepted socket (from client {addr:?})");
                            poll.registry().register(
                                &mut conn,
                                Token(next_client_id),
                                Interest::READABLE | Interest::WRITABLE,
                            )?;
                            clients.insert(next_client_id, conn);
                            next_client_id += 1;
                        }
                        Err(err) => println!("Err: {err}"),
                    }
                }
                Token(client_id) => {
                    let mut client: &TcpStream = match clients.get(&client_id) {
                        Some(client) => {
                            println!("{client_id}: got event");
                            client
                        }
                        None => {
                            println!("{client_id}: error: not registered");
                            continue;
                        }
                    };

                    if event.is_error() {
                        println!("{client_id}: is_error");
                    }

                    if event.is_writable() {
                        // We can (likely) write to the socket without blocking.
                        println!("{client_id}: is_writable");
                    }

                    if event.is_readable() {
                        // We can (likely) read from the socket without blocking.
                        println!("{client_id}: is_readable");
                        loop {
                            let mut buffer: [u8; 10] = [0; 10];
                            let result: std::io::Result<usize> = client.read(&mut buffer);
                            match result {
                                Ok(0) => {
                                    println!("{client_id}: peer closed");
                                    break;
                                }
                                Ok(n) => {
                                    println!("{client_id}: {}", bytes_to_string(&buffer[..n]));
                                    let response: String = format!("got {n} bytes\n");
                                    let result: std::io::Result<usize> =
                                        client.write(response.as_bytes());
                                    match result {
                                        Ok(n) => println!("{client_id}: wrote {n} bytes"),
                                        Err(err) => println!("{client_id}: write error: {err}"),
                                    }
                                }
                                Err(err) if err.kind() == std::io::ErrorKind::WouldBlock => {
                                    println!("{client_id}: WouldBlock");
                                    break;
                                }
                                Err(err) => {
                                    println!("{client_id}: err={err}");
                                    break;
                                }
                            };
                        }
                    }
                    println!("{client_id}: end event");
                }
            }
        }
    }
}

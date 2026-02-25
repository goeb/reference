// target/debug/test-process
// stdout: "line: test\n"
// stderr: ""

use std::io::Write;
use std::process::{Command, Stdio};
use std::{thread, time};

fn main() {
    let mut command: std::process::Command = Command::new("sed");
    let cmd: &mut std::process::Command = command
        .args(["-e", "s/^/line: /"])
        .stdin(Stdio::piped())
        .stdout(Stdio::piped())
        .stderr(Stdio::piped());

    // Spawn a process of the given command
    let result_spawn: std::io::Result<std::process::Child> = cmd.spawn();
    let mut child: std::process::Child = match result_spawn {
        Ok(child) => child,
        Err(err) => {
            eprintln!("Cannot start process: {err}");
            return;
        }
    };

    thread::sleep(time::Duration::from_millis(1000));

    let mut stdin: std::process::ChildStdin = child.stdin.take().expect("failed to get stdin");
    let result_write = stdin.write_all(b"test\n");
    match result_write {
        Ok(_) => (),
        Err(err) => {
            // Example: EPIPE 32 Broken pipe, if the child exited
            println!("stdin.write_all: {err}");
        }
    }

    drop(stdin); // close our side of the stdin of the child process to make it end

    let result_output: std::io::Result<std::process::Output> = child.wait_with_output();
    let output: std::process::Output = match result_output {
        Ok(output) => output,
        Err(err) => {
            eprintln!("Cannot wait for child process: {err}");
            return;
        }
    };

    println!("stdout: {:?}", String::from_utf8(output.stdout).unwrap());
    println!("stderr: {:?}", String::from_utf8(output.stderr).unwrap());
}

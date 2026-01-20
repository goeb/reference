macro_rules! print_all {
    ($e:expr) => {
        println!("{} = {}", stringify!{$e}, $e);
    };
    ($e:expr, $($es:expr),+) => {{
        print_all! { $e }
        print_all! { $($es),+ }
    }};

}

fn main() {
    let args: Vec<String> = std::env::args().collect();

    for arg in args.iter() {
        println!("arg={arg}, {arg:p}");
    }

    let file_path = &args[2];
    println!("In file {file_path}");

    let x_value = std::env::var("X").unwrap_or(String::from(""));
    println!("x_value={x_value}");

    print_all!("a", "b", 1 + 2);

    let result = std::fs::read_to_string(file_path);
    match result {
        Ok(contents) => println!("With text:\n{contents}"),
        Err(error) => {
            eprintln!("Error reading from '{file_path}': {error}");
            std::process::exit(1);
        }
    }
}

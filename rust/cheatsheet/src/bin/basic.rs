// cargo run
//
fn main() {
    basic_types();
    test_match();
    test_vector();
}

fn basic_types() {
    println!("Hello, world!");
    let x: i32 = -123;
    println!("x={}", x);
    let y: f32 = 1.23E6;
    println!("y={}", y);

    let string_ref: &str = "John Doe";
    println!("string_ref={}", string_ref);
    let string_1: String = "Ken".to_string();
    println!("string_1={}", string_1);
    let mut string_2: String = String::from("Thomas");
    println!("string_2={}", string_2);
    string_2.push_str("111");
    println!("string_2={}", string_2);
    let slice_str: &str = &string_2[0..3];
    println!("slice_str={}", slice_str);

    let letter = 'a';
    println!("letter={}", letter);

    let boolean: bool = true;
    println!("boolean={}", boolean);
    let array_of_int: [i32; 5] = [1, 2, 3, 4, 5];
    println!("array_of_int={:?}", array_of_int);
    let array_of_string: [&str; 3] = ["Alice", "Bob", "Charles"];
    println!("array_of_string={:?}", array_of_string);
    println!("array_of_string[0]={}", array_of_string[0]);

    let tuple: (&str, u8) = ("Alice", 33);
    println!("tuple={:?}", tuple);
    let tuple_nested: (u32, (&str, u8)) = (1, ("Bob", 41));
    println!("tuple_nested={:?}", tuple_nested);

    let slice: &[i32; 4] = &[-1, 0, 1, 2];
    println!("slice={:?}", slice);
    let slice_names: &[String; 3] = &[
        "Alice".to_string(),
        "Bob".to_string(),
        "Charles".to_string(),
    ];
    println!("slice_names={:?}", slice_names);
}

fn test_match() {
    let dice_roll = 9;
    match dice_roll {
        3 => println!("test_match: 3"),
        other => println!("test_match: {}", other),
        _ => (), // warning: unreachable pattern
    }

    let config_max = Some(String::from("z123"));
    if let Some(max) = config_max {
        println!("test_match: max={max}");
    }
    let Some(x) = Some(3) else {
        println!("test_match: else");
        return;
    };
    println!("test_match: x={x}");
}

fn test_vector() {
    let mut v = vec![1, 2, 3, 4, 5];
    println!("v={v:?}");

    let third: &i32 = &v[2];
    println!("third={third}");

    let third: Option<&i32> = v.get(2);
    println!("third={:?}", v.get(2));
    match third {
        Some(third) => println!("third={third}"),
        None => println!("There is no third element."),
    }

    let mut j = 0;
    for i in &v {
        println!("v[{j}]={i}");
        j += 1;
    }
    for i in &mut v {
        *i = 2 * (*i);
    }
    println!("v={v:?}");
}

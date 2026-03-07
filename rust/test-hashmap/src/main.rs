use std::collections::HashMap;

#[derive(Debug)]
struct Container {
    name: String,
    value: u32,
}

impl Clone for Container {
    fn clone(&self) -> Container {
        Container {
            name: self.name.clone(),
            value: self.value,
        }
    }
}

impl Container {
    fn increment(&mut self) {
        self.value += 1;
    }
}

fn main() {
    let mut hashmap: HashMap<u32, Container> = HashMap::new();
    hashmap.insert(
        0,
        Container {
            name: String::from("alice"),
            value: 444,
        },
    );
    let item: &Container = hashmap.get(&0).unwrap();
    let mut item2: Container = item.clone();
    item2.increment();
    println!("item={item:?}");
    // Replace the item in the hashmap
    hashmap.remove(&0);
    hashmap.insert(0, item2);
    println!("item={:?}", hashmap[&0]);

    hashmap.insert(
        1,
        Container {
            name: String::from("bob"),
            value: 123,
        },
    );
    println!("item={:?}", hashmap[&1]);

    let bob: &mut Container = hashmap.get_mut(&1).unwrap();
    bob.increment();
    println!("item={:?}", hashmap[&1]);
}

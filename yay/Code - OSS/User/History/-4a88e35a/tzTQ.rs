struct Person {
    name: String,
    age: u8,
}

impl Person {
    pub fn new() -> Self {
        Self {
            name: "No Name".to_string(),
            age: 0,
        }
    }

    pub fn from(name: String, age: u8) -> Self {
        Self {
            name, age
        }
    }
}

fn main() {
    let string = String::from("Artur");
    println!("Hello, world!");
}

#[allow(unused_imports)]
use std::collections::HashMap;
use std::fs;

#[allow(dead_code)]
struct File {
    name: String,
    size: usize,
}

impl File {
    pub fn new(name: String, size: usize) -> Self {
        Self { name, size }
    }
}
#[allow(dead_code)]
struct Directory {
    name: String,
    parent: Option<Box<Directory>>,
    file_list: Vec<File>,
    size: usize,
    children: Vec<Directory>,
}
#[allow(dead_code)]
impl Directory {
    pub fn new(parent: Option<Box<Directory>>, name: String) -> Self {
        Self {
            name,
            parent,
            file_list: Vec::new(),
            size: 0,
            children: Vec::new(),
        }
    }
}
#[allow(dead_code)]
enum Command {
    Cd { argument: String },
    Ls,
}
#[allow(dead_code)]
enum CommandOrFileOrDir {
    Command(Command),
    File(File),
    Node(Directory),
}

fn read_input(path: String) -> Vec<String> {
    let contents = fs::read_to_string(path).expect("should have been able to read the file");
    let contents: Vec<String> = contents.lines().map(|s| s.to_owned()).collect();
    contents
}
#[allow(dead_code)]
fn parse_line(
    line: String,
    wd: Option<Box<Directory>>,
) -> Result<CommandOrFileOrDir, &'static str> {
    if line.as_bytes()[0] as char == '$' {
        if line.as_bytes()[2] as char == 'l' {
            Ok(CommandOrFileOrDir::Command(Command::Ls))
        } else {
            Ok(CommandOrFileOrDir::Command(Command::Cd {
                argument: line[5..].to_string(),
            }))
        }
    } else if line.as_bytes()[0] as char == 'd' {
        Ok(CommandOrFileOrDir::Node(Directory::new(
            wd,
            line[4..].to_string(),
        )))
    } else {
        let size: usize = (line.split(' ').next()).unwrap().parse().unwrap();
        let name = line.split(' ').nth(1);
        Ok(CommandOrFileOrDir::File(File::new(
            name.unwrap().to_string(),
            size,
        )))
    }
}

fn main() {
    let contents = read_input("input".to_owned());
    for line in contents {
        println!("{}", line.as_bytes()[0] as char);
        println!("{}", line);
    }
}

# GenZ Language Compiler 

A fun custom programming language built using GenZ + Indian slang to understand how compilers/interpreters work.

This project demonstrates the core concepts of:
- Lexical Analysis (Tokenization)
- Parsing (AST creation)
- Interpretation (Execution)

---

#  Language Syntax

##  Variable Declaration

Declare variables using:


yeh x hai 10


Meaning:
- `yeh` → declare variable  
- `x` → variable name  
- `hai` → assignment keyword  
- `10` → value  

---

##  Printing Output


bol(x)


Prints the value of `x`.

You can also print strings:


bol("hello world")


---

##  Boolean Values

| GenZ Term | Meaning |
|----------|--------|
| noCap    | true   |
| cap      | false  |

Example:


yeh flag hai noCap
bol(flag)


---

##  Example Program


yeh x hai 10
bol(x)


Output:


10


---

##  Error Handling

If the syntax is invalid, the compiler throws:


Bro what are you even typing 💀


---

#  How It Works

## 1. Tokenization
Breaks code into tokens:


yeh x hai 10


→


['yeh', 'x', 'hai', '10']


---

## 2. Parsing
Converts tokens into structured representation (AST):


Assign(x, 10)


---

## 3. Interpretation
Executes the program:
- Stores variables
- Evaluates values
- Prints output

---

# 🗂️ Project Structure


genz-compiler/
│
├── main.py # Entry point
├── tokenizer.py # Tokenization logic
├── parser.py # Parsing logic (AST)
├── interpreter.py # Execution engine
├── example.genz # Sample program
└── README.md # Documentation


---

#  How to Run

1. Clone the repository:


git clone https://github.com/yourusername/genz-compiler.git

cd genz-compiler


2. Run the program:


python main.py


---

#  Why I Built This

I built this project to:
- Understand how programming languages work internally
- Learn the pipeline of compilers/interpreters
- Make learning fun using GenZ-style syntax

---

#  Future Scope

- Add conditional statements (`agar`, `warna`)
- Add loops (`repeat jabtak`)
- Support expressions (`x + y`)
- Build a full compiler instead of interpreter

---

#  Author

Built by someone who said:

> "Normal languages are boring, let's make coding fun 💀"

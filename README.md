# MyOOPS

**MyOOPS** is an experimental object-oriented programming layer and compiler framework designed to bring a simple, C-like OOP syntax to C development.

The project aims to provide familiar object-oriented concepts such as classes, objects, methods, constructors, encapsulation, inheritance, and polymorphism while using C as the initial compilation target.

> **Status:** Early Development / Experimental

---

## Vision

C is powerful, efficient, and widely used, but it does not provide built-in object-oriented abstractions such as classes, objects, constructors, or inheritance.

MyOOPS explores a different approach:

```text
MyOOPS Source
      ↓
MyOOPS Compiler
      ↓
Generated C
      ↓
GCC / Clang
      ↓
Executable
```

The long-term goal is to develop a lightweight OOP-oriented programming environment that remains closely connected to the C ecosystem.

---

## Example

A MyOOPS program is designed to look like:

```c
#include <myoops.h>

class Hello {

    public:

        void sayHello() {
            print("Hello World");
        }
};

int main() {

    object h : Hello;

    h.sayHello();

    return 0;
}
```

Expected output:

```text
Hello World
```

> The syntax shown above is part of the proposed MyOOPS language design and is currently under development.

---

## Project Architecture

```text
                    MyOOPS
                       │
             ┌─────────┴─────────┐
             │                   │
         Compiler              Runtime
             │                   │
      ┌──────┼──────┐       myoops.h
      │      │      │       myoops.c
    Lexer  Parser  AST
             │
       Semantic Analysis
             │
       Code Generation
             │
          C Source
             │
        GCC / Clang
             │
         Executable
```

---

## Project Structure

```text
MyOOPS/
│
├── compiler/
│   ├── __init__.py
│   ├── lexer.py
│   ├── parser.py
│   ├── ast.py
│   ├── semantic.py
│
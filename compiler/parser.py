from .ast import (
    Program,
    ClassDeclaration,
    MethodDeclaration,
    ObjectDeclaration,
)


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    # -------------------------
    # Utility functions
    # -------------------------

    def current(self):
        if self.position >= len(self.tokens):
            return None

        return self.tokens[self.position]

    def advance(self):
        token = self.current()
        self.position += 1
        return token

    def check(self, value):
        token = self.current()

        if token is None:
            return False

        return token[1] == value

    def expect(self, value):
        token = self.current()

        if token is None:
            raise SyntaxError(
                f"Expected {value}, but reached end of input"
            )

        if token[1] != value:
            raise SyntaxError(
                f"Expected {value}, got {token}"
            )

        self.position += 1

        return token

    def expect_identifier(self):
        token = self.current()

        if token is None:
            raise SyntaxError("Expected identifier")

        if token[0] != "IDENTIFIER":
            raise SyntaxError(
                f"Expected identifier, got {token}"
            )

        self.position += 1

        return token[1]

    # -------------------------
    # Main parser
    # -------------------------

    def parse(self):

        declarations = []

        while self.current() is not None:

            if self.check("class"):
                declarations.append(
                    self.parse_class()
                )

            elif self.check("object"):
                declarations.append(
                    self.parse_object()
                )

            else:
                self.advance()

        return Program(declarations)

    # -------------------------
    # Class
    # -------------------------

    def parse_class(self):

        self.expect("class")

        class_name = self.expect_identifier()

        self.expect("{")

        members = []

        while not self.check("}"):

            if self.check("public"):
                self.advance()
                self.expect(":")

            elif self.check("private"):
                self.advance()
                self.expect(":")

            elif self.check("protected"):
                self.advance()
                self.expect(":")

            elif self.check("void"):
                members.append(
                    self.parse_method("void")
                )

            else:
                raise SyntaxError(
                    f"Unexpected token in class: "
                    f"{self.current()}"
                )

        self.expect("}")

        self.expect(";")

        return ClassDeclaration(
            class_name,
            members
        )

    # -------------------------
    # Method
    # -------------------------

    def parse_method(self, return_type):

        self.expect(return_type)

        method_name = self.expect_identifier()

        self.expect("(")
        self.expect(")")

        self.expect("{")

        body = []

        while not self.check("}"):

            token = self.advance()

            body.append(token)

        self.expect("}")

        return MethodDeclaration(
            return_type,
            method_name,
            [],
            body
        )

    # -------------------------
    # Object
    # -------------------------

    def parse_object(self):

        self.expect("object")

        object_name = self.expect_identifier()

        self.expect(":")

        class_name = self.expect_identifier()

        self.expect(";")

        return ObjectDeclaration(
            class_name,
            object_name
        )
if __name__ == "__main__":

    from lexer import tokenize

    source = """
    class Hello {

        public:

            void sayHello() {
                print("Hello World");
            }
    };

    object h : Hello;
    """

    tokens = tokenize(source)

    parser = Parser(tokens)

    program = parser.parse()

    print(program)
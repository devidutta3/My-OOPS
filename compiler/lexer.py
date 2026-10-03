import re


KEYWORDS = {
    "class",
    "object",
    "public",
    "private",
    "protected",
    "void",
    "int",
    "return",
    "constructor",
    "destructor",
    "extends",
    "virtual",
    "override",
}


TOKEN_PATTERN = re.compile(
    r"""
    (?P<STRING>"(?:\\.|[^"\\])*")
    |(?P<NUMBER>\d+)
    |(?P<IDENTIFIER>[A-Za-z_][A-Za-z0-9_]*)
    |(?P<OPERATOR>==|!=|<=|>=|\+=|-=|\*=|/=|[+\-*/=<>])
    |(?P<SYMBOL>[{}();:,.])
    |(?P<WHITESPACE>\s+)
    |(?P<COMMENT>//[^\n]*)
    """,
    re.VERBOSE,
)


def tokenize(source):
    tokens = []

    position = 0

    while position < len(source):

        match = TOKEN_PATTERN.match(source, position)

        if not match:
            raise SyntaxError(
                f"Unexpected character at position {position}: "
                f"{source[position]!r}"
            )

        kind = match.lastgroup
        value = match.group()

        position = match.end()

        if kind in {"WHITESPACE", "COMMENT"}:
            continue

        if kind == "IDENTIFIER" and value in KEYWORDS:
            kind = "KEYWORD"

        tokens.append((kind, value))

    return tokens

if __name__ == "__main__":

    source = """
    class Hello {
        public:
            void sayHello() {
                print("Hello World");
            }
    };
    """

    tokens = tokenize(source)

    for token in tokens:
        print(token)
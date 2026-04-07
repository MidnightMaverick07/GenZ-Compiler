class Assign:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Print:
    def __init__(self, value):
        self.value = value


def parse(tokens):
    ast = []
    i = 0

    while i < len(tokens):
        # yeh x hai 10
        if tokens[i] == "yeh":
            name = tokens[i + 1]
            value = tokens[i + 3]
            ast.append(Assign(name, value))
            i += 4

        # bol(x)
        elif tokens[i] == "bol":
            value = tokens[i + 2]
            ast.append(Print(value))
            i += 4

        else:
            i += 1  # skip unknown tokens safely

    return ast
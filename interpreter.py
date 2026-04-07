variables = {}

def evaluate(value):
    if value.isdigit():
        return int(value)
    elif value in variables:
        return variables[value]
    elif value == "noCap":
        return True
    elif value == "cap":
        return False
    elif value.startswith('"') and value.endswith('"'):
        return value.strip('"')
    else:
        raise Exception(f"Variable '{value}' not defined 💀")


def execute(ast):
    for node in ast:

        # Assignment
        if node.__class__.__name__ == "Assign":
            variables[node.name] = evaluate(node.value)

        # Print
        elif node.__class__.__name__ == "Print":
            print(evaluate(node.value))
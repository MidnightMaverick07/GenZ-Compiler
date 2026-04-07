import re

def tokenize(code):
    # remove comments
    code = re.sub(r'#.*', '', code)

    tokens = re.findall(
        r'yeh|hai|bol|noCap|cap|[a-zA-Z_]\w*|\d+|".*?"|[()><=+]',
        code.replace(" ", "")
    )
    return tokens
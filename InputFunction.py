import re

# Define regular expressions for tokenization
token_patterns = [
    (r'\bPRINT\b', 'PRINT'),       # Match PRINT keyword
    (r'\bINPUT\b', 'INPUT'),       # Match INPUT keyword
    (r'\b[a-zA-Z]+\b', 'IDENTIFIER'),  # Match identifiers
    (r'\d+', 'NUMBER'),            # Match numbers
    (r'\+', 'ADD_OP'),             # Match addition operator
    (r'-', 'SUB_OP'),              # Match subtraction operator
    (r'\*', 'MUL_OP'),             # Match multiplication operator
    (r'/', 'DIV_OP'),              # Match division operator
    (r'\^', 'EXP_OP'),             # Match exponentiation operator
    (r'\(', 'LPAREN'),             # Match left parenthesis
    (r'\)', 'RPAREN'),             # Match right parenthesis
    (r'=', 'ASSIGN'),              # Match assignment operator
]

def tokenize(expression):
    tokens = []
    while expression:
        match = None
        for pattern, token_type in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(expression)
            if match:
                value = match.group(0)
                tokens.append((token_type, value))
                expression = expression[len(value):].lstrip()
                break
        if not match:
            raise ValueError('Invalid expression: {}'.format(expression))
    return tokens

# Example usage
expression = input("Enter an arithmetic expression: ")
try:
    tokens = tokenize(expression)
    print("Tokens:", tokens)
except ValueError as e:
    print("Error:", e)

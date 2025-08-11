# Prompt user for expression.
expression = input("Expression: ")

# split expression into 3 variables.
x, y, z = expression.split(" ")

# Convert x , z into floats.
x = float(x)
z = float(z)

# use cases
match y:
    case '+':
        print(x + z)
    case '-':
        print(x - z)
    case '*':
        print(x * z)
    case '/':
        print(x / z)
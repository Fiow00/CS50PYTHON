# Demonstrates a NameError

try:
    x = int(input("What's ? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
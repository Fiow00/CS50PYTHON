import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ")
        if name not in names:
            names.append(name)
        else:
            pass
    except EOFError:
        print(f"Adieu, adieu, to {p.join(names)}")
        break

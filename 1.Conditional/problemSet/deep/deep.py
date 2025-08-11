# prompt an answer from the user
answer = input("What is the answer to the Great Quistion of Life, the Universe, and Everything? ").strip().lower()

match answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Use case and conditions
    if s[0:2].isalpha() and 2 <= len(s) < 7 and s.isalnum():
        for c in s:
            if c.isdigit():
                start = s.index(c)
                if s[start:].isdigit() and int(c) != 0:
                    return True
                else:
                    return False

        return True

if __name__ == "__main__":
    main()

import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip);

    if matches:
        numbers = matches.group().split(".");
        for number in numbers:
            number = int(number);
            if number > 255:
                return False;
        return True;
    else:
        return False;

if __name__ == "__main__":
    main()
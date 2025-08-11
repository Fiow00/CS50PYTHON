import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r"(https?:\/\/)?(www\.)?(youtube\.com\/)?(embed\/)?([a-zA-Z0-9]{11})", s);

    if matches:
        groups = matches.groups();
        return "https://youtu.be/" + groups[-1];

if __name__ == "__main__":
    main()

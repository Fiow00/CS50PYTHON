import re;

def main():
    print(convert(input("Hours: ")));

def convert(s):
    matches = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$", s, re.IGNORECASE);
    if matches:
        print("Valid");
    else:
        print("Invalid");
if __name__ == "__main__":
    main();


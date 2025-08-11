from plates import is_valid
def main():
    test_valid()
    test_invalid()

def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("HELLO") == True
    assert is_valid("AA") == True

def test_invalid():
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("H") == False
    assert is_valid("PI3.14") == False
    assert is_valid("OUTATIME") == False
    assert is_valid("22") == False
    assert is_valid("2A") == False

if __name__ == "__main__":
    main()

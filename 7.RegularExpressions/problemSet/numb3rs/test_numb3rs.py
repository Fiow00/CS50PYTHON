from numb3rs import validate;

def main():
    test_validation();
    test_invalidation();

def test_validation():
    assert validate("1.2.3.4") == True;
    assert validate("255.255.255.255") == True;

def test_invalidation():
    assert validate("512.512.512.512") == False;
    assert validate("1.2.3.1000") == False;
if __name__ == "__main__":
    main();
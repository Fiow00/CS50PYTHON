from bank import value

def main():
    test_hello()
    test_h()
    test_others()

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0

def test_h():
    assert value("How is it going") == 20
    assert value("how is it going") == 20

def test_others():
    assert value("What's up") == 100
    assert value("what's up") == 100

if __name__ == "__main__":
    main()

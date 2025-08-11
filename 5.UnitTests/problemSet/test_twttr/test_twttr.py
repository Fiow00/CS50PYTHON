# import required modules
from twttr import shorten

# main
def main():
    test_upper_lower_cases()
    test_numbers()
    test_punctuation()

def test_upper_lower_cases():
    assert shorten('twitter') == 'twttr'
    assert shorten('Twitter') == 'Twttr'
    assert shorten('TwItTeR') == 'TwtTR'

def test_numbers():
    assert shorten('1234') == '1234'

def test_punctuation():
    assert shorten('?!.,') == '?!.,'

if __name__ == "__main__":
    main()

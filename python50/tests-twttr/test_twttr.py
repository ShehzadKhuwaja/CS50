from twttr import shorten

def main():
    test_shorten()

def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("HellO WorLD") == "Hll WrLD"
    assert shorten(",") == ","
    assert shorten("50") == "50"


if __name__ == "__main__":
    main()
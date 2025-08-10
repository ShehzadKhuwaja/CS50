from bank import value

def test_hello():
    assert value("Hello, World") == 0

def test_h():
    assert value("h") == 20
    assert value("hi, cs50") == 20
    assert value("HI, CS50") == 20

def test_something_else():
    assert value("no") == 100
    assert value("GOODBYE") == 100
    assert value("LOVE 50 ") == 100

if __name__ == "__main__":
    main()

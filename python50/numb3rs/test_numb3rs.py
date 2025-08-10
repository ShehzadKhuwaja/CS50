from numb3rs import validate

def test_range():
    assert validate("275.6.4.3") == False
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("135.275.131.222") == False
    assert validate("123.123.256.4") == False
    assert validate("34.34.53.257") == False
    assert validate("192.168.0.1") == True

def test_alpha():
    assert validate("hello.50.cs.168") == False

if __name__ == "__main__":
    main()
from plates import is_valid

def test_first_two_letters():
    assert is_valid("AAC504") == True
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False 

def test_middle_numbers():
    assert is_valid("AAA5QC") == False
    assert is_valid("aaacd5") == True

def test_punctuation():
    assert is_valid("THE,50") == False
    assert is_valid("CS-X-50") == False

def test_spaces():
    assert is_valid("HI 50") == False
    assert is_valid("HI50  ") == False

def test_periods():
    assert is_valid("BYE50.") == False

def test_length():
    assert is_valid("helloworld") == False
    assert is_valid("i") == False
    assert is_valid("ABCDEF") == True
    assert is_valid("ABC") == True

def test_all_character():
    assert is_valid("ABCDEF") == True
    assert is_valid("2023") == False

def test_first_number():
    assert is_valid("ABC050") == False
    assert is_valid("AB1000") == True


if __name__ == "__main__":
    main()
from working import convert
import pytest

def main():
    test_boundry_time()
    test_format_1()
    test_format_2()
    test_time_range()

def test_time_range():
    assert convert("3:45 AM to 4:10 PM") == "03:45 to 16:10"
    pytest.raises(ValueError, convert, "45:20 AM to 3:45 PM")
    pytest.raises(ValueError, convert, "45 AM to 45 PM")
    pytest.raises(ValueError, convert, "3:96 AM to 4:34 PM")
    

def test_format_1():
    assert convert("6:30 AM to 11:30 PM") == "06:30 to 23:30"
    pytest.raises(ValueError, convert, "3:45 AM TO 6:45 PM")
    

def test_format_2():
    assert convert("6 AM to 11 PM") == "06:00 to 23:00"
    pytest.raises(ValueError, convert, "3 AM TO 6 PM")
    

def test_boundry_time():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"

if __name__ == "__main__":
    main()
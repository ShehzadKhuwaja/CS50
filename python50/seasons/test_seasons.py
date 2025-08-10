import pytest
from seasons import convert
from datetime import date

def main():
    test_convert()

def test_convert():
    assert convert("2023-04-04") == "One hundred seventy-four thousand, two hundred forty minutes"
    pytest.raises(ValueError, convert, "2023-04-04-04")
    

if __name__ == "__main__":
    main()
from fuel import convert, gauge
import pytest


def test_covert():
    pytest.raises(ZeroDivisionError, convert, fraction="1/0")
    pytest.raises(ValueError, convert, fraction="cs50/1")
    pytest.raises(ValueError, convert, fraction="50/1")
    
    assert convert("2/4") == 50
    assert convert("3/4") == 75
    assert convert("1/3") == 33

def test_guage():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(50) == "50%"
    

if __name__ == "__main__":
    main()
from jar import Jar
import pytest


def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()
    test_size()
    test_capacity() 

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(30)
    assert jar.capacity == 30


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    pytest.raises(ValueError, jar.deposit, 13)
    jar = Jar()
    jar.deposit(12)
    assert jar.n == 12


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    pytest.raises(ValueError, jar.withdraw, 13)
    jar.withdraw(6)
    assert jar.n == 6


def test_size():
    jar = Jar(30)
    jar.deposit(29)
    assert jar.size == 29

def test_capacity():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(30)
    assert jar.capacity == 30


if __name__ == "__main__":
    main()
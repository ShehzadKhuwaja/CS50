from um import count

def main():
    test_no_um()
    test_manu_um()
    test_um_case_insensitive()
    test_um_boundry()

def test_no_um():
    assert count("hell world this is umcs50") == 0
    assert count("hello, world") == 0

def test_many_um():
    assert count("hello, um, um, um, world, 50") == 3

def test_um_case_insensitive():
    assert count("Um, hello, UM, um") == 3

def test_um_boundry():
    assert count("..Um.., hello world this is is cs um? 50") == 2

if __name__ == "__main__":
    main()
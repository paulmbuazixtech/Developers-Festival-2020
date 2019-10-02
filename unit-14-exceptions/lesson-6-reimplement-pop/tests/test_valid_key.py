def test_valid_key():
    test_dict = {
        "cat": "hat",
        "dog": "log",
        "elf": "shelf"
    }

    expected = {
        "cat": "hat",
        "elf": "shelf"
    }

    assert pop(test_dict, "dog") == "log"
    assert len(test_dict) == 2
    assert test_dict == expected
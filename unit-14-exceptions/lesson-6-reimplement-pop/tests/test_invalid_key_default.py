def test_invalid_key_default():
    test_dict = {
        "cat": "hat",
        "dog": "log",
        "elf": "shelf"
    }

    assert pop(test_dict, "horse", "crickets") == "crickets"
    assert len(test_dict) == 3
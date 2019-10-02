import pytest


def test_invalid_key_no_default():
    test_dict = {
        "cat": "hat",
        "dog": "log",
        "elf": "shelf"
    }

    with pytest.raises(KeyError):
        pop(test_dict, "horse")
def test_only_one_char_in_even_positions():
    #         0123456789
    phrase = 'abXXcdeXfX'
    assert count_in_position(phrase, 'X', 'even') == 1

from src.do_maths import do_advanced_stuff


def test_do_advanced_stuff_1():
    assert abs(do_advanced_stuff(1, 2, 3, 4, 5) - 9.0) <= 1e-14

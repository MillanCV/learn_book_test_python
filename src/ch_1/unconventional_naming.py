"""
This test will never be discoverable by pytest because of file name
"""


def test_in_unconventional_folder():
    assert 1 == 1


def unconventional_name():
    assert 1 == 1

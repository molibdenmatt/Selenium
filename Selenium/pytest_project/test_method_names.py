"""
py.test will run only the files with name starting/ending with 'test'
py.test will run only the methods starting with 'test'
"""


def test_method():
    x = 1
    y = 1
    assert x + y == 2, "Assertion failed, Expected value: 2"


def random_name():
    x = 5
    y = 2
    assert x + y == 2, "Assertion failed, Expected value: 2"


def test_random_name_test():
    x = 5
    y = 2
    assert x + y == 2, "Assertion failed, Expected value: 2"

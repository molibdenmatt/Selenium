import pytest

"""
pip3 install pytest-xdist - Multiple parallel tests runner
py.test -n3 - Will run 3 test at the same time
"""


@pytest.mark.parametrize("ingredient, result", [(5, 10), (2, 4), (2, 8)])
def test_addition(ingredient, result):
    assert ingredient + ingredient == result, "Result is wrong!"


@pytest.mark.skip  # Tell pytest to skip this test
def test_addition2(ingredient, result):
    assert ingredient + ingredient == result * 2, "Result is wrong!"


@pytest.mark.xfail  # Expect test method to fail
def test_addition2(ingredient, result):
    assert ingredient + ingredient == result * 2, "Result is wrong!"

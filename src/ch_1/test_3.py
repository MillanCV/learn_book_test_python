"""
Useful decorators
"""
import pytest


@pytest.mark.skip()
def test_skip():
    assert 1 == 1

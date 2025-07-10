import pytest


@pytest.mark.xfail(reason="Известная ошибка, исправление в следующем релизе")
def test_with_bug():
    assert 1 == 2


@pytest.mark.xfail(reason="Баг уже исправлен, но еще в маркировке xfail")
def test_without_bug():
    ...
# -*- coding: utf-8 -*-
import pytest
from Fixtures.FlatFixture import FlatFixture


@pytest.fixture
def fix(request):
    browser = request.config.getoption("--browser")
    target = r"https://testpartner.vtbins.ru/b2c/flat/test-main.html"
    fixture = FlatFixture(browser, target)
    return fixture


def test_flat(fix):
    fix.fill_frame()
    assert fix.is_frame_filled()
    input()





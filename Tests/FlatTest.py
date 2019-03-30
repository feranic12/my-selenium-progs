# -*- coding: utf-8 -*-
import pytest
from Fixtures.FlatFixture import FlatFixture


@pytest.fixture
def fix(request):
    browser = request.config.getoption("--browser")
    target = {"1": r"https://testpartner.vtbins.ru/b2c/flat/test-main.html",
             "2": r"https://testpartner.vtbins.ru/b2c/flat/test-main.html?p=rad",
             "3": r"https://testpartner.vtbins.ru/b2c/flat/test-main.html?client=123",
             "4": r"https://testpartner.vtbins.ru/b2c/flat/test-main.html?p=rad&client=123",
             "5": r"https://vtbins.ru/b2c/flat/test-main.html",
             "6": r"https://2.vtbins.ru/b2c/flat/test-main.html"}[request.config.getoption("--target")]
    fixture = FlatFixture(browser, target)
    return fixture


def test_flat(fix):
    fix.open_page()
    fix.fill_frame()
    assert fix.is_frame_filled()
    input()





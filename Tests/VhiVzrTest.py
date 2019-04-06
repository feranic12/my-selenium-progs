# -*- coding: utf-8 -*-
import pytest
from Fixtures.VhiVzrFixture import VhiVzrFixture


@pytest.fixture
def fix(request):
    browser = request.config.getoption("--browser")
    fixture = VhiVzrFixture(browser)
    return fixture


def test_vhivzr(fix):
    fix.open_page()
    fix.fill_frame()
    input()
# -*- coding: utf-8 -*-
import pytest
from Fixtures.Mite3Fixture import Mite3Fixture


@pytest.fixture
def fix(request):
    browser = request.config.getoption("--browser")
    mitetype = request.config.getoption("--mitetype")
    fixture = Mite3Fixture(browser, mitetype)
    return fixture


def test1_mite3(fix):
    fix.open_page()
    fix.fill_frame()
    input()

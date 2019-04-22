# -*- coding: utf-8 -*-
import pytest
from Fixtures.Mite3Fixture1 import Mite3Fixture1


@pytest.fixture
def fix(request):
    browser = request.config.getoption("--browser")
    fixture = Mite3Fixture1(browser)
    return fixture


def test1_mite3(fix):
    fix.open_page()
    fix.fill_frame()
    input()

# -*- coding: utf-8 -*-
import pytest
from Fixtures.VoyageFixture import VoyageFixture


@pytest.fixture
def fix(request):
    cmd_days = request.config.getoption("--days")
    browser = request.config.getoption("--browser")
    fixture = VoyageFixture(browser, cmd_days)
    return fixture


def test_voyage(fix):
    fix.open_page()
    fix.fill_frame()
    input()
# -*- coding: utf-8 -*-
import pytest
from Fixtures.VhiVoyageFixture import VhiVoyageFixture


@pytest.fixture
def fix(request):
    browser = request.config.getoption("--browser")
    fixture = VhiVoyageFixture(browser)
    return fixture


def test_vhivoyage(fix):
    fix.open_page()
    fix.fill_frame()
    input()
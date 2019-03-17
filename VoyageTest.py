# -*- coding: utf-8 -*-
import pytest
from Fixtures.VoyageFixture import VoyageFixture


@pytest.fixture
def fix(request):
    cmdopt = request.config.getoption("--days")
    fixture = VoyageFixture(cmdopt)
    return fixture


def test_voyage(fix):
    fix.fill_frame()
    input()
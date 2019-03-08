# -*- coding: utf-8 -*-
import pytest
from Fixtures.VoyageFixture import VoyageFixture

@pytest.fixture
def fix():
    fixture = VoyageFixture()
    return fixture

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--days")


def test_voyage(fix, cmdopt):
    fix.fill_frame(cmdopt)
    input()
# -*- coding: utf-8 -*-
import pytest
from Fixtures.VoyageFixture import VoyageFixture


@pytest.fixture
def fix(request):
    cmd_days = request.config.getoption("--days")
    fixture = VoyageFixture(cmd_days)
    return fixture


def test_voyage(fix):
    fix.fill_frame()
    input()
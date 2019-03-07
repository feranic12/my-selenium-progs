# -*- coding: utf-8 -*-
import pytest
from Fixtures.VoyageFixture import VoyageFixture


def pytest_addoption(parser):
    parser.addoption("--cmdopt",action="store",default=6,type=int)


@pytest.fixture
def fix():
    fixture = VoyageFixture()
    return fixture


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")


def test_voyage(fix, cmdopt):
    fix.fill_frame(cmdopt)
    input()
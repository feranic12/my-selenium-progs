import pytest
from Fixtures.TravelFixture import TravelFixture


@pytest.fixture
def fix():
    fixture = TravelFixture()
    return fixture


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--days")


def test_travel(fix,cmdopt):
    fix.fill_frame(cmdopt)
    input()
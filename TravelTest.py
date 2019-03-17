import pytest
from Fixtures.TravelFixture import TravelFixture


@pytest.fixture
def fix(request):
    cmdopt = request.config.getoption("--days")
    fixture = TravelFixture(cmdopt)
    return fixture


def test_travel(fix):
    fix.fill_frame()
    input()
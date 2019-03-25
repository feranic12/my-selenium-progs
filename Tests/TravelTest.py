import pytest
from Fixtures.TravelFixture import TravelFixture


@pytest.fixture
def fix(request):
    cmd_days = request.config.getoption("--days")
    fixture = TravelFixture(cmd_days)
    return fixture


def test_travel(fix):
    fix.fill_frame()
    input()
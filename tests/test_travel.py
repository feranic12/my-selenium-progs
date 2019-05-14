import pytest
from Fixtures.TravelFixture import TravelFixture


@pytest.fixture
def fix(request):
    cmd_days = request.config.getoption("--days")
    browser = request.config.getoption("--browser")
    fixture = TravelFixture(browser, cmd_days)
    return fixture


def test_travel(fix):
    fix.open_page()
    fix.fill_frame()
    input()
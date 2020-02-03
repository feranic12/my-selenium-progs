import pytest
from Fixtures.HomeFixture import HomeFixture


@pytest.fixture
def fix(request):
    browser = request.config.getoption("--browser")
    fixture = HomeFixture(browser)
    return fixture


def test_home(fix):
    fix.open_page()
    fix.fill_frame()
    input()
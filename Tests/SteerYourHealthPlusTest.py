import pytest
from Fixtures.SteerYourHealthPlusFixture import SteerYourHealthPlusFixture


@pytest.fixture
def fix(request):
    browser = request.config.getoption("--browser")
    fixture = SteerYourHealthPlusFixture(browser)
    return fixture


def test_steeryourhealthplus(fix):
    fix.open_page()
    fix.fill_frame()
    input()

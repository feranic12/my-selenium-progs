import pytest
from Fixtures.MedOnlineFixture import MedOnlineFixture


@pytest.fixture
def fix(request):
    browser = request.config.getoption("--browser")
    fixture = MedOnlineFixture(browser)
    return fixture


def test_medonline(fix):
    fix.open_page()
    fix.fill_frame()
    input()
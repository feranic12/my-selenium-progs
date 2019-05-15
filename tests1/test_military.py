import pytest
from Fixtures.MilitaryFixture import MilitaryFixture


@pytest.fixture
def fix(request):
    browser = request.config.getoption("--browser")
    fixture = MilitaryFixture(browser)
    request.addfinalizer(fixture.destroy)
    return fixture


def test_military(fix):
    fix.open_page()
    fix.fill_frame()
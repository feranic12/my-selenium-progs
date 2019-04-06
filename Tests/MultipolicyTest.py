import pytest
from Fixtures.MultipolicyFixture import MultipolicyFixture


@pytest.fixture
def fix(request):
    browser = request.config.getoption("--browser")
    fixture = MultipolicyFixture(browser)
    return fixture


def test_multipolicy(fix):
    fix.open_page()
    fix.fill_frame()
    input()
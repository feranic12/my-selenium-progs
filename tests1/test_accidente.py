import pytest
from Fixtures.AccidenteFixture import AccidenteFixture


@pytest.fixture
def fix(request):
    browser = request.config.getoption("--browser")
    fixture = AccidenteFixture(browser)
    request.addfinalizer(fixture.destroy)
    return fixture


def test_accidente(fix):
    fix.open_page()
    fix.fill_frame()
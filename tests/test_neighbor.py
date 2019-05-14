import pytest
from Fixtures.NeighborFixture import NeighborFixture


@pytest.fixture
def fix(request):
    browser = request.config.getoption("--browser")
    fixture = NeighborFixture(browser)
    return fixture


def test_neighbor(fix):
    fix.open_page()
    fix.fill_frame()
    input()
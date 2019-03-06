import pytest
from MilitaryFixture import MilitaryFixture


@pytest.fixture
def fix():
    fixture = MilitaryFixture()
    return fixture


def test_military(fix):
    fix.fill_frame()
    input()
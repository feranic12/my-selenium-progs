import pytest
from TravelFixture import TravelFixture


@pytest.fixture
def fix():
    fixture = TravelFixture()
    return fixture


def test_travel(fix):
    fix.fill_frame()
    input()
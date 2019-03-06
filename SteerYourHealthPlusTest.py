import pytest
from SteerYourHealthPlusFixture import SteerYourHealthPlusFixture


@pytest.fixture
def fix():
    fixture = SteerYourHealthPlusFixture()
    return fixture


def test_steeryourhealthplus(fix):
    fix.fill_frame()
    input()

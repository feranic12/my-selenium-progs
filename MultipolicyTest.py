import pytest
from Fixtures.MultipolicyFixture import MultipolicyFixture


@pytest.fixture
def fix():
    fixture = MultipolicyFixture()
    return fixture


def test_multipolicy(fix):
    fix.fill_frame()
    input()
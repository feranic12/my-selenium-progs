# -*- coding: utf-8 -*-
import pytest
from Fixtures.FlatFixture import FlatFixture


@pytest.fixture
def fix():
    fixture = FlatFixture()
    return fixture


def test_flat(fix):
    fix.fill_frame()
    assert fix.is_frame_filled()
    input()





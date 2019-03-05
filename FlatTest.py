# -*- coding: utf-8 -*-
import pytest
from FlatFixture import FlatFixture


@pytest.fixture
def fix():
    fixture=FlatFixture()
    return fixture


def test_flat(fix):
    fix.fill_frame()





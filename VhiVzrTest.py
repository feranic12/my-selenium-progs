# -*- coding: utf-8 -*-
import pytest
from Fixtures.VhiVzrFixture import VhiVzrFixture


@pytest.fixture
def fix():
    fixture = VhiVzrFixture()
    return fixture


def test_vhivzr(fix):
    fix.fill_frame()
    input()
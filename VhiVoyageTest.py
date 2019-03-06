# -*- coding: utf-8 -*-
import pytest
from VhiVoyageFixture import VhiVoyageFixture


@pytest.fixture
def fix():
    fixture = VhiVoyageFixture()
    return fixture


def test_vhivoyage(fix):
    fix.fill_frame()
    input()
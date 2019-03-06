# -*- coding: utf-8 -*-
import pytest
from VoyageFixture import VoyageFixture


@pytest.fixture
def fix():
    fixture = VoyageFixture()
    return fixture


def test_voyage(fix):
    fix.fill_frame()
    input()

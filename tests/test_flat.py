# -*- coding: utf-8 -*-
import pytest
from Fixtures.FlatFixture import FlatFixture
from Fixtures.AccidenteFixture import AccidenteFixture
from Fixtures.MedOnlineFixture import MedOnlineFixture
from Fixtures.MilitaryFixture import MilitaryFixture
from Fixtures.Mite3Fixture import Mite3Fixture
from Fixtures.MultipolicyFixture import MultipolicyFixture
from Fixtures.NeighborFixture import NeighborFixture
from Fixtures.SteerYourHealthPlusChildFixture import SteerYourHealthPlusChildFixture
from Fixtures.SteerYourHealthPlusAdultFixture import SteerYourHealthPlusAdultFixture
from Fixtures.TravelFixture import TravelFixture
from Fixtures.VhiVoyageFixture import VhiVoyageFixture
from Fixtures.VhiVzrFixture import VhiVzrFixture
from Fixtures.VoyageFixture import VoyageFixture


@pytest.fixture
def fix(request):
    browser = request.config.getoption("--browser")
    product = request.config.getoption("--product")
    days = request.config.getoption("--days")
    if product == "Flat":
        target = {"1": r"https://testpartner.vtbins.ru/b2c/flat/test-main.html",
                 "2": r"https://testpartner.vtbins.ru/b2c/flat/test-main.html?p=rad",
                 "3": r"https://testpartner.vtbins.ru/b2c/flat/test-main.html?client=123",
                 "4": r"https://testpartner.vtbins.ru/b2c/flat/test-main.html?p=rad&client=123",
                 "5": r"https://vtbins.ru/b2c/flat/test-main.html",
                 "6": r"https://2.vtbins.ru/b2c/flat/test-main.html"}[request.config.getoption("--target")]
        fixture = FlatFixture(browser, target)
    if product == "Accidente":
        fixture = AccidenteFixture(browser)
    elif product == "MedOnline":
        fixture = MedOnlineFixture(browser)
    elif product == "Military":
        fixture = MilitaryFixture(browser)
    elif product == "Mite3":
        fixture = Mite3Fixture(browser)
    elif product == "Multipolicy":
        fixture = MultipolicyFixture(browser)
    elif product == "NeighborFixture":
        fixture = NeighborFixture(browser)
    elif product == "SteerYourHealthPlusChild":
        target = {"1": r"https://testpartner.vtbins.ru/b2c/steerYourHealthPlus/test-main.html",
                  "2": r"https://testpartner.vtbins.ru/b2c/steerYourHealthPlus/test-main.html?p=led"}[
            request.config.getoption("--target")]
        fixture = SteerYourHealthPlusChildFixture(browser, target)
    elif product == "SteerYourHealthPlusAdult":
        target = {"1": r"https://testpartner.vtbins.ru/b2c/steerYourHealthPlus/test-main.html",
                  "2": r"https://testpartner.vtbins.ru/b2c/steerYourHealthPlus/test-main.html?p=led"}[
            request.config.getoption("--target")]
        fixture = SteerYourHealthPlusAdultFixture(browser, target)
    elif product == "Travel":
        fixture = TravelFixture(browser, days)



    return fixture


def test_flat(fix):
    fix.open_page()
    fix.fill_frame()
    assert fix.is_frame_filled()
    input()





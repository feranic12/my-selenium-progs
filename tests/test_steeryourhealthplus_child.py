import pytest
from Fixtures.SteerYourHealthPlusChildFixture import SteerYourHealthPlusChildFixture



@pytest.fixture
def fix(request):
    browser = request.config.getoption("--browser")
    target =  {"1":r"https://testpartner.vtbins.ru/b2c/steerYourHealthPlus/test-main.html",
               "2":r"https://testpartner.vtbins.ru/b2c/steerYourHealthPlus/test-main.html?p=led"}[request.config.getoption("--target")]
    fixture = SteerYourHealthPlusChildFixture(browser, target)
    return fixture


def test_steeryourhealthplus(fix):
    fix.open_page()
    fix.fill_frame()
    input()

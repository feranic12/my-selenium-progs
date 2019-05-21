def pytest_addoption(parser):
    parser.addoption("--target", action="store", default=1)
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--days", action="store", default=6)
    parser.addoption("--mitetype", action="store", default=1)
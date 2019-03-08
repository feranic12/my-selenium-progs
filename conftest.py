def pytest_addoption(parser):
    parser.addoption("--days",action="store",default=6,type=int)
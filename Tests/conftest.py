def pytest_addoption(parser):
    parser.addoption("--days",action="store",default=6,type=int)
    parser.addoption("--browser",action="store",default="chrome",type=str)
    parser.addoption("--target",action="store",default="1",type=str)
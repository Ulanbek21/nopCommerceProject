import sys
sys.path.append('.')
from selenium import webdriver
import pytest

# @pytest.fixture() # We used in TC so that will give the driver verible
# def setup():
#     driver = webdriver.Chrome()
#     return driver

#---------------------for crosse browser test-------------------------------------------
@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver=webdriver.Firefox()
        print("Launching firefox browser.........")
    return driver

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

# #pytest -s -v testCases/test_login.py --browser chrome ///// Will execute from command pro just specify browser name
# #pytest -s -v testCases/test_login.py --browser firefox


# #--------------------------------------------Report genaretion---------------------------------------------

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Ulan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)



# pytest -s -v -n=3 --html=Reports/report.html testCases/test_login.py --browser chrome



#------------------------Will creat random email or number---------------------------------------

# ef random_generator(size=8, chars=string.ascii_lowercase + string.digits):
#     return ''.join(random.choice(chars) for x in range(size))

#------------------------------------------------------------------------------------------------

# pytest -s -v --html=Reports/report.html testCases/ --browser chrome
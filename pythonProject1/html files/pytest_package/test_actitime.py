# import time
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# driver.get("https://demo.actitime.com/login.do")
#
# class ActiTime:
#     def enter_name(self, u_name):
#         driver.find_element("class name", "textField").send_keys(u_name)
#
#     def enter_pwd(self, pwd):
#         driver.find_element("class name", "textField.pwdfield").send_keys(pwd)
#
#     def click_login_btn(self):
#         driver.find_element("id", "loginButton").click()
#         wait_ = WebDriverWait(driver, 20)
#         assert wait_.until(expected_conditions.title_contains("actiTIME - Enter Time-Track"))
#         exp_title = 'actiTIME - Enter Time-Track'
#         act_title = driver.title
#         assert exp_title == act_title
#
#
# class TestActiTime:
#
#     @pytest.mark.valid_TC
#     def test_valid_uname(self):
#         obj = ActiTime()
#         obj.enter_name("admin")
#         obj.enter_pwd("manager")
#         obj.click_login_btn()
#         time.sleep(2)
#
#     @pytest.mark.invalid_TC
#     def test_invalid_uname(self):
#         obj = ActiTime()
#         obj.enter_name("anu")
#         obj.enter_pwd("manager")
#         obj.click_login_btn()
#
#
#     @pytest.mark.invalid_TC
#     def test_invalid_uname1(self):
#         obj = ActiTime()
#         obj.enter_name("admimm")
#         obj.enter_pwd("manager")
#         obj.click_login_btn()
#
##################################################################################################
# import time
#
# import pytest
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# @pytest.fixture()
# def init_driver():
#
#     path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
#     driver = webdriver.Chrome(executable_path=path)
#     driver.get("https://demo.actitime.com/login.do")
#
# class ActiTime:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def enter_name(self, u_name):
#         self.driver.find_element("class name", "textField").send_keys(u_name)
#
#     def enter_pwd(self, pwd):
#         self.driver.find_element("class name", "textField.pwdfield").send_keys(pwd)
#
#     def click_login_btn(self):
#         self.driver.find_element("id", "loginButton").click()
#         wait_ = WebDriverWait(self.driver, 20)
#         assert wait_.until(expected_conditions.title_contains("actiTIME - Enter Time-Track"))
#         exp_title = 'actiTIME - Enter Time-Track'
#         act_title = self.driver.title
#         assert exp_title == act_title
# data = [("admin", "manager"),
#      ("adminn", "manager"),
#      ("admin", "manage"),
#      ("adm", "man")
# ]
#
# class TestActiTime:
#
#     @pytest.mark.parametrize("u_name, pwd", data)
#     def test_registration(self, u_name, pwd, init_driver):
#         driver = init_driver
#         obj = ActiTime(driver)
#         obj.enter_name(u_name)
#         obj.enter_pwd(pwd)
#         obj.click_login_btn()
#         time.sleep(2)

################################################################

import pytest
import xlrd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class ReadExcel:

    def read_testdata(self):
        f_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\testdata\aa.xlsx"
        wb = xlrd.open_workbook(f_path)
        ws = wb.sheet_by_name("reg_actitime")
        rows = ws.get_rows()  # generator object
        header = next(rows)
        data =[]
        for row in rows:
            element = (row[0].value, row[1].value)
            data.append(element)
        return data

    def read_locators(self):
        f_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\testdata\aa.xlsx"
        wb = xlrd.open_workbook(f_path)
        ws = wb.sheet_by_name("reg_object")
        rows = ws.get_rows()  # generator object
        header = next(rows)
        d = {}
        for row in rows:
            d[row[0].value] = (row[1].value, row[2].value)

        return d


@pytest.fixture(params=["chrome", "firefox", "edge"])
def init_driver(request):
    browser = request.param

    if browser.lower() == "chrome":
        chrome_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=chrome_path)

    elif browser.lower() == "firefox":
        firefox_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\geckodriver.exe"
        driver = webdriver.Firefox(executable_path=firefox_path)

    else:
        edge_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\msedgedriver.exe"
        driver = webdriver.Edge(executable_path=edge_path)



    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(r"https://demo.actitime.com/")
    yield driver
    driver.close()


class ActiTime:

    read_xl = ReadExcel()
    locatr = read_xl.read_locators()

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, f_name):
        assert f_name == "admin", "Invalid Username"
        locator = self.locatr["username"]
        self.driver.find_element(*locator).send_keys(f_name)

    def enter_password(self, pswd):
        assert pswd == "manager", "Invalid Password"
        locator = self.locatr["password"]
        self.driver.find_element(*locator).send_keys(pswd)

    def click_on_checkbox(self):
        locator = self.locatr["checkbox"]
        self.driver.find_element(*locator).click()

    def click_on_login(self):
        locator = self.locatr["login_button"]
        self.driver.find_element(*locator).click()
        wait_ = WebDriverWait(self.driver, 20)
        assert wait_.until(expected_conditions.title_contains("actiTIME - Enter Time-Track"))
        exp_title = 'actiTIME - Enter Time-Track'
        act_title = self.driver.title
        assert exp_title == act_title


# data = [("admin", "manager"), ("admine", "manager"), ("admin", "managere")]


class TestActiTime:

    excel_data = ReadExcel()
    data = excel_data.read_testdata()

    @pytest.mark.parametrize("u_name, pswds", data)
    def test_valid_all_inputs(self, u_name, pswds, init_driver):
        driver = init_driver
        n = ActiTime(init_driver)
        n.enter_username(u_name)
        n.enter_password(pswds)
        n.click_on_login()

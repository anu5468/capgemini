# import re
# import pytest
# from selenium import webdriver
#
# @pytest.fixture()
# def init_driver():
#     path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
#     driver = webdriver.Chrome(executable_path=path)
#     driver.get("https://demowebshop.tricentis.com/")
#     driver.maximize_window()
#     yield driver
#     driver.close()
#
#
#
#
# class RegisterPage:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def click_register_link(self):
#         self.driver.find_element("link text", "Register").click()
#
#     def select_female_radio_btn(self):
#         self.driver.find_element("id", "gender-female").click()
#
#     def select_male_radio_btn(self):
#         self.driver.find_element("id", "gender-male").click()
#
#     def enter_firstname(self, f_name):
#         self.driver.find_element("id", "FirstName").send_keys(f_name)
#
#     def enter_lastname(self, l_name):
#         self.driver.find_element("name", "LastName").send_keys(l_name)
#
#     def enter_email(self, email):
#         pattern = r"\w+@gmail\.com"
#         result = re.findall(pattern, email)
#         assert result, "invalid email"
#         self.driver.find_element("id", "Email").send_keys(email)
#
#     def enter_password(self, pwd):
#         assert len(pwd) >= 6, "password should have atleast 6 characters"
#         self.driver.find_element("name", "Password").send_keys(pwd)
#         return pwd
#
#     def confirm_password(self, c_pwd, actual_pwd):
#         assert actual_pwd == c_pwd, "passwords are different"
#         self.driver.find_element("name", "ConfirmPassword").send_keys(c_pwd)
#
#
# class TestRegisterPage:
#
#     @pytest.mark.valid_testcase
#     def test_valid_email(self, init_driver):
#         driver = init_driver
#         rp = RegisterPage(driver)
#         rp.click_register_link()
#         rp.select_female_radio_btn()
#         rp.enter_firstname("anu")
#         rp.enter_lastname("j")
#         rp.enter_email("anu@gmail.com")
#         actual_pwd = rp.enter_password("123456")
#         rp.confirm_password("123456", actual_pwd)
#
#     @pytest.mark.invalid_testcase
#     def test_invalid_email(self, init_driver):
#         driver = init_driver
#         rp = RegisterPage(driver)
#         rp.click_register_link()
#         rp.select_female_radio_btn()
#         rp.enter_firstname("anu")
#         rp.enter_lastname("j")
#         rp.enter_email("anu@")
#         actual_pwd = rp.enter_password("123456")
#         rp.confirm_password("12345", actual_pwd)
#
#     @pytest.mark.valid_testcase
#     def test_valid_pwd(self, init_driver):
#         driver = init_driver
#         rp = RegisterPage(driver)
#         rp.click_register_link()
#         rp.select_female_radio_btn()
#         rp.enter_firstname("anu")
#         rp.enter_lastname("j")
#         rp.enter_email("anu@gmail.com")
#         actual_pwd = rp.enter_password("123456")
#         rp.confirm_password("123456", actual_pwd)
#
#     @pytest.mark.invalid_testcase
#     def test_invalid_pwd(self, init_driver):
#         driver = init_driver
#         rp = RegisterPage()
#         rp.click_register_link()
#         rp.select_female_radio_btn()
#         rp.enter_firstname("anu")
#         rp.enter_lastname("j")
#         rp.enter_email("anu@")
#         actual_pwd = rp.enter_password("123456")
#         rp.confirm_password("12345", actual_pwd)
#


######################################################################################################
# import re
# import pytest
# from selenium import webdriver
#
# @pytest.fixture(params=["chrome", "firefox", "edge"])
# def init_driver(request):
#     browser = request.param
#
#     if browser.lower() == "chrome":
#         chrome_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
#         driver = webdriver.Chrome(executable_path=chrome_path)
#
#     elif browser.lower() == "firefox":
#         firefox_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\geckodriver.exe"
#         driver = webdriver.Firefox(executable_path=firefox_path)
#
#     else:
#         edge_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\msedgedriver.exe"
#         driver = webdriver.Edge(executable_path=edge_path)
#
#     driver.get("https://demowebshop.tricentis.com/")
#     driver.maximize_window()
#     yield driver
#     driver.close()
#
#
#
#
# class RegisterPage:
#     def __init__(self, driver):
#         self.driver = driver
#
#     def click_register_link(self):
#         self.driver.find_element("link text", "Register").click()
#
#     def select_female_radio_btn(self):
#         self.driver.find_element("id", "gender-female").click()
#
#     def select_male_radio_btn(self):
#         self.driver.find_element("id", "gender-male").click()
#
#     def enter_firstname(self, f_name):
#         self.driver.find_element("id", "FirstName").send_keys(f_name)
#
#     def enter_lastname(self, l_name):
#         self.driver.find_element("name", "LastName").send_keys(l_name)
#
#     def enter_email(self, email):
#         pattern = r"\w+@gmail\.com"
#         result = re.findall(pattern, email)
#         assert result, "invalid email"
#         self.driver.find_element("id", "Email").send_keys(email)
#
#     def enter_password(self, pwd):
#         assert len(pwd) >= 6, "password should have atleast 6 characters"
#         self.driver.find_element("name", "Password").send_keys(pwd)
#         return pwd
#
#     def confirm_password(self, c_pwd, actual_pwd):
#         assert actual_pwd == c_pwd, "passwords are different"
#         self.driver.find_element("name", "ConfirmPassword").send_keys(c_pwd)
#
# data = [
#     ("anu", "j", "anu.jpas04@gmail.com", "123456", "123456"),
#     ("anu", "j", "anu", "123456", "123456"),
#     ("anu", "j", "anu.jpas04@gmail.com", "123456", "123456"),
#     ("anu", "j", "anu.jpas04@gmail.com", "12345", "123456"),
#     ("anu", "j", "anu.jpas04@gmail.com", "123456", "123456"),
#     ("anu", "j", "anu.jpas04@gmail.com", "12345", "123456")
# ]
#
#
# class TestRegisterPage:
#
#     @pytest.mark.parametrize("f_name, l_name, email, pwd, c_pwd", data)
#     def test_registration(self, f_name, l_name, email, pwd, c_pwd, init_driver):
#         driver = init_driver
#         rp = RegisterPage(driver)
#         rp.click_register_link()
#         rp.select_female_radio_btn()
#         rp.enter_firstname(f_name)
#         rp.enter_lastname(l_name)
#         rp.enter_email(email)
#         actual_pwd = rp.enter_password(pwd)
#         rp.confirm_password(c_pwd, actual_pwd)

################################################################################################
import datetime
import re
import xlrd
import pytest
from selenium import webdriver

class ReadExcel:

    def read_testdata(self):
        f_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\testdata\pp.xlsx"
        wb = xlrd.open_workbook(f_path)
        ws = wb.sheet_by_name("reg_credentials")
        rows = ws.get_rows()   #generate object
        header = next(rows)
        data = []
        for row in rows:
            element = (row[0].value, row[1].value, row[2].value, row[3].value, row[4].value)
            data.append(element)
        return data


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

    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    yield driver
    driver.close()




class RegisterPage:
    def __init__(self, driver):
        self.driver = driver

    def click_register_link(self):
        self.driver.find_element("link text", "Register").click()

    def select_female_radio_btn(self):
        self.driver.find_element("id", "gender-female").click()

    def select_male_radio_btn(self):
        self.driver.find_element("id", "gender-male").click()

    def enter_firstname(self, f_name):
        self.driver.find_element("id", "FirstName").send_keys(f_name)

    def enter_lastname(self, l_name):
        self.driver.find_element("name", "LastName").send_keys(l_name)

    def enter_email(self, email):
        pattern = r"\w+@gmail\.com"
        result = re.findall(pattern, email)
        assert result, "invalid email"
        self.driver.find_element("id", "Email").send_keys(email)

    def enter_password(self, pwd):
        assert len(pwd) >= 6, "password should have atleast 6 characters"
        self.driver.find_element("name", "Password").send_keys(pwd)
        return pwd

    def confirm_password(self, c_pwd, actual_pwd):
        assert actual_pwd == c_pwd, "passwords are different"
        self.driver.find_element("name", "ConfirmPassword").send_keys(c_pwd)

class TestRegisterPage:
    read_excel = ReadExcel()
    data = read_excel.read_testdata()

    @pytest.mark.parametrize("f_name, l_name, email, pwd, c_pwd", data)
    def test_registration(self, f_name, l_name, email, pwd, c_pwd, init_driver):

        driver = init_driver
        try:
            rp = RegisterPage(driver)
            rp.click_register_link()
            rp.select_female_radio_btn()
            rp.enter_firstname(f_name)
            rp.enter_lastname(l_name)
            rp.enter_email(email)
            actual_pwd = rp.enter_password(pwd)
            rp.confirm_password(c_pwd, actual_pwd)

        except BaseException as error_msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
            path = r"C:\Users\Anu\PycharmProjects\pythonProject1\screenshot\\"
            driver.save_screenshot(path+name)
            raise error_msg


########################################################################
# import re
# import xlrd
# import pytest
# from selenium import webdriver
#
# class ReadExcel:
#
#     def read_testdata(self):
#         f_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\testdata\pp.xlsx"
#         wb = xlrd.open_workbook(f_path)
#         ws = wb.sheet_by_name("reg_credentials")
#         rows = ws.get_rows()   #generate object
#         header = next(rows)
#         data = []
#         for row in rows:
#             element = (row[0].value, row[1].value, row[2].value, row[3].value, row[4].value)
#             data.append(element)
#         return data
#
#     def read_locators(self):
#         f_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\testdata\uu1.xlsx"
#         wb = xlrd.open_workbook(f_path)
#         ws = wb.sheet_by_name("reg_objects")
#         rows = ws.get_rows()  # generate object
#         header = next(rows)
#         d = {}
#         for row in rows:
#             d[row[0].value] = (row[1].value, row[2].value)
#
#         return d
#
#
# @pytest.fixture(params=["chrome", "firefox", "edge"])
# def init_driver(request):
#     browser = request.param
#
#     if browser.lower() == "chrome":
#         chrome_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
#         driver = webdriver.Chrome(executable_path=chrome_path)
#
#     elif browser.lower() == "firefox":
#         firefox_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\geckodriver.exe"
#         driver = webdriver.Firefox(executable_path=firefox_path)
#
#     else:
#         edge_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\msedgedriver.exe"
#         driver = webdriver.Edge(executable_path=edge_path)
#
#     driver.get("https://demowebshop.tricentis.com/")
#     driver.maximize_window()
#     yield driver
#     driver.close()
#
#
#
#
# class RegisterPage:
#     read_xl = ReadExcel()
#     reg_locators = read_xl.read_locators()
#
#     def __init__(self, driver):
#         self.driver = driver
#
#     def click_register_link(self):
#         locator = self.reg_locators["register_link"]
#         self.driver.find_element(*locator).click()
#
#     def select_female_radio_btn(self):
#         locator_name, locator_value = self.reg_locators["female_radio_btn"]
#         self.driver.find_element(locator_name, locator_value).click()
#
#     def select_male_radio_btn(self):
#         locator = self.reg_locators["male_radio_btn"]
#         self.driver.find_element(*locator).click()
#
#     def enter_firstname(self, f_name):
#         locator = self.reg_locators["firstname_txt"]
#         self.driver.find_element(*locator).send_keys(f_name)
#
#     def enter_lastname(self, l_name):
#         locator = self.reg_locators["lastname_txt"]
#         self.driver.find_element(*locator).send_keys(l_name)
#
#     def enter_email(self, email):
#         pattern = r"\w+@gmail\.com"
#         result = re.findall(pattern, email)
#         assert result, "invalid email"
#
#         locator = self.reg_locators["email_txt"]
#         self.driver.find_element(*locator).send_keys(email)
#
#     def enter_password(self, pwd):
#         if isinstance(pwd, float):
#             pwd = str(int(pwd))
#
#         assert len(pwd) >= 6, "password should have atleast 6 characters"
#         locator = self.reg_locators["password_txt"]
#         self.driver.find_element(*locator).send_keys(pwd)
#         return pwd
#
#     def confirm_password(self, c_pwd, actual_pwd):
#         if isinstance(c_pwd, float):
#             c_pwd = str(int(c_pwd))
#
#         locator = self.reg_locators["confirm_password_txt"]
#         assert actual_pwd == c_pwd, "passwords are different"
#         self.driver.find_element(*locator).send_keys(c_pwd)
#
#
# class TestRegisterPage:
#     read_excel = ReadExcel()
#     data = read_excel.read_testdata()
#
#     @pytest.mark.parametrize("f_name, l_name, email, pwd, c_pwd", data)
#     def test_registration(self, f_name, l_name, email, pwd, c_pwd, init_driver):
#         driver = init_driver
#         rp = RegisterPage(driver)
#         rp.click_register_link()
#         rp.select_female_radio_btn()
#         rp.enter_firstname(f_name)
#         rp.enter_lastname(l_name)
#         rp.enter_email(email)
#         actual_pwd = rp.enter_password(pwd)
#         rp.confirm_password(c_pwd, actual_pwd)
# #

############################################################################################


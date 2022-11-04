import pytest
from POM.login_page import LoginPage
from library.excel_lib import ReadExcel
from library.config import Config


class TestLoginPage:
    read_excel = ReadExcel()
    data = read_excel.read_testdata(Config.LOGIN_TESTDATA_SHEET)

    @pytest.mark.parametrize("email, pwd", data)
    def test_login(self, init_driver, email, pwd):
        driver = init_driver

        lp = LoginPage(driver)
        lp.click_login_link()
        lp.enter_email(email)
        lp.enter_password(pwd)




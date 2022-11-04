import datetime
import pytest
from POM.register_page import RegisterPage
from library.excel_lib import ReadExcel
from library.config import Config

class TestRegisterPage:
    read_excel = ReadExcel()
    data = read_excel.read_testdata(Config.REG_TESTDATA_SHEET)

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
            #path = r"C:\Users\Anu\PycharmProjects\pythonProject1\screenshot\\"
            driver.save_screenshot(Config.SCREENSHOTS_PATH+name)
            raise error_msg

import datetime

import pytest
from POM.health_page import HealthPage
from library.excel_lib import ReadExcel
from library.config import Config


class TestHealthPage:
    read_excel = ReadExcel()
    data = read_excel.read_testdata(Config.HEALTH_TESTDATA_SHEET)

    @pytest.mark.parametrize("mobno, pname, pat_age, cname, pcode, flatno, sname", data)
    def test_health(self, mobno, pname, pat_age, cname, pcode, flatno, sname, init_driver):

        driver = init_driver
        try:
            hp = HealthPage(driver)
            hp.click_labtest()
            hp.click_healthpackage()
            hp.click_diabetescare()
            hp.click_selectpatient()
            hp.click_1patient()
            hp.click_add_details()
            hp.enter_mob_no(mobno)
            hp.click_continue()
            hp.click_CONTINUE_()
            hp.click_add_patient()
            hp.click_add_icon()
            hp.enter_patient_name(pname)
            hp.enter_age(pat_age)
            hp.click_radio()
            hp.click_submit()
            hp.click_add_address()
            hp.enter_contact_name(cname)
            hp.enter_pin_code(pcode)
            hp.enter_flat_no(flatno)
            hp.enter_street_name(sname)
            hp.click_home()
            hp.click_save()
            hp.click_slot_select()
            hp.click_pay_cash()

        except BaseException as error_msg:
            td = datetime.datetime.now()
            name = f"Screenshots_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Config.SCREENSHOTS_PATH+name)
            raise error_msg






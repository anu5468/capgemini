import re
import time

from library.excel_lib import ReadExcel
from library.config import Config


class HealthPage:
    read_xl = ReadExcel()
    health_locators = read_xl.read_locators(Config.HEALTH_LOCATORS_SHEET)

    def __init__(self, driver):
        self.driver = driver

    def click_labtest(self):
        locator = self.health_locators["labtest"]
        self.driver.find_element(*locator).click()

    def click_healthpackage(self):
        locator = self.health_locators["healthpackage"]
        self.driver.find_element(*locator).click()

    def click_diabetescare(self):
        locator = self.health_locators["diabetescare"]
        self.driver.find_element(*locator).click()
        self.driver.refresh()

    def click_selectpatient(self):
        locator = self.health_locators["selectpatient"]
        self.driver.find_element(*locator).click()

    def click_1patient(self):
        locator = self.health_locators["1patient"]
        self.driver.find_element(*locator).click()

    def click_add_details(self):
        locator = self.health_locators["add_details"]
        self.driver.find_element(*locator).click()

    def enter_mob_no(self, mobno):
        if isinstance(mobno, float):
            mobno = int(mobno)
        locator = self.health_locators["mob_no"]
        self.driver.find_element(*locator).send_keys(mobno)

    def click_continue(self):
        locator = self.health_locators["continue"]
        self.driver.find_element(*locator).click()
        time.sleep(20)

    def click_CONTINUE_(self):
        locator = self.health_locators["CONTINUE_"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def click_add_patient(self):
        locator = self.health_locators["add_patient"]
        self.driver.find_element(*locator).click()

    def click_add_icon(self):
        locator = self.health_locators["add_icon"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def enter_patient_name(self, pname):
        locator = self.health_locators["patient_name"]
        self.driver.find_element(*locator).send_keys(pname)
        time.sleep(2)

    def enter_age(self, patage):
        if isinstance(patage, float):
            patage = int(patage)
        locator = self.health_locators["age"]
        self.driver.find_element(*locator).send_keys(patage)

    def click_radio(self):
        locator = self.health_locators["radio"]
        self.driver.find_element(*locator).click()

    def click_submit(self):
        locator = self.health_locators["submit"]
        self.driver.find_element(*locator).click()

    def click_add_address(self):
        locator = self.health_locators["add_address"]
        self.driver.find_element(*locator).click()
        time.sleep(1)

    def enter_contact_name(self, cname):
        locator = self.health_locators["contact_name"]
        self.driver.find_element(*locator).send_keys(cname)
        time.sleep(1)

    def enter_pin_code(self, pcode):
        if isinstance(pcode, float):
            pcode = int(pcode)
        locator = self.health_locators["pin_code"]
        self.driver.find_element(*locator).send_keys(pcode)
        time.sleep(1)

    def enter_flat_no(self, flatno):
        if isinstance(flatno, float):
            flatno = int(flatno)
        locator = self.health_locators["flat_no"]
        self.driver.find_element(*locator).send_keys(flatno)
        time.sleep(1)

    def enter_street_name(self, sname):
        locator = self.health_locators["street_name"]
        self.driver.find_element(*locator).send_keys(sname)

    def click_home(self):
        locator = self.health_locators["home"]
        self.driver.find_element(*locator).click()

    def click_save(self):
        locator = self.health_locators["save"]
        self.driver.find_element(*locator).click()

    def click_slot_select(self):
        locator = self.health_locators["slot_select"]
        self.driver.find_element(*locator).click()

    def click_pay_cash(self):
        locator = self.health_locators["pay_cash"]
        self.driver.find_element(*locator).click()



import time
from behave import *
from selenium import webdriver


@given('user is able to launch browser')
def open_browser(context):
    path = r"C:\Users\Anu\PycharmProjects\HTD_Sprint1\drivers\chromedriver1.exe"
    context.driver = webdriver.Chrome(executable_path=path)
    context.driver.get("https://pharmeasy.in/")
    context.driver.maximize_window()
    context.driver.implicitly_wait(20)


@when('user is able to click on the labtest module')
def click_labtest(context):
    context.driver.find_element("xpath", '//span[text()="Lab Tests"]').click()


@then('user is able to click on the healthpackage module')
def click_healthpackage(context):
    context.driver.find_element("xpath", '//a[.="Health Packages"]').click()


@then('user is able to select one package')
def select_package(context):
    context.driver.find_element("xpath", '//div[.="Diabetes Care"]').click()
    time.sleep(10)


@then('user is able to click on select')
def click_select_patient(context):
    context.driver.find_element("xpath", '//button[.="Select"]').click()


@then('user is able to select one patient')
def click_1patient(context):
    context.driver.find_element("xpath", '(//p[@class="_39TRp"])[1]').click()


@then('user is able to click on add patient details')
def click_add_details(context):
    context.driver.find_element("xpath", '//button[@id="cart-addPatient-Dweb"]').click()


@then('user is able to enter phonenumber "{number}"')
def enter_phonenumber(context, number):
    context.driver.find_element("xpath", '//input[@placeholder="Enter your phone number"]').send_keys(number)


@then('user is able to click on continue')
def click_continue(context):
    context.driver.find_element("xpath", '//button[.="Continue"]').click()
    time.sleep(20)


@then('user is able to click on cont')
def click_cont(context):
    context.driver.find_element("xpath", '//button[.=" CONTINUE"]').click()
    time.sleep(20)


@then('user is able to click on add patient button')
def click_add_patient(context):
    context.driver.find_element("xpath", '//button[@id="cart-addPatient-Dweb"]').click()


@then('user is able to click on plus icon')
def click_plus_icon(context):
    context.driver.find_element("xpath", '(//img[@alt="add icon"])[2]').click()


@then('user is able to enter patient name "{pname}"')
def enter_patient_name(context, pname):
    context.driver.find_element("xpath", '//input[@id="add-Patient-name"]').send_keys(pname)


@then('user is able to enter age "{age}"')
def enter_age(context, age):
    context.driver.find_element("xpath", '//input[@type="number"]').send_keys(age)


@then('user is able to select radio button')
def select_button(context):
    context.driver.find_element("xpath", '//div[@id="add-Patient-gender-0"]').click()


@then('user is able to click on submit')
def click_submit(context):
    context.driver.find_element("xpath", '//button[@type="submit"]').click()


@then('user is able to click on add new address')
def click_add_address(context):
    context.driver.find_element("xpath", '(//div[.="+ Add new address"])[1]').click()


@then('user is able to enter contact name "{cname}"')
def enter_contact_name(context, cname):
    context.driver.find_element("xpath", '//input[@name="contactName"]').send_keys(cname)


@then('user is able to enter pincode "{pcode}"')
def enter_pin_code(context, pcode):
    context.driver.find_element("xpath", '//input[@name="pincode"]').send_keys(pcode)


@then('user is able to enter flatnumber "{flatno}"')
def enter_flat_no(context, flatno):
    context.driver.find_element("xpath", '//input[@name="flatNumber"]').send_keys(flatno)


@then('user is able to enter street name "{sname}"')
def enter_street_name(context, sname):
    context.driver.find_element("xpath", '//input[@name="streetName"]').send_keys(sname)


@then('user is able to select home')
def click_home(context):
    context.driver.find_element("xpath", '//span[.="Home"]').click()


@then('user is able to click on save address')
def click_save(context):
    context.driver.find_element("xpath", '//button[@id="addAddress-saveBtn"]').click()


@then('user is able to click on slot selection continue')
def click_slot_select(context):
    context.driver.find_element("id", 'slot-selection-continueBtn-dWeb').click()


@then('user is able to click on paycash button')
def click_pay_cash(context):
    context.driver.find_element("xpath", '//span[.="Pay Cash"]/../../..//input[@type="radio"]').click()


# @then('user is able to click on place order')
# def place_holder(context):
#     context.driver.find_element("xpath", '//span[.="Place Order"]').click()

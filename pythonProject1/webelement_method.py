import time

from selenium import webdriver
path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()


#element = driver.find_element("id","small-searchterms")
# element = driver.find_element("class name", "search-box-text.ui-autocomplete-input")
# element.click()
# time.sleep(1)
# element.send_keys("books")

# element = driver.find_element("class name", "ico-register")
# element.click()
# element1 = driver.find_element("id", "gender-female")
# element1.click()
# driver.find_element("id", "FirstName").send_keys("Anu")
# driver.find_element("id", "LastName").send_keys("J")
# driver.find_element("id", "Email").send_keys("anu.jpas04@gmail.com")
# driver.find_element("id", "Password").send_keys("anu@5468")
# driver.find_element("id", "ConfirmPassword").send_keys("anu@5468")
#driver.find_element("id", "register-button").click()

####
register_link = driver.find_element("class name", "ico-register")
print(register_link.text)
print(register_link.location)
print(register_link.size)
print(register_link.rect)
print(register_link.get_attribute("href"))

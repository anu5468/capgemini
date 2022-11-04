#############################simple alert####################################
# import time
#
# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# driver.get(r"C:\Users\Anu\PycharmProjects\pythonProject1\html files\demo.html")
# driver.maximize_window()
# driver.find_element("xpath", '//button[@id="submit"]').click()
# time.sleep(2)
# alert_obj = driver.switch_to.alert
# print(alert_obj.text)
# alert_obj.dismiss()


##################################confirmation alert###############################################################
# import time
#
# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# driver.get(r"C:\Users\Anu\PycharmProjects\pythonProject1\html files\demo.html")
# driver.maximize_window()
# driver.find_element("xpath", '//button[@id="delete"]').click()
# time.sleep(2)
# alert_obj = driver.switch_to.alert
# alert_obj.dismiss()


###########################email id demo web shop###############################
# import time

# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# driver.get("https://demowebshop.tricentis.com")
# driver.maximize_window()
# driver.find_element("xpath", '//a[text()="Facebook"]').click()
# driver.implicitly_wait(10)
# handles = driver.window_handles
# print(handles)
# print(driver.current_window_handle)
# print(driver.title)
# driver.switch_to.window(handles[1])
# print(driver.current_window_handle)
# print(driver.title)
#
# driver.find_element("xpath", '//input[@name="email"]').send_keys("anu@gmail.com")
# time.sleep(2)

##############################file upload pop ups###################
# import time
#
# from selenium import webdriver
#
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# driver.get("https://www.monsterindia.com/")
# driver.maximize_window()
# driver.find_element("xpath", '//span[text()="Upload Resume"]').click()
# time.sleep(2)
# path1 = r"C:\Users\Anu\PycharmProjects\pythonProject1\html files\demo.txt"
# driver.find_element("xpath", '(//input[@type="file"])[1]').send_keys(path1)

############################################################################
import time

from selenium import webdriver
path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get(r"C:\Users\Anu\PycharmProjects\pythonProject1\html files\iframe.html")
driver.maximize_window()

#switching to a frame using id attribute
driver.switch_to.frame("FR1")
driver.find_element("xpath", '//input[@id="small-searchterms"]').send_keys("mobiles")
time.sleep(2)

##switching back to parent/main frame
# driver.switch_to.default_content()

###switching to a frame using name attribute
# driver.switch_to.frame("frame2")
# driver.find_element("xpath", '//input[@id="search_form"]').send_keys("abcd")

##########switching to a frame using web-element
# frame_ =driver.find_element("xpath", '//iframe[@name="frame2"]')
# driver.switch_to.frame(frame_)
# driver.find_element("xpath", '//input[@id="search_form"]').send_keys("abcd")
# time.sleep(2)

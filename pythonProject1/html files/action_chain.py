# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# action_obj = ActionChains(driver)
# driver.get("https://www.myntra.com//")
# driver.maximize_window()
# element = driver.find_element("xpath", '//a[@data-group="men"]')
# action_obj.move_to_element(element).perform()

####################################double click#####################################################################
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# action_obj = ActionChains(driver)
# driver.get(r"C:\Users\Anu\PycharmProjects\pythonProject1\html files\demo.html")
# driver.maximize_window()
# ele1 = driver.find_element("xpath", '//button[@id="double-click"]')
# time.sleep(2)
# action_obj.double_click(ele1).perform()

###################################simulating keys###################################################

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# action_obj = ActionChains(driver)
# driver.get(r"C:\Users\Anu\PycharmProjects\pythonProject1\html files\demo.html")
# driver.maximize_window()
# action_obj.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
















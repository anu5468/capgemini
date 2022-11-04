from selenium import webdriver
path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver1.exe"
driver = webdriver.Chrome(executable_path=path)
driver.get("https://demo.actitime.com/login.do")
driver.find_element("class name", "textField").send_keys("admin")
driver.find_element("class name", "textField.pwdfield").send_keys("manager")
driver.find_element("id", "loginButton").click()
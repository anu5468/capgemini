# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# file_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\html files\css_selector.html"
# driver.get(file_path)
# driver.maximize_window()
# #driver.find_element("css selector", 'input[type="text"]').send_keys("Anu")
# #driver.find_element("css selector", 'input[type="password"]').send_keys("anu@5")
# driver.find_element("xpath", '//input[@type="text"]').send_keys("anu")
# driver.find_element("xpath", '//input[@type="password"]').send_keys("1234")

########################################################################
# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
# driver.find_element("css selector", "a[class='ico-register']").click()
# driver.find_element("css selector", "input[value='F']").click()
# driver.find_element("css selector", "input[id='FirstName']").send_keys("Anu")
# driver.find_element("css selector", "input[id='LastName']").send_keys("J")
# driver.find_element("css selector", "input[id='Email']").send_keys("anu.jpas@gmail.com")
# driver.find_element("css selector", "input[id='Password']").send_keys("anu@5468")
# driver.find_element("css selector", "input[id='ConfirmPassword']").send_keys("anu@5468")
# driver.find_element("css selector", "input[id='register-button']").click()

# driver.find_element("xpath", '//a[@class="ico-register"]').click()
# driver.find_element("xpath", '(//input[@name="Gender"])[2]').click()
# driver.find_element("xpath", '//input[@name="FirstName"]').send_keys("anu")

#####################################################################
# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# driver.get("https://demo.actitime.com/login.do")
# driver.find_element("css selector", "input[placeholder='Username']").send_keys("admin")
# driver.find_element("css selector", "input[placeholder='Password']").send_keys("manager")
# driver.find_element("css selector", "a[id='loginButton']").click()


##########################################################################3

# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
# driver.find_element("xpath", "//a[@class='ico-register']").click()
# driver.find_element("css selector", "input[value='F']").click()
# driver.find_element("css selector", "input[id='FirstName']").send_keys("Anu")
# driver.find_element("css selector", "input[id='LastName']").send_keys("J")
# driver.find_element("css selector", "input[id='Email']").send_keys("anu.jpas@gmail.com")
# driver.find_element("css selector", "input[id='Password']").send_keys("anu@5468")
# driver.find_element("css selector", "input[id='ConfirmPassword']").send_keys("anu@5468")
# driver.find_element("css selector", "input[id='register-button']").click()

##########################################################

# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# driver.get("https://demo.actitime.com/login.do")
# driver.find_element("xpath", "//input[@placeholder='Username']").send_keys("admin")
# driver.find_element("xpath", "//input[@placeholder='Password']").send_keys("manager")
# driver.find_element("xpath", "//div[text()='Login ']").click()



#############################################################################

#1) identify dependent and independent elements
#2) write locator expression for independent element
#3) traverse backward until the common parent of both dep and indep elements is obtained
#4) locate the dependent element


#############################################################################
import time

# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\html files\demo.html"
# driver.get(path)
# driver.find_element("xpath", '//td[text()="Perl"]/..//input[@type="checkbox"]').click()
# time.sleep(1)
# driver.find_element("xpath", '//td[text()="Ruby"]/..//input[@type="checkbox"]').click()
# time.sleep(1)
# driver.find_element("xpath", '//td[text()="Java"]/..//input[@type="checkbox"]').click()
# time.sleep(1)
# driver.find_element("xpath", '//td[text()="Python"]/..//input[@type="checkbox"]').click()
# time.sleep(1)
# driver.find_element("xpath", '//td[text()="C#"]/..//input[@type="checkbox"]').click()
# time.sleep(1)
# driver.find_element("xpath", '//td[text()="JavaScript"]/..//input[@type="checkbox"]').click()


########################################################################################


# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# path = r"C:\Users\Shree\PycharmProjects\pythonProject1\html files\demo.html"
# driver.get(path)
# languages = ["Perl", "Ruby", "Java", "Python", "C#", "xpath"]
# for language in languages(6):
#     driver.find_element("xpath", '//td[text()="{languages}"]/..//input[@type="checkbox"]').click()
#     time.sleep(1)


############################################################################################
#1)
# import time
#
# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window()
# driver.find_element("xpath", "(//a[@href='/books'])[3]").click()
# time.sleep(1)
# driver.find_element("xpath", "(//input[@value='Add to cart'])[1]").click()
# time.sleep(1)
# driver.find_element("xpath", "(//input[@value='Add to cart'])[2]").click()
# time.sleep(1)
# driver.find_element("xpath", "(//input[@value='Add to cart'])[3]").click()
# time.sleep(1)


######################################################################################################
#(2)


# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# driver.get("https://demowebshop.tricentis.com")
# driver.maximize_window()
# community_poll = ["pollanswers-1","pollanswers-2","pollanswers-3","pollanswers-4"]
# for poll in community_poll:
#     driver.find_element("xpath", f"//input[@id='{poll}']").click()
#     time.sleep(1)


#######################################################################################
#5)

# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# driver.get("https://smartbear.com/")
# # list_footer_name = ["AlertSite","BitBar","Bugsnag","Capture for Jira","Collaborator","Cucumber for Jira","CucumberStudio","Cucumber Open","LoadNinja","Pact","Pactflow","ReadyAPI","SoapUI","Swagger","SwaggerHub","TestComplete","TestEngine","TestLeft","Zephyr"]
# list_footer_name=driver.find_element("xpath", f'//div[@class="product-column col-12"]//a]')
# time.sleep(2)
# for footer in list_footer_name:
#     print(element.text)

#################################################################################
#3)


# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# driver.get("https://services.smartbear.com/samples/testcomplete14/smartstore/sunglasses")
# driver.maximize_window()
# sun_glass = driver.find_elements("xpath", f"//span[@class='art-price']")
# for price in sun_glass:
#     print(price.text)


###################################################################################
#4)


# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# driver.get(r"C:\Users\Anu\PycharmProjects\pythonProject1\html files\demo.html")
# driver.maximize_window()
# name = ["AAPL", "MSFT", "AA", "FB"]
# for p in name:
#     s = driver.find_element("xpath", f"//td[.='{p}']/..//td[@class='price']")
#     time.sleep(2)
#     print(s.text)
# driver.close()




######################################################################################
#8)
# import time
# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# file_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\html files\demo.html"
# driver.get(file_path)
# languages = ["Ruby","Java","Perl","Python","C#","JavaScript"]
# res = languages[::-1]
# for language in res:
#     driver.find_element("xpath", f'//td[text() = "{language}"]/..//input[@name = "download"]').click()
#     time.sleep(2)


########################################################################################
#(9)
import time

# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# file_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\html files\demo.html"
# driver.get(file_path)
# languages = ["Ruby","Java","Perl","Python","C#","JavaScript"]
# res = languages[::2]
# for language in res:
#     driver.find_element("xpath", f'//td[text() = "{language}"]/..//input[@name = "download"]').click()
#     time.sleep(1)
#



##########################################################################################
#(10)

# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# file_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\html files\demo.html"
# driver.get(file_path)
# languages = ["Ruby","Java","Perl","Python","C#","JavaScript"]
# driver.find_element("xpath", f'//td[text() = "{languages[0]}"]/..//input[@name = "download"]').click()
# time.sleep(2)
# driver.find_element("xpath", f'//td[text() = "{languages[-1]}"]/..//input[@name = "download"]').click()
# time.sleep(2)

################################################################################
# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# driver.get(r"C:\Users\Anu\PycharmProjects\pythonProject1\html files\demo.html")
# driver.find_element("xpath", "(//input[@class='first_row'])[1]").send_keys("hello")
# driver.find_element("xpath", "(//input[@class='first_row'])[2]").send_keys("world")
# driver.find_element("xpath", "(//input[@class='first_row'])[3]").send_keys("welcome")
# driver.find_element("xpath", "(//input[@class='second_row'])[1]").send_keys("to")
# driver.find_element("xpath", "(//input[@class='second_row'])[2]").send_keys("python")
# driver.find_element("xpath", "(//input[@class='second_row'])[3]").send_keys("hi")
# driver.find_element("xpath", "(//input[@class='third_row'])[1]").send_keys("selenium")
# driver.find_element("xpath", "(//input[@class='third_row'])[2]").send_keys("browser")
# driver.find_element("xpath", "(//input[@class='third_row'])[3]").send_keys("automation")
######################################################################################
# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# driver.get(r"C:\Users\Anu\PycharmProjects\pythonProject1\html files\demo.html")
# text_boxes = driver.find_elements("xpath", '//input[@name="fname"]')
# words = ["hi", "hello", "welcome", "to", "python", "selenium", "hi", "python", "bye"]
# for element,text in zip(text_boxes, words):
#     element.send_keys(text)
#     time.sleep(1)
##########################################################################################
# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# driver.get("https://www.python.org/")
# driver.maximize_window()
# element=driver.find_elements("tag name", "a")
# for item in element:
#     print(item.text)
# driver.close()

#############################################################################################
# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# ecutabldriver = webdriver.Chrome(exe_path=path)
# driver.get("https://www.python.org/")
# driver.maximize_window()
# element = driver.find_elements("xpath", '//a[contains(.,"Python")]')
# for item in element:
#     print(item.text)
# driver.close()

#################################################################################################


# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\geckodriver.exe"
# driver = webdriver.Firefox(executable_path=path)
# driver.get("https://www.facebook.com/reg/")
# driver.find_element("xpath", '//input[@name="firstname"]').send_keys("Anu")
# driver.find_element("xpath", '//input[@name="lastname"]').send_keys("Anu")
# driver.find_element("xpath", '//input[@name="reg_email__"]').send_keys("anu.jpas04@gmail.com")
# driver.find_element("xpath", '//input[@name="reg_email_confirmation__"]').send_keys("anu.jpas04@gmail.com")
# driver.find_element("xpath", '//input[@name="reg_passwd__"]').send_keys("anu@1234")
# d_dropdown = driver.find_element("xpath", '//select[@id="day"]')
# time.sleep(1)
# obj = Select(d_dropdown)
# obj.select_by_index(18)
# time.sleep(1)
# m_dropdown = driver.find_element("xpath", '//select[@id="month"]')
# time.sleep(1)
# obj = Select(m_dropdown)
# obj.select_by_index(6)
# time.sleep(1)
# y_dropdown = driver.find_element("xpath", '//select[@id="year"]')
# time.sleep(1)
# obj = Select(y_dropdown)
# obj.select_by_value("1998")
# time.sleep(1)
# driver.find_element("xpath", '(//input[@name="sex"])[1]').click()
# time.sleep(1)
# driver.find_element("xpath", '(//button[@type="submit"])[1]').click()
#

#

########################################################################
# from selenium import webdriver
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# driver.get("https://www.myntra.com//")
# driver.maximize_window()
# driver.find_element("xpath", '//input[@placeholder="Search for products, brands and more"]').send_keys("avaas kurtas")
# time.sleep(2)
# driver.find_element("xpath", '//li[.="Ives Kurtas"]').click()

#############################################################################

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# driver.get(r"C:\Users\Anu\PycharmProjects\pythonProject1\html files\demo.html")
# cars = driver.find_element("xpath", '//select[@id="standard_cars"]')
# obj = Select(cars)
# all_cars = obj.options
############index
# for index in range(len(all_cars)):
#     obj.select_by_index(index)
#     time.sleep(1)

#############reverse index
# for index in range(len(all_cars)-1,-1,-1):
#     obj.select_by_index(index)
#     time.sleep(1)
#########################value
# for car in all_cars:
#     obj.select_by_value(car.get_attribute("value"))

############################ reverse value
# for car in all_cars[::-1]:
#     obj.select_by_value(car.get_attribute("value"))
#     time.sleep(1)

###############################visible text
# for car in all_cars:
#     obj.select_by_visible_text(car.text)
#     time.sleep(1)

 ############################################reverse visible text
# for car in all_cars[::-1]:
#     obj.select_by_visible_text(car.text)
#     time.sleep(1)

#################################selected option
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=path)
# driver.get(r"C:\Users\Anu\PycharmProjects\pythonProject1\html files\demo.html")
# cars = driver.find_element("xpath", '//select[@id="multiple_cars"]')
# obj = Select(cars)
# obj.select_by_index(2)
# obj.select_by_index(4)
# obj.select_by_index(8)
# s = obj.all_selected_options
# for item in s:
#     print(item.text)

####################################################################

# from turtle import *
# color("red")
# begin_fill()
# pensize(5)
# left(50)
# forward(133)
# circle(50,200)
# right(140)
# circle(50,200)
# forward(133)
# end_fill()

#######################################################################

# print("\U0001F917")
# print("\U0001F637")
# print("\U0001F62A")
# print("\U0001F618")
# print("\U0001F600")

######################################################################
# import calendar
# year = 2023
# month = 2
# x = calendar.month(year,month)
# print(x)

# ################################################

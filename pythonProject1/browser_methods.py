import time

from selenium import webdriver
path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
url = "https://demowebshop.tricentis.com/"
driver.get(url)

##minimize, maximize, fullscreen
# driver.maximize_window()
# time.sleep(1)
# driver.minimize_window()
# time.sleep(1)
# driver.fullscreen_window()


#position and size
print(driver.get_window_position())
print(driver.get_window_size())
print(driver.get_window_rect())

#
driver.refresh()
driver.back()
time.sleep(2)
driver.forward()

#name
print(driver.title)
print(driver.current_url)
print(driver.name)

#close and quit
#drive.close()
#driver.quit()








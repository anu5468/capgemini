from selenium import webdriver

c_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
c_driver = webdriver.Chrome(executable_path=c_path)
print(c_driver)


f_path =r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\geckodriver.exe"
f_driver = webdriver.Firefox(executable_path=f_path)
print(f_driver)

e_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\msedgedriver.exe"
e_driver = webdriver.Edge(executable_path=e_path)
print(e_driver)


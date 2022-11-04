import pytest
from selenium import webdriver
from library.config import Config
@pytest.fixture(params=["chrome", "firefox", "edge"])
def init_driver(request):
    browser = request.param

    if browser.lower() == "chrome":
        chrome_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\chromedriver.exe"
        driver = webdriver.Chrome(executable_path=Config.CHROME_PATH)

    elif browser.lower() == "firefox":
        firefox_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\geckodriver.exe"
        driver = webdriver.Firefox(executable_path=Config.FIREFOX_PATH)

    else:
        edge_path = r"C:\Users\Anu\PycharmProjects\pythonProject1\drivers\msedgedriver.exe"
        driver = webdriver.Edge(executable_path=Config.MSEDGE_PATH)

    driver.get(Config.URL)
    driver.maximize_window()
    yield driver
    driver.close()
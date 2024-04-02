import time
from selenium import webdriver
from Utilities.readProperties import Readconfig

class Test_launch_url:
    baseUrl = Readconfig.getApplicationUrl()

    def test_01_launch_url(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseUrl)
        time.sleep(5)
        self.driver.save_screenshot(".\\Screenshots\\Test_Case_01_launch_url.png")
        self.driver.close()
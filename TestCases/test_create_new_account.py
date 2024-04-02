import time
from selenium import webdriver
from PageObjects.CreateNewAccountPage import NewAccount
from Utilities.readProperties import Readconfig
import random
import string
import pytest

def random_gen(size=9, chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for x in range(size))

class Test_media_photos:
    baseUrl = Readconfig.getApplicationUrl()
    email = random_gen()+'@gmail.com'
    password = "Royalrcb@#22"
    
    @pytest.mark.skip()
    def test_New_account(self): 
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseUrl)
        # self.driver.maximize_window()
        self.driver.implicitly_wait(30)

        self.new_acc = NewAccount(self.driver)
        time.sleep(5)
        self.new_acc.click_continue_with_email()
        self.new_acc.click_create_new_account()
        self.new_acc.set_new_email(self.email)
        self.new_acc.set_password(self.password)
        time.sleep(5)
        self.new_acc.click_continue()
        self.new_acc.set_first_name()
        self.new_acc.set_last_name()
        self.new_acc.set_month()
        self.new_acc.set_birth_year()
        time.sleep(5)
        self.new_acc.click_submit()
        time.sleep(30)
        self.new_acc.close_default_panel()
        self.new_acc.close_notification_alert()
        time.sleep(2)
        self.new_acc.take_home_screenshot()
        self.new_acc.check_driver_title()
        time.sleep(5)

        self.element_inside_shadow = self.driver.execute_script(
    "return document.querySelector('x-app[dir=\"ltr\"]').shadowRoot"
    ".querySelector('x-home[class=\"  \"]').shadowRoot"
    ".querySelector('x-home-task-module[dir=\"ltr\"]').shadowRoot"
    ".querySelector('.medium').shadowRoot"
    ".querySelector('sp-button[role=\"button\"][data-test-id=\"task-instagram-square-post-browse\"]');"
)
        self.driver.execute_script("arguments[0].click();", self.element_inside_shadow)
        time.sleep(10)
        self.driver.save_screenshot(".\\Screenshots\\Project.png")
        # self.driver.close()

        
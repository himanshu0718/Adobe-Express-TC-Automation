from selenium.webdriver.common.by import By
from pyshadow.main import Shadow
from selenium import webdriver

class create_project:
    # insta_post = "return document.querySelector('x-app[dir=\"ltr\"]').shadowRoot"
    # ".querySelector('x-home[class=\"  \"]').shadowRoot"
    # ".querySelector('x-home-task-module[dir=\"ltr\"]').shadowRoot"
    # ".querySelector('.medium').shadowRoot"
    # ".querySelector('sp-button[role=\"button\"][data-test-id=\"task-instagram-square-post-browse\"]');"

    def __init__(self, driver):
        self.driver = driver
        self.driver = webdriver.Chrome()
        self.shadow = Shadow(driver)

    def click_instagram_post(self):
        self.element_inside_shadow = self.driver.execute_script(
    "return document.querySelector('x-app[dir=\"ltr\"]').shadowRoot"
    ".querySelector('x-home[class=\"  \"]').shadowRoot"
    ".querySelector('x-home-task-module[dir=\"ltr\"]').shadowRoot"
    ".querySelector('.medium').shadowRoot"
    ".querySelector('sp-button[role=\"button\"][data-test-id=\"task-instagram-square-post-browse\"]');"
)
        self.driver.execute_script("arguments[0].click();", self.element_inside_shadow)
    
    








    

from selenium.webdriver.common.by import By
import pyautogui
from pyshadow.main import Shadow

class NewAccount:
    #locators
    continue_with_email_id = 'signIn'
    create_new_acc_xpath = '//form[@id="EmailForm"]//p/a'
    new_email_id = 'Signup-EmailField'
    password_id = 'Signup-PasswordField'
    continue_xpath = "//span[contains(text(),'Continue')]"
    first_name_id = 'Signup-FirstNameField'
    last_name_id = 'Signup-LastNameField'
    month_id = 'Signup-DateOfBirthChooser-Month-value'
    birth_year_xpath = "//input[@name='bday-year']"
    submit_xpath = "//button[@name='submit']"
    close_id = 'close'

    # action methods
    def __init__(self, driver):
        self.driver = driver
        self.shadow = Shadow(driver)
        self.pyautogui = pyautogui

    def click_continue_with_email(self):
        self.shadow.find_element(f"sp-button[id={self.continue_with_email_id}]").click()
    
    def click_create_new_account(self):
        self.driver.find_element(By.XPATH,self.create_new_acc_xpath).click()

    def set_new_email(self, email):
        self.driver.find_element(By.ID,self.new_email_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.ID,self.password_id).send_keys(password)
    
    def click_continue(self):
        self.driver.find_element(By.XPATH,self.continue_xpath).click()

    def set_first_name(self):
        self.driver.find_element(By.ID, self.first_name_id).send_keys("Tim")

    def set_last_name(self):
        self.driver.find_element(By.ID, self.last_name_id).send_keys("user")
    
    def set_month(self):
        self.driver.find_element(By.ID, self.month_id).click()
        self.driver.find_element(By.XPATH, "//span[contains(text(),'March')]").click()
    
    def set_birth_year(self):
        self.driver.find_element(By.XPATH, self.birth_year_xpath).send_keys("2000")

    def click_submit(self):
        self.driver.find_element(By.XPATH, self.submit_xpath).click()

    def close_default_panel(self):
        self.shadow.find_element(f"button[id={self.close_id}]").click()

    def take_home_screenshot(self):
        self.driver.save_screenshot(".\\Screenshots\\home.png")
    
    def check_driver_title(self):
        home_title = self.driver.title
        if home_title == "Adobe Express":
            print("pass")

    def close_notification_alert(self):
        self.pyautogui.click(x=497, y=242)
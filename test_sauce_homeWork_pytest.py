from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exc
import pytest
from datetime import date
from pathlib import Path

class Test_Sauce:
    def waitForElementVisible(self, locator):
        WebDriverWait(self.driver, 5).until(exc.visibility_of_element_located(locator))

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()

    def test_empty_login(self):

        self.waitForElementVisible((By.ID, "user-name"))
        username_input = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        password_input = self.driver.find_element(By.ID, "password")

        username_input.send_keys("")
        password_input.send_keys("")

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        self.waitForElementVisible((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3"))
        login_info = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_empty_login.png")
        assert login_info.text == "Epic sadface: Username is required"

    
    @pytest.mark.parametrize("username, password", [("1","1"), ("kullaniciadim","sifrem"), ("azizozkrcdg","azizozkrcdg")])
    def test_invalid_login(self, username, password):

        self.waitForElementVisible((By.ID, "user-name"))
        username_input = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        password_input = self.driver.find_element(By.ID, "password")

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        self.waitForElementVisible((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3"))
        login_info = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test_invalid_login-{username}-{password}.png")
        assert login_info.text == "Epic sadface: Username and password do not match any user in this service"

    @pytest.mark.parametrize("username, password", [("standard_user","secret_sauce"), ("problem_user","secret_sauce")])
    def test_valid_login(self, username, password):

        self.waitForElementVisible((By.ID, "user-name"))
        username_input = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, "password"))
        password_input = self.driver.find_element(By.ID, "password")

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        self.waitForElementVisible((By.XPATH, "//*[@id='header_container']/div[2]/span"))
        productText = self.driver.find_element(By.XPATH, "//*[@id='header_container']/div[2]/span")
        self.driver.save_screenshot(f"{self.folderPath}/test_valid_login-{username}-{password}.png")
        assert productText.text == "Products"
        



    
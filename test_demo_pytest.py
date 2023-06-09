from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exc
import pytest
from pathlib import Path
from datetime import date

class Test_demoClass:
    def waitForElementVisible(self, locator):
        WebDriverWait(self.driver,5).until(exc.visibility_of_element_located(locator))

    # her testten önce çağrılır
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")

        # günün tarihini al bu tarih ile bir klasör var mı kontrol et yoksa oluştur
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        

    # her testten sonra çağrılır
    def teardown_method(self):
        self.driver.quit()

    def test_demoFunc(self):
        #3A Act Arreng Assert
        text = "Hello"
        assert text == "Hello"
    
    def test_demoFunc2(self):
        assert True
    
    @pytest.mark.parametrize("username,password", [("1","1"), ("kullaniciadim","sifrem")])
    def test_invalid_login(self, username, password):
        self.waitForElementVisible((By.ID,"user-name"))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID,"password"))
        passwordInput = self.driver.find_element(By.ID, "password")

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.waitForElementVisible((By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3"))
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"

from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exc


class Test_Sauce:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")


    # Boş kullanıcı ve şifre giriş kontrolü
    def blankEntry(self):
        WebDriverWait(self.driver, 5).until(exc.visibility_of_element_located((By.ID,"user-name")))
        username_input = self.driver.find_element(By.ID, "user-name")
        password_input = self.driver.find_element(By.ID, "password")

        username_input.send_keys("")
        password_input.send_keys("")
        
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        WebDriverWait(self.driver, 5).until(exc.visibility_of_element_located((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")))
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"Boş username ve password girişi test sonucu : {testResult}")
        

    # Boş şifre giriş kontrolü
    def blankPassword(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver, 5).until(exc.visibility_of_element_located((By.ID,"user-name")))
        username_input = self.driver.find_element(By.ID, "user-name")
        password_input = self.driver.find_element(By.ID, "password")

        username_input.send_keys("abcdefg")
        password_input.send_keys("")
        
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        WebDriverWait(self.driver, 5).until(exc.visibility_of_element_located((By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")))
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Boş şifre girişi test sonucu : {testResult}")

        
    # Kullanıcı adı "locked_out_user" şifre "secre_sauce" kontrolü
    def loginAttempt1(self):
        self.driver.get("https://www.saucedemo.com/")
        WebDriverWait(self.driver, 5).until(exc.visibility_of_element_located((By.ID,"user-name")))
        username_input = self.driver.find_element(By.ID, "user-name")
        password_input = self.driver.find_element(By.ID, "password")
       
        username_input.send_keys("locked_out_user")
        password_input.send_keys("secret_sauce")
        
        login_button = self.driver.find_element(By.ID, "login-button")
        login_button.click()

        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"'locked_out_user' kullanıcı adı ve 'secret_sauce' şifresi ile giriş testi sonucu : {testResult}")


    # Kullanıcı adı ve şifre boş girildiğinde yanda çıkan kırmızı işaretlerin kapatılması kontrolü
    def loginAttempt2(self):
        pass
        # Sonradan doldurulacak!



testSauce = Test_Sauce()
testSauce.blankEntry()
testSauce.blankPassword()
testSauce.loginAttempt1()

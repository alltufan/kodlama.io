from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_Sauce:
    
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url="https://www.saucedemo.com"
        
    
    def engine(self):
        self.driver.get(self.url)
        sleep(3)
        self.usernameInput=self.driver.find_element(By.ID,'user-name')
        self.passwordInput=self.driver.find_element(By.ID,'password')
        sleep(3)
    def button(self):
        loginBtn=self.driver.find_element(By.ID,'login-button')
        loginBtn.click()
        sleep(2)
    
    
    def usernameError(self):
        self.engine()
        self.usernameInput.send_keys("")
        self.passwordInput.send_keys("1")
        self.button()
        sleep(10)
        
    def passwordError(self):
        self.engine()
        self.usernameInput.send_keys("1")
        self.passwordInput.send_keys("")
        self.button()
        sleep(10)
        
    def invalidLogin(self):
        self.engine()
        self.usernameInput.send_keys("locked_out_user")
        self.passwordInput.send_keys("secret_sauce")
        self.button()
        sleep(10)
        
    def loginUser(self,a,b):
        self.engine()
        self.usernameInput.send_keys(a)
        self.passwordInput.send_keys(b)
        self.button()
        sleep(2)
        if self.usernameInput=="" and self.passwordInput=="":
            errorBtn=self.driver.find_element(By.CLASS_NAME,'error-button')
            errorBtn.click()
        sleep(10)
    
    def displayProduct(self):
        self.loginUser("standard_user","secret_sauce")
        product=self.driver.find_elements(By.CLASS_NAME,'inventory_item')
        print(f"Gösterilen Ürün Sayısı:{len(product)}")
        sleep(30)
        
        
test=Test_Sauce()

    
test.usernameError()
test.passwordError()
test.invalidLogin()
test.loginUser("","")
test.loginUser("standard_user","secret_sauce")
test.displayProduct()
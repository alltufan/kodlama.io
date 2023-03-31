from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.webdriver.support import expected_conditions as ec 
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path 
from datetime import date


class Test_Demo:
    def setupMethod(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True) #günün tarihini al bu tarih ile klasör var mı kontrol et yoksa oluştur.
        
    def teardown_method(self):
        self.driver.quit()
        
    def Login(self,username,password):
        self.setupMethod()
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,'user-name')))
        usernameinput=self.driver.find_element(By.ID,'user-name')
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,'password')))
        passwordinput=self.driver.find_element(By.ID,'password')
        usernameinput.send_keys(username)
        passwordinput.send_keys(password)
        WebDriverWait(self.driver,5).until(ec.visibility_of_element_located((By.ID,'login-button')))
        loginBtn=self.driver.find_element(By.ID,'login-button')
        loginBtn.click()
        
    @pytest.mark.parametrize("username,password",[("1","1")])    
    def test_invalid_login(self,username,password):
        self.Login(username,password)
        errormessage=self.driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')
        WebDriverWait(self.driver,10).until(ec.visibility_of_all_elements_located((By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')))
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}_{password}.png ")
        assert errormessage.text == "Epic sadface: Username and password do not match any user in this service"
    
    @pytest.mark.parametrize("username,password",[("1","secret_sauce")])   
    def test_invalid_username_Login(self,username,password):
        self.Login(username,password)
        errormessage=self.driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')
        WebDriverWait(self.driver,5).until(ec.visibility_of_all_elements_located((By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')))
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}_{password}.png ")
        assert errormessage.text == "Epic sadface: Username and password do not match any user in this service"
        
    @pytest.mark.parametrize("username,password",[("locked_out_user","1")])   
    def test_invalid_password_Login(self,username,password):
        self.Login(username,password)
        errormessage=self.driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')
        self.wait((By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3'),5)
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}_{password}.png ")
        assert errormessage.text == "Epic sadface: Username and password do not match any user in this service"
        
    def emptyLogin(self):
        self.Login("","")
        errorMessage=self.driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]')
        self.wait((By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]'),5)
        self.driver.save_screenshot(f"{self.folderPath}/test-empty-login.png")
        assert errorMessage.text=="Epic sadface: Username is required"
    
    @pytest.mark.skip() 
    def test_valid_Login(self,username,password):
        username="standard_user"
        password="secret_sauce"
        self.Login(username,password)
        errormessage=self.driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')
        self.wait((By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3'),5)
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}_{password}.png ")
    
         
    def test_productList(self):
        self.Login("standard_user","secret_sauce")
        product=self.driver.find_elements(By.CLASS_NAME,'inventory_item')
        print(f"Gösterilen Ürün Sayısı:{len(product)}")
        self.wait((By.CLASS_NAME,'inventory_list'),5)
        self.driver.save_screenshot(f"{self.folderPath}/test-product-list-{len(product)}-adet-ürün.png")
        
    def shopping(self):
        self.Login("standard_user","secret_sauce")
        self.btnlocator('/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button')
        self.btnlocator('/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/button')
        self.wait((By.XPATH,'/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button'),5)
        self.screenShot("shopping")

        
    def btnlocator(self,Xpath):
        self.driver.find_element(By.XPATH,Xpath).click()
        
    def wait(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_all_elements_located((locator)))
    
    def screenShot(self,topic):
        self.driver.save_screenshot(f"{self.folderPath}/test-{topic}.png")
        
test = Test_Demo()

#test.test_invalid_login("1","1")
#test.test_invalid_username_Login("1","secret_sauce")
#test.test_invalid_password_Login("locked_out_user","1")
#test.test_valid_Login("locked_out_user","secret_sauce")
#test.test_productList()
test.shopping()

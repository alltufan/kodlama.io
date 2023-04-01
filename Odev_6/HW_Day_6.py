from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from datetime import date
from pathlib import Path
from constants import Constants
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from time import sleep
import sys 

class Sauce_Demo:
    def setup_mode(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(Constants.url)
        self.folderPath =str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        
    def teardown_method(self):
        self.driver.quit()
        
    def wait(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located((locator)))
     
    @pytest.mark.parametrize("username,password",[("standard_user", "secret_sauce")])    
    def valid_login(self,username,password):
        self.setup_mode()
        username_inpt=self.driver.find_element(By.XPATH,Constants.usernameXPATH)
        self.wait((By.ID,Constants.usernameId),5)
        password_inpt=self.driver.find_element(By.XPATH,Constants.passwordXPATH)
        self.wait((By.ID,Constants.passwordId),5)
        
        action = ActionChains(self.driver)
        action.send_keys_to_element(username_inpt,username)
        action.send_keys_to_element(password_inpt,password)
        action.perform()
        login_btn=self.driver.find_element(By.ID,Constants.loginBtnId)
        login_btn.click()
        
        
    def test_page(self):
        self.setup_mode()
        self.valid_login("standard_user", "secret_sauce")
        
        self.wait((By.ID,Constants.menuButtonID),5)
        menu_btn=self.driver.find_element(By.ID,Constants.menuButtonID)
        menu_btn.click()
        
        self.wait((By.ID,Constants.aboutBtnID),5)
        about_btn=self.driver.find_element(By.ID,Constants.aboutBtnID).click()
        
        sc_file=str(Path(self.folder_path)/f"test-page-about.png")
        self.driver.save_screenshot(sc_file)
    
    @pytest.mark.parametrize("username,password",[("locked_out_user", "secret_sauce")])
    def banned_acc_log(self,username,password):
        self.setup_mode()
        username_inpt=self.driver.find_element(By.XPATH,Constants.usernameXPATH)
        self.wait((By.ID,Constants.usernameId),5)
        password_inpt=self.driver.find_element(By.XPATH,Constants.passwordXPATH)
        self.wait((By.ID,Constants.passwordId),5)
        
        action = ActionChains(self.driver)
        action.send_keys_to_element(username_inpt,username)
        action.send_keys_to_element(password_inpt,password)
        action.perform()
        
        login_btn=self.driver.find_element(By.ID,Constants.loginBtnId).click()
        error_msg=self.driver.find_element(By.XPATH,Constants.errorXPATH)
        sc_file=str(Path(self.folderPath)/"test-banned-account-login.png")
        self.driver.save_screenshot(sc_file)
        
        assert error_msg.text == Constants.ErrorMessage_blockedUser
    
    @pytest.mark.parametrize("username,password",[("1", "secret_sauce")])    
    def invalid_username_login(self,username,password):
        self.setup_mode()
        username_inpt=self.driver.find_element(By.XPATH,Constants.usernameXPATH)
        self.wait((By.ID,Constants.usernameId),5)
        password_inpt=self.driver.find_element(By.XPATH,Constants.passwordXPATH)
        self.wait((By.ID,Constants.passwordId),5)
        
        action = ActionChains(self.driver)
        action.send_keys_to_element(username_inpt,username)
        action.send_keys_to_element(password_inpt,password)
        action.perform()
        
        login_btn=self.driver.find_element(By.ID,Constants.loginBtnId).click()
        error_msg=self.driver.find_element(By.XPATH,Constants.errorXPATH)
        sc_file=str(Path(self.folderPath)/"test-invalid-username-login.png")
        self.driver.save_screenshot(sc_file)
        
        assert error_msg.text == Constants.ErrorMessage_invalidLogin
        
    @pytest.mark.parametrize("username,password",[("standard_user", "1")])    
    def invalid_password_login(self,username,password):
        self.setup_mode()
        username_inpt=self.driver.find_element(By.XPATH,Constants.usernameXPATH)
        self.wait((By.ID,Constants.usernameId),5)
        password_inpt=self.driver.find_element(By.XPATH,Constants.passwordXPATH)
        self.wait((By.ID,Constants.passwordId),5)
        
        action = ActionChains(self.driver)
        action.send_keys_to_element(username_inpt,username)
        action.send_keys_to_element(password_inpt,password)
        action.perform()
        
        login_btn=self.driver.find_element(By.ID,Constants.loginBtnId).click()
        error_msg=self.driver.find_element(By.XPATH,Constants.errorXPATH)
        sc_file=str(Path(self.folderPath)/"test-invalid-password-login.png")
        self.driver.save_screenshot(sc_file)
        
        assert error_msg.text == Constants.ErrorMessage_invalidLogin
    
    @pytest.mark.parametrize("username,password",[("", "")])    
    def empty_login(self,username,password):
        self.setup_mode()
        username_inpt=self.driver.find_element(By.XPATH,Constants.usernameXPATH)
        self.wait((By.ID,Constants.usernameId),5)
        password_inpt=self.driver.find_element(By.XPATH,Constants.passwordXPATH)
        self.wait((By.ID,Constants.passwordId),5)
        
        action = ActionChains(self.driver)
        action.send_keys_to_element(username_inpt,username)
        action.send_keys_to_element(password_inpt,password)
        action.perform()
        
        login_btn=self.driver.find_element(By.ID,Constants.loginBtnId).click()
        error_msg=self.driver.find_element(By.XPATH,Constants.errorXPATH)
        sc_file=str(Path(self.folderPath)/"test-empty-login.png")
        self.driver.save_screenshot(sc_file)
        
        assert error_msg.text == Constants.ErrorMessage_Empty
        
    def item_count(self):
        self.valid_login("standard_user", "secret_sauce")
        self.wait((By.XPATH,Constants.inventorycontainerXPATH),5)
        items=self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(len(items))
        assert self.driver.find_elements(By.CLASS_NAME,"inventory_item") == items
        
    def add_button(self):
        self.valid_login("standard_user", "secret_sauce")
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-onesie\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-test.allthethings()-t-shirt-(red)\"]").click()
        sc_file1=str(Path(self.folderPath)/"test-shopping-add.png")
        self.driver.save_screenshot(sc_file1)
        self.driver.find_element(By.LINK_TEXT, "6").click()
        sc_file2=str(Path(self.folderPath)/"test-shopping-remove.png")
        self.driver.save_screenshot(sc_file2)
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-backpack\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-bike-light\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-bolt-t-shirt\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-fleece-jacket\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-sauce-labs-onesie\"]").click()
        self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"remove-test.allthethings()-t-shirt-(red)\"]").click()
        
        sc_file3=str(Path(self.folderPath)/"test-addButton-end.png")
        self.driver.save_screenshot(sc_file3)
        
    def logout_button(self):
        self.valid_login("standard_user", "secret_sauce")
        self.wait((By.ID,Constants.pageID),5)
        self.driver.find_element(By.ID,Constants.menuButtonID).click()
        sc_file=str(Path(self.folderPath)/"test-logout.png")
        self.driver.save_screenshot(sc_file)
        self.driver.find_element(By.ID,Constants.logoutID).click()
        
        assert self.driver.current_url == Constants.url
    @pytest.mark.parametrize("username,password",[("problem_user", "secret_sauce")])    
    def problem_user_login(self,username,password):
        puitems=6
        self.valid_login(username,password)
        self.wait((By.ID,Constants.pageID),10)
        #sc_file1=str(Path(self.folderPath)/"test-problem_user.png")
        #self.driver.save_screenshot(sc_file1)
        items=self.driver.find_elements(By.CLASS_NAME,Constants.pu_itemClass)
        print(len(items))
        self.driver.find_element(By.XPATH,Constants.pu_item_Xpath).click()
        sc_file=str(Path(self.folderPath)/"test-pu-addcard.png")
        self.driver.save_screenshot(sc_file)
        menu=self.driver.find_element(By.ID,Constants.pumenuID)
        menu.click()
        self.wait((By.ID,Constants.pumenuID),5)
        lgout=self.driver.find_element(By.ID,Constants.pulogoutID)
        lgout.click()
    
        assert len(items) == puitems
        assert self.driver.current_url == Constants.url
        
    def twitter(self):
        self.setup_mode()
        self.driver.get(Constants.url_twitter)
        self.wait((By.CLASS_NAME,Constants.twitter_class_main),5)
        sc=str(Path(self.folderPath)/"test-twitter-display.png")
        self.driver.save_screenshot(sc)
        
        assert self.driver.current_url == Constants.url_twitter
        
        
        
        




Deneme = Sauce_Demo()
#Deneme.banned_acc_log("locked_out_user", "secret_sauce")
#Deneme.invalid_password_login("standard_user", "1")
#Deneme.invalid_username_login("1", "secret_sauce")
#Deneme.empty_login("","")
#Deneme.item_count()
#Deneme.add_button()
#Deneme.logout_button()
#Deneme.problem_user_login("problem_user", "secret_sauce")

Deneme.twitter()
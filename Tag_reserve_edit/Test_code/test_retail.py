# app.py - The main executable file
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from time import sleep
from Test_locators import locators
from Test_data import data
import pytest


class Test_Logimax:
    @pytest.fixture
    

    def booting_function(self):
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
       self.driver.get(data.Logi_Data().url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(5)
  
    
   
    def test_Billing(self,booting_function):   
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().customer_order).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().creat_order).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().search).send_keys(data.Logi_Data().Search_code)
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Edit).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Edit option open Successfully')
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Gross_weight).clear()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Gross_weight).send_keys(data.Logi_Data().G_weight)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Gross Weight Edit: {a}'.format(a = data.Logi_Data().G_weight))
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().type).click()
        sleep(5)
        type = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        type.send_keys('piece')
        type.send_keys(Keys.RETURN) 
        assert self.driver.title == 'Logimax Technology | Admin'
        print('MC Type Edit: {a}'.format( a = 'piece'))
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Mc_value).clear()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Mc_value).send_keys(data.Logi_Data().value)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('MC Value Edit : {a}'.format(a = data.Logi_Data().value))
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().other_charge).click()
        sleep(5)
        Other_charge = Select(self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Charge_name))
        Other_charge .select_by_value('2')
        selected_option = Other_charge.first_selected_option
        selected_text = selected_option.text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Charge Name Edit: {a}'.format(a = selected_text))   
        sleep(5) 
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().value).clear()
        sleep(5) 
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().value).send_keys(data.Logi_Data().other_charge_value)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Other Charge Value Edit : {a}'.format(a = data.Logi_Data().other_charge_value))
        sleep(5)
           
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Save_charge).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().description).click()
        sleep(5) 
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().item_description).clear()
        sleep(5) 
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().item_description).send_keys(data.Logi_Data().items_describe)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Item Description Edit: {a}'.format(a = data.Logi_Data().items_describe))
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Add_description).click() 
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Due_days).clear()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Due_days).send_keys(data.Logi_Data().no_of_days)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('No Of Due Days Edit : {a}'.format(a = data.Logi_Data().no_of_days))
        sleep(5)
        
        
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().New_tag_scan).send_keys(data.Logi_Data().Tag_code)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Add New Tag   : {a}'.format( a = data.Logi_Data().Tag_code))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Tag_search).click()
        sleep(20)
    
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Gross_weight2).clear()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Gross_weight2).send_keys(data.Logi_Data().G_weight2)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('New Tag Gross Weight: {a}'.format(a = data.Logi_Data().G_weight2))
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Mc_type2).click()
        sleep(5)
        Mc_type = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        Mc_type.send_keys('piece')
        Mc_type.send_keys(Keys.RETURN) 
        assert self.driver.title == 'Logimax Technology | Admin'
        print('New Tag MC Type : {a}'.format( a = 'piece'))
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Mc_value2).clear()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Mc_value2).send_keys(data.Logi_Data().value2)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('New Tag MC Value: {a}'.format(a = data.Logi_Data().value2))
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().other_charge2).click()
        sleep(5)
        Other_charge = Select(self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Charge_name))
        Other_charge .select_by_value('2')
        selected_option = Other_charge.first_selected_option
        selected_text = selected_option.text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('New Tag Charge Name : {a}'.format(a = selected_text))   
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().value).clear()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().value).send_keys(data.Logi_Data().other_charge_value2)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('New Tag Other Charge Value : {a}'.format(a = data.Logi_Data().other_charge_value2))
        sleep(5)         
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Save_charge).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().description2).click()
        sleep(5) 
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().item_description).send_keys(data.Logi_Data().items_describe2)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('New Tag Item Description: {a}'.format(a = data.Logi_Data().items_describe2))
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Add_description).click() 
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Due_days2).send_keys(data.Logi_Data().no_of_days2)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('New Tag No Of Due Days : {a}'.format(a = data.Logi_Data().no_of_days2))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().save_page).click() 
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Tag Reserve Edit option Working Successfully')
# app.py - The main executable file
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from time import sleep
from Test_locators import locators
from Test_data import data
import pytest


class Test_Logimax:
    @pytest.fixture
    

    def booting_function(self):
       self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
       self.driver.get(data.Logi_Data().url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(5)
  
    
   
    def test_Billing(self,booting_function):   
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(20)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().customer_order).click()
        sleep(20)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().creat_order).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().search).send_keys(data.Logi_Data().search_id)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('search order number : {a}'.format( a = data.Logi_Data().search_id))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().edit).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Edit option : Edit option open successfully')
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Gross_weight).clear()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Gross_weight).send_keys(data.Logi_Data().G_weight)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Gross Weight edit : {a}'.format(a = data.Logi_Data().G_weight))     
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Peace).clear()     
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Peace).send_keys(data.Logi_Data().Pcs)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('No Of PCs edit : {a}'.format(a = data.Logi_Data().Pcs))
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Wast).clear()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Wast).send_keys(data.Logi_Data().wast_percentage)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Wast percentage edit : {a}'.format(a = data.Logi_Data().wast_percentage))
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Mc_value).clear()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Mc_value).send_keys(data.Logi_Data().value)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('MC Value edit : {a}'.format(a = data.Logi_Data().value))
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().other_charge).click()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().add_new).click()
        sleep(5)
        Other_charge = Select(self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Charge_name))
        Other_charge .select_by_value('2')
        selected_option = Other_charge.first_selected_option
        selected_text = selected_option.text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Charge Name edit : {a}'.format(a = selected_text))   
        sleep(5) 
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().value).clear()
        sleep(5) 
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().value).send_keys(data.Logi_Data().other_charge_value)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Other Charge Value edit : {a}'.format(a = data.Logi_Data().other_charge_value))
        sleep(5) 
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Save_charge).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Due_days).clear()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Due_days).send_keys(data.Logi_Data().no_of_days)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('No Of Due Days edit : {a}'.format(a = data.Logi_Data().no_of_days))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().save_page).click() 
        assert self.driver.title == 'Logimax Technology | Admin'
        print('All Edit option worked successfully')
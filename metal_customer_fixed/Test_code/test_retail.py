# app.py - The main executable file
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
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
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Add_order).click()
        sleep(5)
        customer = self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Customer)
        sleep(10)
        customer.send_keys('Hari')
        sleep(5)
        customer.send_keys(Keys.BACK_SPACE)
        sleep(10)
        se_ver = self.driver.find_elements(By.XPATH, "//ul[@id='ui-id-1']//li")
        print('Total',len(se_ver))
        customer_name = 'Hari-6380399326'
        for element in se_ver:
            if element.text == customer_name:
                element.click()
                break
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Order_Branch).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box).send_keys ('HEAD OFFICE')
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Select Branch name : {a}'.format(a = 'HEAD OFFICE'))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Sales_Employee).click()
        sleep(5)
        employee = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        employee.send_keys('111-Logimax Developer')
        employee.send_keys(Keys.RETURN) 
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Sales Employee name  : {a}'.format( a='111-Logimax Developer'))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().balance_type).click()
        type = self.driver.find_element(By.XPATH, '(//*[@for="metal_bal_type"])').text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Balance Type : {a}'.format( a=type ))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Order_Type).click()
        customer_order = self.driver.find_element(By.XPATH, '(//*[@for="customer_order"])').text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Order Type : {a}'.format( a = customer_order ))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().order_rate).click()
        order_rate = self.driver.find_element(By.XPATH, '(//*[@for="customer_order"])[2]').text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Rate Type : {a}'.format( a = order_rate ))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().add_item).click()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().product).click()
        sleep(5)
        product = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        product.send_keys('MRP GOLD')
        product.send_keys(Keys.RETURN) 
        assert self.driver.title == 'Logimax Technology | Admin'
        print('product name  : {a}'.format( a = 'MRP GOLD'))
        sleep(20)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().design).click()
        sleep(5)
        design = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        design.send_keys('MACHINE MADE')
        design.send_keys(Keys.RETURN) 
        assert self.driver.title == 'Logimax Technology | Admin'
        print('design name  : {a}'.format( a = 'MACHINE MADE'))
        sleep(5)        
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().sub_design).click()
        sleep(5)
        sub_design = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        sub_design.send_keys('HOLLOW ROPE')
        sub_design.send_keys(Keys.RETURN) 
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Sub design name  : {a}'.format( a = 'HOLLOW ROPE'))
        sleep(5)
        purity = Select(self.driver.find_element(by=By.ID,value=locators.Logi_Locators().purity))
        purity.select_by_value('18')
        selected_option = purity.first_selected_option
        selected_text = selected_option.text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('purity value : {a}'.format(a = selected_text))   
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Gross_weight).send_keys(data.Logi_Data().G_weight)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Gross Weight: {a}'.format(a = data.Logi_Data().G_weight))    
        
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Peace).send_keys(data.Logi_Data().Pcs)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('No Of PCs: {a}'.format(a = data.Logi_Data().Pcs))
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Wast).send_keys(data.Logi_Data().wast_percentage)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Wast percentage: {a}'.format(a = data.Logi_Data().wast_percentage))
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Mc_type).click()
        sleep(5)
        Mc_type = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        Mc_type.send_keys('piece')
        Mc_type.send_keys(Keys.RETURN) 
        assert self.driver.title == 'Logimax Technology | Admin'
        print('MC Type : {a}'.format( a = 'piece'))
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Mc_value).clear()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Mc_value).send_keys(data.Logi_Data().value)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('MC Value: {a}'.format(a = data.Logi_Data().value))
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().other_charge).click()
        sleep(5)
        Other_charge = Select(self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Charge_name))
        Other_charge .select_by_value('2')
        selected_option = Other_charge.first_selected_option
        selected_text = selected_option.text
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Charge Name : {a}'.format(a = selected_text))   
        sleep(5) 
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().value).clear()
        sleep(5) 
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().value).send_keys(data.Logi_Data().other_charge_value)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Other Charge Value : {a}'.format(a = data.Logi_Data().other_charge_value))
        sleep(5) 
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Save_charge).click()
        sleep(5) 
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().description).click()
        sleep(5) 
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().item_description).send_keys(data.Logi_Data().items_describe)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('Item Description: {a}'.format(a = data.Logi_Data().items_describe))
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Add_description).click() 
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Due_days).send_keys(data.Logi_Data().no_of_days)
        assert self.driver.title == 'Logimax Technology | Admin'
        print('No Of Due Days : {a}'.format(a = data.Logi_Data().no_of_days))
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().save_page).click() 
    
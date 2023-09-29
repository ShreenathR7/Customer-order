# locators.py - File where all The HTML Locators are Kept
class Logi_Locators:
    username_inputBox = 'username'

    password_inputBox = 'password'
     
    signButton ='(//*[@id="submit_login"])'
    
    side_bar = '(//*[@role="button"])'
    
    customer_order = '(//*[@class="fa fa-pie-chart text-orange"])[3]'
    
    creat_order  = '(//*[@class="fa fa-circle-o"])[89]'
    
    search = '(//*[@class="form-control input-sm"])[2]'
    
    edit = 'edit'
    
    text_box = '(//*[@role="textbox"])'
    
   
    Gross_weight = "weight_1"
    
    Peace = "qty_1"
    
    Wast = "o_item[1][wast_percent]"
    
   
    Mc_value = "o_item[1][mc]"
    
    other_charge = '(//*[@class="btn btn-success"])[4]'

    add_new = 'add_new_charge'
    
    Charge_name="est_stones_item[id_charge][]"
    
    value = "est_stones_item[value_charge][]"
    
    Save_charge = "update_charge_details"
    
    Due_days= '(//*[@class="form-control due_date"])'
    
    save_page = "create_order"
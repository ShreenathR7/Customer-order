# locators.py - File where all The HTML Locators are Kept
class Logi_Locators:
    username_inputBox = 'username'

    password_inputBox = 'password'
     
    signButton ='(//*[@id="submit_login"])'
    
    side_bar = '(//*[@role="button"])'
    
    customer_order = '(//*[@class="fa fa-pie-chart text-orange"])[3]'
    
    creat_order  = '(//*[@class="fa fa-circle-o"])[88]'
    
    Add_order ="add_Order"
    
    Customer = "cus_name"
    
    Order_Branch = "select2-branch_select-container"
    
    text_box = '(//*[@role="textbox"])'
    
    Sales_Employee = 'select2-issue_employee-container'
                     
    balance_type = "cash_bal_type"
    
    tag_order = "tag_order"
    
    order_rate="order_rate"
    
    New_tag_scan = 'est_tag_scan'
    
    Tag_search = 'tag_search'
    
    Gross_weight = "weight_1"
    
    size = '(//*[@role="presentation"])[16]'
    
    Peace = "qty_1"
    
    Wast = "o_item[1][wast_percent]"
    
    Mc_type = '(//*[@role="presentation"])[16]'
    
    Mc_value = "o_item[1][mc]"
    
    other_charge = '(//*[@class="btn btn-success"])[4]'
    
    Charge_name="est_stones_item[id_charge][]"
    
    value = "est_stones_item[value_charge][]"
    
    Save_charge = "update_charge_details"
    
    description = '(//*[@class="btn btn-default btn-sm"])[2]'
    
    item_description = "description"
    
    Add_description  = '(//*[@class="btn btn-success add_order_desc"])'
    
    Due_days= '(//*[@class="form-control due_date"])'
    
    save_page = "create_order"
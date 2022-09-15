import time
import re
import selenium
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
import properties as properties
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import keys_to_typing

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# web_driver = webdriver.Chrome(options=options)

# serv = Service("C:/Users/vinow/PycharmProjects/Corpex/Corpex/Drivers/chromedriver.exe")

# web_driver = webdriver.Chrome(executable_path='C:/Users/vinow/PycharmProjects/Corpex/Corpex/Drivers/chromedriver.exe')
serv = Service("C:/Users/vinow/PycharmProjects/Corpex/Corpex/Drivers/chromedriver.exe")
web_driver = webdriver.Chrome(service=serv)


# driver_path = "C:/Users/vinow/PycharmProjects/Corpex/Corpex/Drivers/chromedriver.exe"
# web_driver = webdriver.Chrome(driver_path)

def open_browser(url):
    web_driver.get(url)
    web_driver.maximize_window()


# def open_browser(url):

# webdriver.Chrome()
def page_refresh():
    web_driver.refresh()


def wait_and_find(element, locator):
    try:
        if locator == 'ID':
            waitElement = WebDriverWait(web_driver, 120).until(
                EC.presence_of_element_located((By.ID, element)))
        elif locator == 'XPATH':
            waitElement = WebDriverWait(web_driver, 120).until(
                EC.presence_of_element_located((By.XPATH, element)))
        elif locator == 'CSS':
            WebDriverWait(web_driver, 120).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, element)))

    except:
        print("No element present for the locator " + element)

    return waitElement


def wait_and_find_elements_list(element, locator):
    if locator == 'ID':
        waitElements = WebDriverWait(web_driver, 30).until(
            EC.presence_of_all_elements_located((By.ID, element)))
    elif locator == 'XPATH':
        waitElements = WebDriverWait(web_driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, element)))
    return waitElements


def string_equals(string1, string2):
    return string1 == string2


def is_displayed(element):
    return web_driver.find_element(By.XPATH, element).is_displayed()





def is_selectByallvisibletext(element, locator):
    try:
        if locator == 'ID':
            visiblealltext = WebDriverWait(web_driver, 30).until(
                EC.visibility_of_all_elements_located((By.ID, element)))
        elif locator == 'XPATH':
            visiblealltext = WebDriverWait(web_driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, element)))
        elif locator == 'CSS':
            visiblealltext = WebDriverWait(web_driver, 30).until(
                EC.visibility_of_element_located(By.CSS_SELECTOR, element))
    except:
        print("No element present for the locator " + element)

    return visiblealltext


def is_selectByvisibletext(element, locator):
    try:
        if locator == 'ID':
            visibletext = WebDriverWait(web_driver, 30).until(
                Select.select_by_visible_text((By.ID, element)))
        elif locator == 'XPATH':
            visibletext = WebDriverWait(web_driver, 30).until(
                Select.select_by_visible_text((By.XPATH, element)))
        elif locator == 'CSS':
            visibletext = WebDriverWait(web_driver, 30).until(Select.select_by_visible_text(By.CSS_SELECTOR, element))
    except:
        print("No element present for the locator " + element)

    return visibletext


def login_to_moonshot(username, password):
    wait_and_find(properties.user_name_textbox, 'XPATH').send_keys(username)
    wait_and_find(properties.password_textbox, 'XPATH').send_keys(password)
    time.sleep(5)
    wait_and_find(properties.login_button, 'XPATH').click()


def pop_up_username(username):
    handles = web_driver.window_handles
    web_driver.switch_to.window(handles[1])

    wait_and_find(properties.pop_up_username, 'XPATH').send_keys(username)
    wait_and_find(properties.pop_up_submit_button, 'XPATH').click()
    # wait_and_find(properties)


def pop_up_password(username):
    handles = web_driver.window_handles
    web_driver.switch_to.window(handles[1])

    wait_and_find(properties.pop_up_pass, 'XPATH').send_keys(username)
    wait_and_find(properties.pop_up_submit, 'XPATH').click()


def jump_to_click_dropdown():
    time.sleep(60)
    handles = web_driver.window_handles
    web_driver.switch_to.window(handles[0])
    wait_and_find(properties.jump_to_client_dropdown, 'XPATH').click()


def amazon_dropdown_value():
    wait_and_find(properties.Amazon_dropdown_value, 'XPATH').click()


def add_plan_button():
    time.sleep(60)
    handles = web_driver.window_handles
    web_driver.switch_to.window(handles[1])

    wait_and_find(properties.Add_plan_button, 'XPATH').click()


def search_vision(username):
    # time.sleep(60)
    # handles = web_driver.window_handles
    # web_driver.switch_to.window(handles[1])

    wait_and_find(properties.search_vision_textbox, 'XPATH').send_keys(username)
    wait_and_find(properties.search_click, 'XPATH').click()


def vision_link_dropdown():
    wait_and_find(properties.vision_plan_link, 'XPATH').click()


# def add_a_claim():
#     wait_and_find(properties.add_claim_button, 'XPATH').click()
#     wait_and_find(properties.manage_liablity_link,
#     'XPATH').click()
#     # wait_and_find(properties.client_name_textbox, 'XPATH').send_keys(clientname)
#     # wait_and_find(properties.continue_button, 'XPATH').click()
#     # wait_and_find(properties.client_name, 'XPATH').send_keys()
#     # wait_and_find(properties.temporary_claim_file, 'XPATH').click()
#
#     # def select_by_value(self, webElement, value):
#     #     options = webElement.find_elements_by_tag_name("option")
#     #     for option in options:
#     #         if option.text == value:
#     #             webElement.click()
#     #             webElement.send_keys(option.text, Keys.RETURN)
#
#
# def is_selectbyvalue(element, locator):
#     try:
#         if locator == 'ID':
#             selectvalue = WebDriverWait(web_driver, 30).until(
#                 Select.select_by_value((By.ID, element)))
#         elif locator == 'XPATH':
#             selectvalue = WebDriverWait(web_driver, 30).until(
#                 Select.select_by_value((By.XPATH, element)))
#         elif locator == 'CSS':
#             selectvalue = WebDriverWait(web_driver, 30).until(Select.select_by_value(By.CSS_SELECTOR, element))
#
#     except:
#         print("No element present for the locator " + element)
#
#     return selectvalue
#
#
# def add_management_liablity(clientname):
#     handles = web_driver.window_handles
#     web_driver.switch_to.window(handles[1])
#
#     wait_and_find(properties.client_name_textbox, 'XPATH').send_keys(clientname)
#     time.sleep(2)
#     wait_and_find(properties.client_name_click, 'XPATH').click()
#     # wait_and_find(properties.client_name_textbox,'XPATH').click()
#
#
# def select_claimtype_dropdown():
#     wait_and_find(properties.select_claim_type, 'XPATH').click()
#     time.sleep(5)
#     wait_and_find(properties.select_cyber, 'XPATH').click()
#
#
# def select_incident_claim_dropdown():
#     wait_and_find(properties.select_incident_claim_dropdown, 'XPATH').click()
#     time.sleep(5)
#     wait_and_find(properties.select_claim_in_dropdown, 'XPATH').click()
#
#
# def select_primary_dropdown():
#     wait_and_find(properties.primary_carrier_dropdown, 'XPATH').click()
#     time.sleep(5)
#     wait_and_find(properties.select_allianz_primary_dropdown, 'XPATH').click()
#
#
# def date_of_loss(enterdate):
#     time.sleep(10)
#     wait_and_find(properties.date_of_loss_textbox, 'XPATH').click()
#     wait_and_find(properties.date_of_loss_textbox, 'XPATH').send_keys(enterdate)
#
#
# def complex_dropdown():
#     wait_and_find(properties.complex_dropdown, 'XPATH').click()
#     time.sleep(5)
#     wait_and_find(properties.select_complex_in_dropdown, 'XPATH').click()
#
#
# def description_of_loss(loss):
#     wait_and_find(properties.description_of_loss_textbox, 'XPATH').send_keys(loss)
#
#
# def select_policy():
#     wait_and_find(properties.select_policies_checkbox, 'XPATH').click()
#
#
# def continue_button():
#     wait_and_find(properties.continue_button, 'XPATH').click()
#
#
# def claimant_name(claimant):
#     wait_and_find(properties.claimant_name, 'XPATH').send_keys(claimant)
#
#
# def claimant_continue_button():
#     wait_and_find(properties.claimant_continue_button, 'XPATH').click()
#
#
# # def select_claim_type()
# # wait_and_find(properties.client_name_textbox, 'XPATH').click()
# # wait_and_find(properties.select_claim_type, 'XPATH').select_by_value(3)
# # selects = Select(wait_and_find).select_by_index(3)
#
# # wait_and_find(properties.continue_button, 'XPATH').click()
#
#
# def review_slidertab():
#     wait_and_find(properties.review_slider_tab, 'XPATH').click()
#
#
# def CCM_review_checkbox():
#     wait_and_find(properties.CCM_reference_check, 'XPATH').click()
#
#
# def review_description_textbox(text):
#     wait_and_find(properties.review_description_textbox, 'XPATH').send_keys(text)
#
#
# def review_submit_button():
#     wait_and_find(properties.submit_review_button, 'XPATH').click()
#
#
# def send_mail_slider():
#     wait_and_find(properties.send_email_slider_tab, 'XPATH').click()
#
#
# def notify_insurer_checkbox():
#     handles = web_driver.window_handles
#     web_driver.switch_to.window(handles[1])
#
#     wait_and_find(properties.notify_insurer_checkbox, 'XPATH').click()
#
#
# def send_close_mail_button():
#     wait_and_find(properties.send_close_button, 'XPATH').click()
#
# def claim_summary_checkbox():
#     wait_and_find(properties.claim_summary_pdf_checkbox, 'XPATH').click()
#
# # def claim_summary_popup():
# #     handles = web_driver.window_handles
# #     web_driver.switch_to.window(handles[1])
# #
# #     wait_and_find(properties.claim_summary_popup, 'XPATH').click()
def wait_find(element, locator):
    try:
        if locator == 'ID':
            waitElement = WebDriverWait(web_driver, 30).until(
                EC.text_to_be_present_in_element((By.ID, element)))
        elif locator == 'XPATH':
            waitElement = WebDriverWait(web_driver, 30).until(
                EC.text_to_be_present_in_element((By.XPATH, element)))
        elif locator == 'CSS':
            WebDriverWait(web_driver, 30).until(
                EC.text_to_be_present_in_element((By.CSS_SELECTOR, element)))

    except:
        print("No element present for the locator " + element)

    return waitElement


def pop_up_button():
    handles = web_driver.window_handles
    web_driver.switch_to.window(handles[1])
    wait_and_find(properties.pop_up_button, 'XPATH').click()


def welcome_page():
    return bool(wait_and_find(properties.welcome_page, 'XPATH').is_selected())
    # welcome=wait_and_find(properties.welcome_page, 'XPATH').text
    # return welcome


def save_and_add_button():
    wait_and_find(properties.save_and_add_button, 'XPATH').click()


def scroll_up():
    time.sleep(60)
    web_driver.execute_script('window.scrollTo(0,200)')


def policy_number(username):
    wait_and_find(properties.policy_number_textbox, 'XPATH').send_keys(username)


def plan_name(username):
    wait_and_find(properties.plan_name_textbox, 'XPATH').send_keys(username)


# def document_category():
#     wait_and_find(properties.document_category,'XPATH').click()

def select_document_category():
    wait_and_find(properties.document_category, 'XPATH').click()
    time.sleep(5)
    wait_and_find(properties.select_value_document_category, 'XPATH').click()


# def secondary_document_category():
#     wait_and_find(properties.secondary_document_category,'XPATH').click()

def select_secondary_document():
    wait_and_find(properties.secondary_document_category, 'XPATH').click()
    time.sleep(5)
    wait_and_find(properties.select_value_secondary_doc, 'XPATH').click()


# def generic_document():
#     wait_and_find(properties.generic_document_name,'XPATH').click()
def select_generic_document():
    wait_and_find(properties.generic_document_name, 'XPATH').click()
    time.sleep(5)
    wait_and_find(properties.select_generic_document, 'XPATH').click()


# def business_level():
#     wait_and_find(properties.business_level,'XPATH').click()


def select_business_level():
    wait_and_find(properties.business_level, 'XPATH').click()
    time.sleep(5)
    wait_and_find(properties.select_business_level, 'XPATH').click()


def select_carrier():
    wait_and_find(properties.carrier, 'XPATH').click()
    time.sleep(5)
    wait_and_find(properties.select_carrier, 'XPATH').click()


def plan_ID(username):
    wait_and_find(properties.plan_id, 'XPATH').send_keys(username)


def plan_start_renewal_date():
    wait_and_find(properties.plan_start_date, 'XPATH').click()
    time.sleep(5)
    wait_and_find(properties.plan_start_year_click,'XPATH').click()
    time.sleep(5)
    wait_and_find(properties.select_plan_year,'XPATH').click()
    time.sleep(5)
    wait_and_find(properties.select_month,'XPATH').click()
    time.sleep(5)
    wait_and_find(properties.select_plan_date, 'XPATH').click()


def plan_status():
    wait_and_find(properties.plan_status, 'XPATH').click()
    time.sleep(5)
    wait_and_find(properties.select_plan_status, 'XPATH').click()


def issuing_location():
    wait_and_find(properties.issuing_location, 'XPATH').click()
    time.sleep(5)
    wait_and_find(properties.select_issuing_location, 'XPATH').click()


def commission(username):
    wait_and_find(properties.commission_textbox, 'XPATH').send_keys(username)


def tier():
    wait_and_find(properties.tier, 'XPATH').click()
    time.sleep(5)
    wait_and_find(properties.select_tier, 'XPATH').click()


def search_tags_text():
    search = wait_and_find(properties.search_tag, 'XPATH').text
    return search


def get_search_message(toast_value):
    return getattr(wait_and_find(toast_value), 'XPATH', 'text')
    # wait_and_find(properties.search_tag, 'XPATH').text


def selected(element, locator):
    if locator == 'ID':
        select = WebDriverWait(web_driver, 30).until(
            EC.element_to_be_selected((By.ID, element)))
    elif locator == 'XPATH':
        select = WebDriverWait(web_driver, 30).until(
            EC.element_to_be_selected((By.XPATH, element)))
    return select


def display_to_client():
    # # def is_checked(self, driver, item_id):
    #     checked = web_driver.execute_script(
    #         wait_and_find(properties.display_to_client).checked
    #
    #     )
    #     return checked
    return bool(wait_and_find(properties.display_to_client, 'XPATH').is_selected())

    # def checkbox_is_selected():
    #     web_driver.execute_script(
    #             wait_and_find(properties.display_to_client,'XPATH')).is_selected()
    #


def get_search_tag():
    return getattr(wait_and_find(properties.search_tag, 'XPATH'), 'text')


def region_selector(username):
    wait_and_find(properties.region_selector_textbox, 'XPATH').send_keys(username)


def class_selector(username):
    wait_and_find(properties.class_selector_textbox, 'XPATH').send_keys(username)




def is_checked(locator):
    try:
        selenium.should_be_checked(locator)
    except AssertionError:
        return False
    else:
        return True


def plan_summaries_dropdown():
    time.sleep(5)
    wait_and_find(properties.summary_dropdown, 'XPATH').click()


def plan_year_button():
    wait_and_find(properties.plan_year, 'XPATH').click()


def group_by():
    wait_and_find(properties.group_by_dropdown, 'XPATH').click()
    time.sleep(5)
    wait_and_find(properties.select_carrier_dropdown, 'XPATH').click()


def view_all_link_text():
    wait_and_find(properties.view_all_link_text, 'XPATH').click()


def select_existing_plan():
    time.sleep(5)
    wait_and_find(properties.select_existing_plan, 'XPATH').click()


def edit_plan_button():
    wait_and_find(properties.edit_plan_button, 'XPATH').click()


def edit_policy_number(username):
    wait_and_find(properties.edit_policy_number, 'XPATH').send_keys(username)


def update_button():
    wait_and_find(properties.update_plan_button, 'XPATH').click()


def close_browser():
    web_driver.quit()

def display_name_text():
    wait_and_find(properties.display_name_textbox, 'XPATH').click()
    time.sleep(10)

def display_name_message():
    display = wait_and_find(properties.display_name_textbox, 'XPATH').text
    return display
def get_display_message(toast_value):
    return getattr(wait_and_find(properties.display_name_textbox,toast_value), 'XPATH', 'text')


def amazon_dashboard():
    time.sleep(120)
    activity_name = is_selectByvisibletext(properties.amazon_dashboard, 'XPATH').tex
    return activity_name

def username_label():
    time.sleep(10)
    wait_and_find(properties.username_label,'XPATH').text
#!/usr/bin/env python3




import time
from datetime import date
from configparser import ConfigParser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

today = date.today()
today_date = str(today.month) + "/" + str(today.day) + "/" + str(today.year)
driver = webdriver.Firefox()

def exists(variable):
    try:
        eval(variable)
    except NameError:
        return False
    return True


config = ConfigParser()
config.read('config.ini')

Student_ID = config.get('main', 'Student_ID')
First_name = config.get('main', 'First_name')
Last_name = config.get('main', 'Last_name')
Grade = config.get('main', 'Grade')
url = config.get('main', 'url')

driver.get(url)


while not exists("elem_submit"):
    try:
        elem_submit = driver.find_element_by_css_selector("[aria-label='Submit']")
    except:
        print("bad, refresh")
        driver.refresh()
        time.sleep(5)

col = 0
while col < 2:
    elem_date_id_fn_ln = driver.find_elements_by_css_selector("[placeholder='Enter your answer']")
    col = elem_date_id_fn_ln.__len__()
    time.sleep(1)

elem_date = driver.find_element_by_css_selector("[placeholder='Please input date in format of M/d/yyyy']")

# elem_date_id_fn_ln = driver.find_elements_by_css_selector("[placeholder='Enter your answer']")

elem_id = driver.find_element_by_css_selector("[placeholder='The value must be a number']")
elem_first_name = elem_date_id_fn_ln[0]
elem_last_name = elem_date_id_fn_ln[1]

# elem_id = driver.find_element_by_css_selector("[aria-labelledby='question3-title question3-required question3-questiontype']")

# elem_first_name = driver.find_element_by_css_selector("[aria-labelledby='question4-title question4-required question4-questiontype']")

# elem_last_name = driver.find_element_by_css_selector("[aria-labelledby='question7-title question7-required question7-questiontype']")

elem_grade = driver.find_element_by_css_selector("[aria-label='Select your answer']")
elem_grade.click()

elem_grad_span = driver.find_elements_by_class_name("select-option-nocheck")
elem_grad_span[1].click()

elem_remote = driver.find_element_by_css_selector("[aria-label='Remote Learning Student']")

elem_confirm1 = driver.find_element_by_css_selector(
    "[aria-label='REQUIRED: I (or the student) is in attendance today']")

elem_confirm2 = driver.find_element_by_css_selector(
    "[aria-label='REQUIRED: I (or the student) is available via email and/or phone during regular school hours']")

elem_submit = driver.find_element_by_css_selector("[aria-label='Submit']")

elem_date.send_keys(today_date)
elem_id.send_keys(Student_ID)
elem_first_name.send_keys(First_name)
elem_last_name.send_keys(Last_name)
elem_grade.click()

elem_grad_span = driver.find_elements_by_class_name("select-option-nocheck")
elem_grad_span[1].click()
elem_remote.click()

elem_confirm1.click()
elem_confirm2.click()

#elem_submit.click()
#driver.quit()

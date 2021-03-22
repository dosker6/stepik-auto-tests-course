from selenium import webdriver
import time



def test_button(browser):
    link = 'http://selenium1py.pythonanywhere.com/es/catalogue/coders-at-work_207/'
    browser.get(link)
    assert browser.find_element_by_css_selector('.btn-add-to-basket')

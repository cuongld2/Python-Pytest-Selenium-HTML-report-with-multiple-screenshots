import sys
import traceback
from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.select import Select
import pytest


@pytest.fixture()
def browser_local():
    global driver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
    return

class TestBrowser:


    def test_teach(self, browser_local):
        Value = "Under 20"
        browser_local.get("http://www.teachmeselenium.com/automation-practice/")
        dropdown = Select(browser_local.find_element_by_name("age"))
        dropdown.select_by_value(Value)
        browser_local.close()
        test_driver = webdriver.Chrome()
        test_driver.get("https://www.vnexpress.net")
        test_driver.quit()

    def test_facebook(self,browser_local):
        Value = "Under 20"
        browser_local.get("http://www.facebook.com/")
        browser_local.close()
        test_driver = webdriver.Chrome()
        test_driver.get("https://www.coccoc.com")
        test_driver.quit()
        # browser.save_screenshot("Test2.png")


    def test_google(self,browser_local):
        Value = "Under 20"
        browser_local.get("http://www.google.com/")

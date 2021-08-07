import sys
import traceback
from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.select import Select
import pytest

class TestBrowser:

    def test_facebook(self,browser):
        browser.get("http://www.facebook.com/")
        assert 1==0
        # browser.save_screenshot("Test2.png")

    def test_google(self,browser):
        browser.get("http://www.google.com/")

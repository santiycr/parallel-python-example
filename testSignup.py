#! /usr/bin/env python
#-.- coding=utf8 -.-

from selenium import selenium
import unittest, time, re

class signup(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("saucelabs.com",
                                 4444,
                                 """{\
                                     "username": "your-username",\
                                     "access-key": "your-access-key",\
                                     "os": "Windows 2003",\
                                     "browser": "firefox",\
                                     "browser-version": ""\
                                 }""",
                                 "http://saucelabs.com/")
        self.selenium.start()
        self.selenium.set_timeout(90000)
    
    def test_empty_info(self):
        sel = self.selenium
        sel.open("/")
        sel.click("//input[@name='submit' and @value='Sign up']")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Sign up - Sauce Labs", sel.get_title())
        try: self.assertEqual("Please enter a value",
                              sel.get_text("//table[@class='signup']//tr[1]//*[@class='form-error']"))
        except AssertionError, e: self.verificationErrors.append("Email not required")
        try: self.assertEqual("Please enter a value",
                              sel.get_text("//table[@class='signup']//tr[2]//*[@class='form-error']"))
        except AssertionError, e: self.verificationErrors.append("Username not required")
        try: self.assertEqual("Please enter a value",
                              sel.get_text("//table[@class='signup']//tr[3]//*[@class='form-error']"))
        except AssertionError, e: self.verificationErrors.append("Password not required")
    
    def test_empty_email(self):
        sel = self.selenium
        sel.open("/signup")
        self.assertEqual("Sign up - Sauce Labs", sel.get_title())
        sel.type("username", "fake")
        sel.type("password", "fakepass")
        sel.click("submit")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Please enter a value",
                          sel.get_text("//table[@class='signup']//tr[1]//*[@class='form-error']"))
    
    def test_empty_user(self):
        sel = self.selenium
        sel.open("/signup")
        self.assertEqual("Sign up - Sauce Labs", sel.get_title())
        sel.type("email", "fake@fake.com")
        sel.type("password", "fakepass")
        sel.click("submit")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Please enter a value",
                          sel.get_text("//table[@class='signup']//tr[2]//*[@class='form-error']"))
    
    def test_empty_passwd(self):
        sel = self.selenium
        sel.open("/signup")
        self.assertEqual("Sign up - Sauce Labs", sel.get_title())
        sel.type("username", "fake")
        sel.type("email", "fake@fake.com")
        sel.click("submit")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Sign up - Sauce Labs", sel.get_title())
        self.assertEqual("Please enter a value",
                          sel.get_text("//table[@class='signup']//tr[3]//*[@class='form-error']"))
    
    def test_incorrect_email(self):
        sel = self.selenium
        sel.open("/signup")
        self.assertEqual("Sign up - Sauce Labs", sel.get_title())
        sel.type("username", "fake")
        sel.type("email", "a")
        sel.type("password", "fakepass")
        sel.click("submit")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Sign up - Sauce Labs", sel.get_title())
        self.assertEqual("An email address must contain a single @",
                          sel.get_text("//table[@class='signup']//tr[1]//*[@class='form-error']"))
        sel.type("username", "fake")
        sel.type("email", "fakefake.com")
        sel.type("password", "fakepass")
        sel.click("submit")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Sign up - Sauce Labs", sel.get_title())
        self.assertEqual("An email address must contain a single @",
                          sel.get_text("//table[@class='signup']//tr[1]//*[@class='form-error']"))
        sel.type("username", "fake")
        sel.type("email", "fake@@fake.com")
        sel.type("password", "fakepass")
        sel.click("submit")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Sign up - Sauce Labs", sel.get_title())
        self.assertEqual("The domain portion of the email address is invalid (the portion after the @: @fake.com)",
                          sel.get_text("//table[@class='signup']//tr[1]//*[@class='form-error']"))
        sel.type("username", "fake")
        sel.type("email", "fake@fakecom")
        sel.type("password", "fakepass")
        sel.click("submit")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Sign up - Sauce Labs", sel.get_title())
        self.assertEqual("The domain portion of the email address is invalid (the portion after the @: fakecom)",
                          sel.get_text("//table[@class='signup']//tr[1]//*[@class='form-error']"))
    
    def test_incorrect_user(self):
        sel = self.selenium
        sel.open("/signup")
        self.assertEqual("Sign up - Sauce Labs", sel.get_title())
        sel.type("username", "a")
        sel.type("email", "fake@fake.com")
        sel.type("password", "fakepass")
        sel.click("submit")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Sign up - Sauce Labs", sel.get_title())
        self.assertEqual("Enter a value at least 4 characters long",
                          sel.get_text("//table[@class='signup']//tr[2]//*[@class='form-error']"))
    
    def test_incorrect_passwd(self):
        sel = self.selenium
        sel.open("/signup")
        self.assertEqual("Sign up - Sauce Labs", sel.get_title())
        sel.type("username", "fake")
        sel.type("email", "fake@fake.com")
        sel.type("password", "a")
        sel.click("submit")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Sign up - Sauce Labs", sel.get_title())
        self.assertEqual("Enter a value at least 6 characters long",
                          sel.get_text("//table[@class='signup']//tr[3]//*[@class='form-error']"))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

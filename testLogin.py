#! /usr/bin/env python
#-.- coding=utf8 -.-

from selenium import selenium
import unittest, time, re

class login(unittest.TestCase):
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
        sel.click("css=.inline-login input[name=submit][type=submit]")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Login - Sauce Labs", sel.get_title())
        try: self.assertEqual("Incorrect username or password", sel.get_text("css=.error-box"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=.login input[name=username]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=.login input[name=password][type=password]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=.login input[name=submit][type=submit]"))
        except AssertionError, e: self.verificationErrors.append(str(e))

    def test_no_passwd(self):
        sel = self.selenium
        sel.open("/login")
        sel.type("username", "fake")
        sel.click("submit")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Login - Sauce Labs", sel.get_title())
        try: self.assertEqual("Incorrect username or password", sel.get_text("css=.error-box"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=.login input[name=username]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=.login input[name=password][type=password]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=.login input[name=submit][type=submit]"))
        except AssertionError, e: self.verificationErrors.append(str(e))

    def test_no_user(self):
        sel = self.selenium
        sel.open("/login")
        sel.type("password", "fake")
        sel.click("submit")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Login - Sauce Labs", sel.get_title())
        try: self.assertEqual("Incorrect username or password", sel.get_text("css=.error-box"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=.login input[name=username]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=.login input[name=password][type=password]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=.login input[name=submit][type=submit]"))
        except AssertionError, e: self.verificationErrors.append(str(e))

    def test_no_user(self):
        sel = self.selenium
        sel.open("/login")
        sel.type("username", "fake")
        sel.type("password", "fake")
        sel.click("submit")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Login - Sauce Labs", sel.get_title())
        try: self.assertEqual("Incorrect username or password", sel.get_text("css=.error-box"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=.login input[name=username]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=.login input[name=password][type=password]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=.login input[name=submit][type=submit]"))
        except AssertionError, e: self.verificationErrors.append(str(e))

    def test_valid_account(self):
        sel = self.selenium
        sel.open("/login")
        sel.type("username", "demo")
        sel.type("password", "demopass")
        sel.click("submit")
        sel.wait_for_page_to_load("30000")
        self.assertEqual("Account Info - Sauce Labs", sel.get_title())
        try: self.failIf(sel.is_element_present("css=.error-box"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//div[@id='main']/center/table[1]/tbody/tr/td[2]/nobr/span/b")
        try: self.assertEqual("demo", sel.get_text("css=.menu b"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

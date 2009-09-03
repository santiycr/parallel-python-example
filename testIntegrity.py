#! /usr/bin/env python
#-.- coding=utf8 -.-

from selenium import selenium
import unittest, time, re

class integrity(unittest.TestCase):
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
    
    def test_integrity(self):
        sel = self.selenium
        sel.open("/")
        # Verify basic text
        self.assertEqual("Sauce Labs", sel.get_title())
        try: self.failUnless(sel.is_text_present("Web Browsers as a Service"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present("Getting started is easy."))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_text_present(u"Copyright © 2009 Sauce Labs Inc. All rights reserved."))
        except AssertionError, e: self.verificationErrors.append(str(e))
        # Links
        try: self.failUnless(sel.is_element_present("link=Blog"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=Terms of Service"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=Privacy Notice"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=Contact"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=Follow Sauce Labs on Twitter!"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=Selenium"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("link=Learn more..."))
        except AssertionError, e: self.verificationErrors.append(str(e))
        # Login form
        try: self.failUnless(sel.is_element_present("css=.inline-login input[name=username]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=.inline-login input[name=password][type=password]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=.inline-login input[name=submit][type=submit]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        # Signup form
        try: self.failUnless(sel.is_element_present("css=.signup input[name=email]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=.signup input[name=username]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=.signup input[name=password][type=password]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        try: self.failUnless(sel.is_element_present("css=.signup input[name=submit][type=submit]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        # Feedback tab
        try: self.failUnless(sel.is_element_present("uservoice-feedback-tab"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

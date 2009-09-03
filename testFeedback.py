#! /usr/bin/env python
#-.- coding=utf8 -.-

from selenium import selenium
import unittest, time, re

class feedback(unittest.TestCase):
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
    
    def test_feedback_frame(self):
        sel = self.selenium
        sel.open("/")
        self.assertEqual("Sauce Labs", sel.get_title())
        self.failUnless(sel.is_element_present("uservoice-feedback-tab"))
        sel.click("uservoice-feedback-tab")
        for i in range(60):
            try:
                if sel.is_element_present("css=#uservoice-dialog-content"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if sel.is_element_present("css=#suggestions"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Submit an Idea", sel.get_text("css=#suggestions h1"))
        except AssertionError, e: self.verificationErrors.append("Wrong feedback title")
        try: self.failUnless(sel.is_element_present(u"link=» Go to our Feedback Forum (?? ideas)"))
        except AssertionError, e: self.verificationErrors.append("Feedback link not present")
        try: self.failUnless(sel.is_element_present("link=Report a Bug"))
        except AssertionError, e: self.verificationErrors.append("Bug report link not present")
        try: self.failUnless(re.search(r"^Have a Bug\? Report a Bug$", sel.get_text("css=h6.switch")))
        except AssertionError, e: self.verificationErrors.append("Bug report text not present")
     
    def test_feedback_redirection(self):
        sel = self.selenium
        sel.open("/")
        self.assertEqual("Sauce Labs", sel.get_title())
        self.failUnless(sel.is_element_present("uservoice-feedback-tab"))
        sel.click("uservoice-feedback-tab")
        for i in range(60):
            try:
                if sel.is_element_present("css=#suggestions"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        self.failUnless(re.search(r"^http://feedback\.saucelabs\.com/[\s\S]*$",
                        sel.get_attribute(u"link=» Go to our Feedback Forum (?? ideas)@href")))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

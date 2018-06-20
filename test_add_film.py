# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_add_film(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_add_film(self):
        success = True
        wd = self.wd
        wd.get("http://10.130.139.119/")
        if not wd.find_element_by_xpath("//input").is_selected():
            wd.find_element_by_xpath("//input").click()
        if not wd.find_element_by_xpath("//input").is_selected():
            wd.find_element_by_xpath("//input").click()
        wd.find_element_by_id("ember444").click()
        wd.find_element_by_id("ember444").clear()
        wd.find_element_by_id("ember444").send_keys("root")
        wd.find_element_by_xpath("//div[@id='content']//button[.='Войти']").click()
        wd.find_element_by_id("ember453").click()
        wd.find_element_by_id("ember453").clear()
        wd.find_element_by_id("ember453").send_keys("123")
        wd.find_element_by_xpath("//div[@id='content']//button[.='Войти']").click()
        wd.find_element_by_id("ember696").click()
        wd.find_element_by_id("ember990").click()
        wd.find_element_by_id("filmname").click()
        wd.find_element_by_id("filmname").clear()
        wd.find_element_by_id("filmname").send_keys("12323123")
        wd.find_element_by_id("filmyear").click()
        wd.find_element_by_id("filmyear").clear()
        wd.find_element_by_id("filmyear").send_keys("2020")
        wd.find_element_by_id("filmcountry").click()
        wd.find_element_by_id("filmcountry").clear()
        wd.find_element_by_id("filmcountry").send_keys("12323")
        wd.find_element_by_id("filmduration").click()
        wd.find_element_by_id("filmduration").send_keys("\\undefined")
        wd.find_element_by_id("filmduration").click()
        wd.find_element_by_id("filmduration").clear()
        wd.find_element_by_id("filmduration").send_keys("3")
        wd.find_element_by_id("filmduration").click()
        wd.find_element_by_id("filmduration").clear()
        wd.find_element_by_id("filmduration").send_keys("4")
        wd.find_element_by_id("filmcountry").click()
        wd.find_element_by_id("filmcountry").send_keys("\\undefined")
        wd.find_element_by_id("ember-power-select-trigger-multiple-input-ember1297").click()
        wd.find_element_by_xpath("//ul[@id='ember-power-select-options-ember1297']/li[2]").click()
        wd.find_element_by_xpath("//ul[@id='ember-power-select-options-ember1297']/li[3]").click()
        wd.find_element_by_xpath("//ul[@id='ember-power-select-options-ember1297']/li[6]").click()
        if not wd.find_element_by_id("nolimit").is_selected():
            wd.find_element_by_id("nolimit").click()
        wd.find_element_by_xpath("//form[@id='ember1085']//button[.='Сохранить']").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

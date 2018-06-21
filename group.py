# -*- coding: utf-8 -*-

from selenium import webdriver
driver = webdriver.Chrome(executable_path='D:\Git\my_first_test\env\Scripts\chromedriver.exe')

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
        self.wd = webdriver.Chrome('D:\Git\my_first_test\env\Scripts\chromedriver.exe')
        self.wd.implicitly_wait(60)

    def test_test_add_film(self):
        success = True
        wd = self.wd
        wd.get("http://10.130.139.119/")
        if not wd.find_element_by_xpath("//input").is_selected():
            wd.find_element_by_xpath("//input").click()
        if not wd.find_element_by_xpath("//input").is_selected():
            wd.find_element_by_xpath("//input").click()

        self.athorization(wd)
        wd.find_element_by_xpath("//a[@href='/movies']").click()
        wd.find_element_by_xpath("//a[@href='/movie/add']").click()
        wd.find_element_by_id("filmname").click()
        wd.find_element_by_id("filmname").clear()
        wd.find_element_by_id("filmname").send_keys("1movie1")
        wd.find_element_by_id("filmyear").click()
        wd.find_element_by_id("filmyear").clear()
        wd.find_element_by_id("filmyear").send_keys("2009")
        wd.find_element_by_xpath("//div[@class='ember-power-select-trigger ember-power-select-multiple-trigger@']").click()
        wd.find_element_by_xpath("//li[@data-selected-index='5']").click()
        wd.find_element_by_xpath("//li[@data-selected-index='4']").click()

        ##if not wd.find_element_by_id("nolimit").is_selected():
        ##    wd.find_element_by_id("nolimit").click()
        wd.find_element_by_xpath("//form[@id='ember1085']//button[.='Сохранить']").click()
        self.assertTrue(success)

    def athorization(self, wd):
        wd.find_element_by_id("ember444").click()
        wd.find_element_by_id("ember444").clear()
        wd.find_element_by_id("ember444").send_keys("root")
        wd.find_element_by_xpath("//div[@id='content']//button[.='Войти']").click()
        wd.find_element_by_id("ember453").click()
        wd.find_element_by_id("ember453").clear()
        wd.find_element_by_id("ember453").send_keys("123")
        wd.find_element_by_xpath("//div[@id='content']//button[.='Войти']").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

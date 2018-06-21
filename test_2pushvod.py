# -*- coding: utf-8 -*-


from selenium import webdriver


from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class (unittest.TestCase):
    def setUp(self):
        self.wd = webdriver('D:\Git\my_first_test\env\Scripts\chromedriver.exe')
        self.wd.implicitly_wait(60)
    
    def test_(self):
        success = True
        wd = self.wd
        wd.get("http://10.130.139.119/login")
        if not wd.find_element_by_xpath("//input").is_selected():
            wd.find_element_by_xpath("//input").click()
        if not wd.find_element_by_xpath("//input").is_selected():
            wd.find_element_by_xpath("//input").click()
        wd.find_element_by_id("ember441").click()
        wd.find_element_by_id("ember441").clear()
        wd.find_element_by_id("ember441").send_keys("root")
        wd.find_element_by_id("ember450").click()
        wd.find_element_by_id("ember450").clear()
        wd.find_element_by_id("ember450").send_keys("123")
        wd.find_element_by_css_selector("div.panel-body.login-panel_body").click()
        wd.find_element_by_xpath("//div[@id='content']//button[.='Войти']").click()
        self.new_movie_create(success, wd)

    def new_movie_create(self, success, wd, mov_name="1movies", year="2010", country="STRANA", duration_min="503",
                         description="Opisanie", director="person1", scriptwriter="person2", cast="person3"):
        wd.find_element_by_id("ember693").click()
        wd.find_element_by_id("ember987").click()
        wd.find_element_by_id("filmname").click()
        wd.find_element_by_id("filmname").clear()
        wd.find_element_by_id("filmname").send_keys("%s" % mov_name)
        wd.find_element_by_id("filmyear").click()
        wd.find_element_by_id("filmyear").clear()
        wd.find_element_by_id("filmyear").send_keys("%s" % year)
        wd.find_element_by_id("filmcountry").click()
        wd.find_element_by_id("filmcountry").clear()
        wd.find_element_by_id("filmcountry").send_keys("%s" % country)
        wd.find_element_by_id("filmduration").click()
        wd.find_element_by_id("filmduration").click()
        wd.find_element_by_id("filmduration").clear()
        wd.find_element_by_id("filmduration").send_keys("%s" % duration_min)
        wd.find_element_by_id("filmdescription").click()
        wd.find_element_by_id("filmdescription").clear()
        wd.find_element_by_id("filmdescription").send_keys("%s" % description)
        wd.find_element_by_id("filmdirector").click()
        wd.find_element_by_id("filmdirector").clear()
        wd.find_element_by_id("filmdirector").send_keys("%s" % director)
        wd.find_element_by_id("filmwriter").click()
        wd.find_element_by_id("filmwriter").clear()
        wd.find_element_by_id("filmwriter").send_keys("%s" % scriptwriter)
        wd.find_element_by_id("filmcast").click()
        wd.find_element_by_id("filmcast").clear()
        wd.find_element_by_id("filmcast").send_keys("%s" % cast)
        wd.find_element_by_id("ember-power-select-trigger-multiple-input-ember1316").click()
        wd.find_element_by_xpath("//ul[@id='ember-power-select-options-ember1316']/li[2]").click()
        wd.find_element_by_xpath("//ul[@id='ember-power-select-options-ember1316']/li[3]").click()
        wd.find_element_by_xpath("//ul[@id='ember-power-select-options-ember1316']/li[4]").click()
        wd.find_element_by_xpath("//ul[@id='ember-power-select-options-ember1316']/li[5]").click()
        wd.find_element_by_xpath("//form[@id='ember1104']/div[1]/div[1]/div[2]/div").click()
        wd.find_element_by_xpath("//form[@id='ember1104']//button[.='Сохранить']").click()
        self.assertTrue(success)

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

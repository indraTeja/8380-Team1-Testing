import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TC001_ByzantiumLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # open https://byzantium-final.herokuapp.com and navigate to Login
    def test_1_login(self):
        #test passwords
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://byzantium-final.herokuapp.com/")
        time.sleep(2)

        elem = driver.find_element_by_xpath("/html/body/nav/nav[2]/div/div/ul[1]/li[3]/a")
        elem.click()
        time.sleep(5)

        # Login Test scripts go
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(3)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        #elem = driver.find_element_by_xpath("/html/body/nav/nav[2]/div/div/ul[1]/li[5]/a").click()

        def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
    unittest.main()

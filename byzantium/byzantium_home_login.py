import time
import unittest
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # open https://byzantium-travel.herokuapp.com and navigate to Login
    def test_blog(self):
        #test passwords
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://byzantium-travel.herokuapp.com/home/")
        time.sleep(1)

        elem = driver.find_element_by_xpath("/html/body/nav/nav[2]/div/div/ul[1]/li[4]/a").click()
        time.sleep(5)

        # Login Test scripts go
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)




        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/nav/nav[2]/div/div/ul[1]/li[5]/a").click()
        time.sleep(5)


        def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
    unittest.main()

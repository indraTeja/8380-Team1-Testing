import time
import unittest
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # open https://byzantium-travel.herokuapp.com and navigate to Features
    def test_blog(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://byzantium-travel.herokuapp.com/home/")
        time.sleep(1)

        #open Read More
        elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/button").click()
        time.sleep(1)


        driver.get("https://byzantium-travel.herokuapp.com/home/#Features")
        time.sleep(2)


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
        unittest.main()
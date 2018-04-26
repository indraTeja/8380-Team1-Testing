import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ByzantiumLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    # open https://byzantium-final.herokuapp.com and navigate to Features
    def test_facebook(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://byzantium-final.herokuapp.com/")
        time.sleep(2)

        elem = driver.find_element_by_xpath("/html/body/nav/nav[2]/div/div/ul[1]/li[3]/a")
        elem.click()
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div/div[2]/a/input")
        elem.click()
        
        driver.get("https://byzantium-travel.herokuapp.com/home/#Features")
        time.sleep(10)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
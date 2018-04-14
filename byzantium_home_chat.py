import time
import unittest
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


   # open https://byzantium-travel.herokuapp.com and open chat
    def test_blog(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://byzantium-travel.herokuapp.com/home/")
        time.sleep(1)

        elem = driver.find_element_by_xpath("/html/body/nav/nav[2]/div/div/ul[1]/li[3]/a").click()
        time.sleep(2)
        #elem = driver.find_element_by_id("chat-input")
        #elem.send_keys("This is a test post of text")

        inputElement = driver.find_element_by_id("chat-input")
        inputElement.send_keys('This is a test post of text')
        time.sleep(2)


        inputElement.send_keys(Keys.ENTER)
        time.sleep(5)
        #assert "Post SMS"

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()
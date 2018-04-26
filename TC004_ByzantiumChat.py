import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TC004_ByzantiumChat(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


   # open https://byzantium-final.herokuapp.com and open chat
    def test_4_chat(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://byzantium-final.herokuapp.com/")
        time.sleep(2)

        elem = driver.find_element_by_xpath("/html/body/nav/nav[2]/div/div/ul[1]/li[3]/a")
        elem.click()
        time.sleep(3)

        # Login Test scripts go
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(3)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)

        # TWILIO CHAT API
        inputElement = driver.find_element_by_id("chat-input")
        inputElement.send_keys('Hello Dr. Royce')
        inputElement.send_keys(Keys.ENTER)
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
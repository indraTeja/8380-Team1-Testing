import time
import unittest
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


   # open https://byzantium-final.herokuapp.com and open chat
    def test_planner(self):
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
        #elem = driver.find_element_by_id("chat-input")
        #elem.send_keys("This is a test post of text")

        #startPlanning

        #select type of trip
        elem = driver.find_element_by_id("jb-glry-id-0_thumb_1")
        elem.click()
        time.sleep(4)
        elem = driver.find_element_by_id("selector")
        elem.click()
        time.sleep(3)

        #pass origin, FLIGHT API
        elem = driver.find_element_by_id("origin")
        elem.send_keys("OMA")
        time.sleep(4)
        elem = driver.find_element_by_id("startdate")
        elem.send_keys("2018-05-25")
        time.sleep(4)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/form/div[4]/input")
        elem.click()
        time.sleep(3)


        #hotels API
        # elem = driver.find_element_by_id("check_in")
        # elem.send_keys("2018-05-20")
        # time.sleep(3)
        # elem = driver.find_element_by_id("check_out")
        # elem.send_keys("2018-05-25")
        # time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div/form/div[4]/input")
        elem.click()
        time.sleep(3)


        #zomato API restaurants
        elem = driver.find_element_by_id("keyword")
        elem.send_keys("Italian")
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div/div/form/div[4]/input")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_id("keyword")
        elem.send_keys("Japanese")
        time.sleep(3)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[4]/div/div/div/form/div[4]/input")
        elem.click()
        time.sleep(2)


        # TWILIO SMS API
        elem = driver.find_element_by_id("to_number")
        elem.send_keys("+14026861203")
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[3]/div[5]/div/div/div/div/form/div[3]/input")
        elem.click()
        time(2)

        #TWILIO CHAT API
        inputElement = driver.find_element_by_id("chat-input")
        inputElement.send_keys('Hello Dr. Royce')
        inputElement.send_keys('This is our Final Demo!')
        inputElement.send_keys('Please check out our APIs!')
        inputElement.send_keys(Keys.ENTER)
        time.sleep(5)
        #assert "Post SMS"

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()
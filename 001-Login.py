#Author : Deepika
#Final Test Demo


import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class TC001_Hospital_CRUD(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_crud_hospital(self):
       user = "instructor"
       pwd = "instructor1a"

       driver = self.driver
       driver.maximize_window()


       driver.get("https://byzantium-travel.herokuapp.com/")
       time.sleep(2)


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
    unittest.main()

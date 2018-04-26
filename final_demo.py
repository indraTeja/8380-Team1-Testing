import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv
from TC001_ByzantiumLogin import *
from TC002_ByzantiumFacebook import *
from TC003_ByzantiumPlanner import *
from TC004_ByzantiumChat import *

class ConfigTestCase(unittest.TestCase):
    def setUp(self):
        print('set up')

    def runTest(self):
        print('run test')
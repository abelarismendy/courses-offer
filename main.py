import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from tkinter import messagebox, simpledialog
import json
import re
import os
import shutil
from sys import platform

if platform == "linux" or platform == "linux2":
    chrome_path = './drivers/chromedriver'

elif platform == "darwin":
    chrome_path = './drivers/chromedriver_mac'

options = Options()
options.add_argument('user-data-dir=/tmp/tarun')

class ObtainInfo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=chrome_path, options=options)
        self.driver.maximize_window()
        self.driver.get('https://ofertadecursos.uniandes.edu.co/')
        self.driver.implicitly_wait(10)
    def test_main(self):
        # wait 10 seconds before closing the browser
        self.driver.implicitly_wait(10)

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output='reportes', report_name='reporte_prueba'))
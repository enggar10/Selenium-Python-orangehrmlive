#from dbm.ndbm import library
import dbm
import unittest
import time
from urllib import response
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#variable
url="https://opensource-demo.orangehrmlive.com/"
username="Admin"
password="admin123"
username1="test123"
passw="Test_1234"

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    #test case pertama
    def test_success_login(self):

        driver = self.driver
        driver.get(url) # buka situs
        time.sleep(3)
        driver.find_element(By.NAME,"txtUsername").send_keys(username) # isi username
        time.sleep(1)
        driver.find_element(By.NAME,"txtPassword").send_keys(password) # isi password
        time.sleep(5)
        driver.find_element(By.NAME,"Submit").click()
        time.sleep(5)

        driver.find_element(By.ID,"menu_admin_viewAdminModule").click()
        time.sleep(5)
        driver.find_element(By.NAME,"btnAdd").click()
        time.sleep(5)

        select_element = driver.find_element(By.NAME,"systemUser[userType]") #select dropdown
        select_object = Select (select_element)
        select_object.select_by_value('1')
        time.sleep(5)

        driver.execute_script("document.getElementById('systemUser_employeeName_empName').focus()") #set fokus autocomplete
        driver.find_element(By.NAME,"systemUser[employeeName][empName]").send_keys('a') #insert value
        time.sleep(5)
        driver.execute_script("document.getElementsByClassName('ac_even')[0].click()") #select value autocomplete
        time.sleep(5)

        driver.find_element(By.NAME,"systemUser[userName]").send_keys(username1) 
        time.sleep(2)

        select_element = driver.find_element(By.NAME,"systemUser[status]") #select dropdown
        select_object = Select (select_element)
        select_object.select_by_value('1')
        time.sleep(5)

        driver.find_element(By.NAME,"systemUser[password]").send_keys(passw)
        time.sleep(2)
        driver.find_element(By.NAME,"systemUser[confirmPassword]").send_keys(passw)
        time.sleep(2)
        
        driver.find_element(By.NAME,"btnSave").click()
        time.sleep(5)

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()   
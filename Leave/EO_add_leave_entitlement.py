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
from selenium.webdriver.common.action_chains import ActionChains

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#variable
url="https://opensource-demo.orangehrmlive.com/"
username="Admin"
password="admin123"
enti="10"

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

        self.driver.implicitly_wait(0.5)
        a = ActionChains(self.driver)
        m = driver.find_element(By.ID,"menu_leave_viewLeaveModule")
        a.move_to_element(m).perform()
        #identify sub menu element
        n = driver.find_element(By.ID,"menu_leave_Entitlements")
        a.move_to_element(n).perform()
        o = driver.find_element(By.ID,"menu_leave_addLeaveEntitlement")
        #hover over element and click
        a.move_to_element(o).click().perform()
        time.sleep(2)

        #driver.find_element(By.NAME,"entitlements[filters][bulk_assign]").click()
        #time.sleep(5)

       # select_element = driver.find_element(By.NAME,"entitlements[filters][location]") #select dropdown
       #cselect_object = Select (select_element)
       # select_object.select_by_value('-1')
       # time.sleep(5)

       # select_element = driver.find_element(By.NAME,"entitlements[filters][subunit]") #select dropdown
       # select_object = Select (select_element)
       # select_object.select_by_value('0')
       # time.sleep(5)

        driver.execute_script("document.getElementById('entitlements_employee_empName').focus()") #set fokus autocomplete
        driver.find_element(By.NAME,"entitlements[employee][empName]").send_keys('a') #insert value
        time.sleep(5)
        driver.execute_script("document.getElementsByClassName('ac_even')[0].click()") #select value autocomplete
        time.sleep(5)


        select_element = driver.find_element(By.NAME,"entitlements[leave_type]") #select dropdown
        select_object = Select (select_element)
        select_object.select_by_value('9')
        time.sleep(5)

        select_element = driver.find_element(By.ID,"period") #select dropdown
        select_object = Select (select_element)
        select_object.select_by_value('2021-01-01$$2021-12-31')
        time.sleep(5)
        
        driver.find_element(By.NAME,"entitlements[entitlement]").send_keys(enti)
        time.sleep(2)
        
        driver.find_element(By.NAME,"btnSave").click()
        time.sleep(5)

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()   

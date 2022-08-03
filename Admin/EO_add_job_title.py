#from dbm.ndbm import library
import dbm
from tarfile import PAX_NAME_FIELDS
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
        
        n = driver.find_element(By.ID,"menu_leave_viewMyLeaveList")
        a.move_to_element(n).click().perform()
       
        time.sleep(2)

        d=driver.find_element(By.ID,"calFromDate").click()
        time.sleep(5)
        
        #driver.switch_to.frame(d);
        #identify element inside frame
        d= driver.find_element(By.ID,"ui-datepicker-div")
        d.click()
        time.sleep(10)
        #identify list of all dates

        print('look')

        time.sleep(1)

        d=driver.find_element(By.ID,"calToDate").click()
        time.sleep(5)

        print('from')


       # driver.switch_to.frame(d);
        #identify element inside frame
        d= driver.find_element(By.ID,"ui-datepicker-div")
        d.click()
        print('to date')
        time.sleep(1)

        #driver.find_element(By.ID,"leaveList_chkSearchFilter_checkboxgroup_allcheck").click()
        #time.sleep(1)
        
        driver.find_element(By.ID,"btnSearch").click()
        time.sleep(3)
        
         

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()   

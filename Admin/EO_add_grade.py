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
name="graduate"

#driver = webdriver.Chrome(executable_path="C:\Users\Enggar\python\chromedriver.exe")


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
        m = driver.find_element(By.ID,"menu_admin_viewAdminModule")
        a.move_to_element(m).perform()
        #identify sub menu element
        n = driver.find_element(By.ID,"menu_admin_Job")
        a.move_to_element(n).perform()
        o = driver.find_element(By.ID,"menu_admin_viewPayGrades")
        #hover over element and click
        a.move_to_element(o).click().perform()

        driver.find_element(By.NAME,"btnAdd").click()
        time.sleep(3)


        driver.find_element(By.NAME,"payGrade[name]").send_keys(name)
        time.sleep(1)
        driver.find_element(By.NAME,"btnSave").click()
        time.sleep(5)
         

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()   
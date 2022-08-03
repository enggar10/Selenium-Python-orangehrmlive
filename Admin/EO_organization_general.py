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

orname ="END Terrorism"
tax="qwetyu"
regnum="10"
phon="110110110"
email="end.terrorism@terrorist.com"
fax="10547658"
addres1="night square"
addres2="night round"
city = "OndonCity"
state="NY"
zip="32445"
note="isilah"



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
        n = driver.find_element(By.ID,"menu_admin_Organization")
        a.move_to_element(n).perform()
        o = driver.find_element(By.ID,"menu_admin_viewOrganizationGeneralInformation")
        #hover over element and click
        a.move_to_element(o).click().perform()
        time.sleep(2)

        driver.find_element(By.NAME,"btnSaveGenInfo").click()
        time.sleep(3)

        driver.find_element(By.NAME,"organization[name]").clear()
        time.sleep(2)
        driver.find_element(By.NAME,"organization[name]").send_keys(orname)
        time.sleep(2)
        driver.find_element(By.NAME,"organization[taxId]").clear()
        time.sleep(2)
        driver.find_element(By.NAME,"organization[taxId]").send_keys(tax)
        time.sleep(1)
        driver.find_element(By.NAME,"organization[registraionNumber]").clear()
        time.sleep(2)
        driver.find_element(By.NAME,"organization[registraionNumber]").send_keys(regnum)
        time.sleep(1)
        driver.find_element(By.NAME,"organization[phone]").clear()
        time.sleep(2)
        driver.find_element(By.NAME,"organization[phone]").send_keys(phon)
        time.sleep(1)
        driver.find_element(By.NAME,"organization[email]").clear()
        time.sleep(2)
        driver.find_element(By.NAME,"organization[email]").send_keys(email)
        time.sleep(1)
        driver.find_element(By.NAME,"organization[fax]").clear()
        time.sleep(2)
        driver.find_element(By.NAME,"organization[fax]").send_keys(fax)
        time.sleep(1)
        driver.find_element(By.NAME,"organization[street1]").clear()
        time.sleep(2)
        driver.find_element(By.NAME,"organization[street1]").send_keys(addres1)
        time.sleep(1)
        driver.find_element(By.NAME,"organization[street2]").clear()
        time.sleep(2)
        driver.find_element(By.NAME,"organization[street2]").send_keys(addres2)
        time.sleep(1)
        driver.find_element(By.NAME,"organization[city]").clear()
        time.sleep(2)
        driver.find_element(By.NAME,"organization[city]").send_keys(city)
        time.sleep(1)
        driver.find_element(By.NAME,"organization[province]").clear()
        time.sleep(2)
        driver.find_element(By.NAME,"organization[province]").send_keys(state)
        time.sleep(1)
        driver.find_element(By.NAME,"organization[zipCode]").clear()
        time.sleep(2)
        driver.find_element(By.NAME,"organization[zipCode]").send_keys(zip)
        time.sleep(1)

    
        select_element = driver.find_element(By.NAME,"organization[country]") #select dropdown
        select_object = Select (select_element)
        select_object.select_by_value('AS')
        time.sleep(5)

        driver.find_element(By.NAME,"organization[note]").send_keys(note)
        time.sleep(1)

        driver.find_element(By.NAME,"btnSaveGenInfo").click()
        time.sleep(5)
         

    def tearDown(self): 
        self.driver.close()

if __name__ == "__main__":
    unittest.main()   
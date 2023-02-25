import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class TestLoginOrangeHRM(unittest.TestCase):
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    def test_a_login_OrangeHRM_success(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com") #open Website
        time.sleep(5)
        driver.find_element(By.NAME, "username").send_keys("Admin") #input username
        time.sleep(2)
        driver.find_element(By.NAME, "password").send_keys("admin123") #input password
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() #click button Login
        time.sleep(2)
        Dashboard_tag = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span") #validate dashboard page
        self.assertEqual(Dashboard_tag.text, "Dashboard")  
        time.sleep(2)
        assert driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[2]/ul/li/span") #validate Profile
        time.sleep(2)
        print("Login Succes")
    
    
    def tearDown(self): 
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()
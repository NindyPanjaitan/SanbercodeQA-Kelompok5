import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from element import elem
from value import data


class OrangeHRM(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        self.url = "https://opensource-demo.orangehrmlive.com/"

    def test_search(self):
        # steps
        driver = self.browser
        driver.maximize_window()
        driver.get(self.url)  # link url
        time.sleep(3)
        name = driver.find_element(By.NAME, elem.username)
        name.send_keys("Admin")
        password = driver.find_element(By.NAME, elem.password)
        password.send_keys("admin123")
        time.sleep(1)
        driver.find_element(By.TAG_NAME, elem.btnLogin).click()
        time.sleep(3)
        driver.find_element(By.XPATH, elem.menuAdmin).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectDropdown).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.selectOrganization).click()
        time.sleep(1)
        driver.find_element(By.XPATH, elem.nameLoc).send_keys(data.name)
        time.sleep(1)

        driver.find_element(By.XPATH, elem.btnSearch).click()
        time.sleep(5)

        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]/div[1]/span[1]").text
        self.assertIn(response_data, '(1) Record Found')

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()

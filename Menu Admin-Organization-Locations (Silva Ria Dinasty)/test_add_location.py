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

    def test_add_location(self):
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
        driver.find_element(By.XPATH, elem.btnAdd).click()
        time.sleep(5)
        # Add Location
        driver.find_element(By.XPATH, elem.name).send_keys(data.name)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.city).send_keys(data.city)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.pCode).send_keys(data.pCode)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.phone).send_keys(data.phone)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.address).send_keys(data.address)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.state).send_keys(data.state)
        time.sleep(1)
        driver.find_element(By.XPATH, elem.fax).send_keys(data.fax)
        time.sleep(1)
        ####

        wait = WebDriverWait(driver, 0)
        dropdown = wait.until(EC.visibility_of_element_located(
            (By.XPATH, elem.country)))
        dropdown.click()
        dropdown.send_keys("asdasda")
        time.sleep(1)
        dropdown.send_keys(Keys.RETURN)

        driver.find_element(By.XPATH, elem.notes).send_keys(data.notes)

        # Button Save
        driver.find_element(
            By.XPATH, elem.btnSave).click()
        time.sleep(5)

        # validasi
        response_data = driver.find_element(
            By.XPATH, "//body/div[@id='app']/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/h5[1]").text
        self.assertIn(response_data, 'Locations')

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
    unittest.main()

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import loginSuccess

class jobTitles(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Chrome(ChromeDriverManager().install())

  # success delete 1 job titles
  def test_job(self):
    # steps
    driver = self.browser
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(1)
    driver.maximize_window()
    loginSuccess.test_success_login(driver)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[4]/div/button[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[3]/div/div/div/div[3]/button[2]").click()
    time.sleep(2)

    # validasi
    driver.find_element(By.CLASS_NAME, "oxd-loading-spinner-container")
    time.sleep(2)
    driver.close()

  # success delete all job titles
  def test_job_all(self):
    # steps
    driver = self.browser
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(1)
    driver.maximize_window()
    loginSuccess.test_success_login(driver)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[3]/div/div[1]/div/div[1]/div/label/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[2]/div/div/button").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[3]/div/div/div/div[3]/button[2]").click()
    time.sleep(2)

    # validasi
    driver.find_element(By.CLASS_NAME, "oxd-loading-spinner-container")
    time.sleep(2)
    driver.close()

if __name__ == "__main__":
  unittest.main()
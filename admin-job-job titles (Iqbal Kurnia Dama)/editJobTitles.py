import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import loginSuccess
from selenium.webdriver.common.keys import Keys

class jobTitles(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Chrome(ChromeDriverManager().install())

  # success edit testing job titles
  def test_edit_job(self):
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
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[4]/div/button[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input").send_keys(" edit test")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/textarea").send_keys("edit test description")
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "oxd-file-input").send_keys("C:/Users/iqbal/Downloads/Quality Assurance.pdf")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div[2]/textarea").send_keys("edit test note")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[5]/button[2]").click()
    time.sleep(2)

    # validasi
    driver.find_element(By.CLASS_NAME, "oxd-loading-spinner-container")
    time.sleep(2)
    driver.close()

  # test edit job titles with empty job title and size exceeded
  def test_edit_job_1(self):
    # steps
    driver = self.browser
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(1)
    driver.maximize_window()
    loginSuccess.test_success_login(driver)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[4]/div/button[2]").click()
    time.sleep(2)
    hapus = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input")
    hapus.send_keys(Keys.CONTROL + "a")
    hapus.send_keys(Keys.DELETE)
    hapus.send_keys("")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/textarea").send_keys("edit test description")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div[1]/div[2]/div/div[2]/div[3]/div[2]/div/label/span").click()
    driver.find_element(By.CLASS_NAME, "oxd-file-input").send_keys("C:/Users/iqbal/Downloads/Quality Assurance.pdf")
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div[2]/textarea").send_keys("edit test note")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[5]/button[2]").click()
    time.sleep(2)

    # validasi
    response_data = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/span").text
    self.assertIn(response_data, "Required")
    driver.close()

  # failed add testing job titles with size exceeded
  def test_edit_job_2(self):
    # steps
    driver = self.browser
    driver.get("https://opensource-demo.orangehrmlive.com/")
    time.sleep(1)
    driver.maximize_window()
    loginSuccess.test_success_login(driver)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[1]/a").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[4]/div/button[2]").click()
    time.sleep(2)
    hapus = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/input")
    hapus.send_keys(Keys.CONTROL + "a")
    hapus.send_keys(Keys.DELETE)
    hapus.send_keys("test 123")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/textarea").send_keys("edit test description")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div[1]/div[2]/div/div[2]/div[3]/div[2]/div/label/span").click()
    driver.find_element(By.CLASS_NAME, "oxd-file-input").send_keys("C:/Users/iqbal/Downloads/Book.pdf")
    time.sleep(3)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div[2]/textarea").send_keys("edit test note")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[5]/button[2]").click()
    time.sleep(2)

    # validasi
    response_data = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[3]/div[2]/div/span").text
    self.assertIn(response_data, "Attachment Size Exceeded")
    driver.close()

if __name__ == "__main__":
  unittest.main()
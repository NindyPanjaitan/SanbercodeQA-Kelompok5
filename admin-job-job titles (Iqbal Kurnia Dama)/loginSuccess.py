# import unittest
# import time
# from selenium import webdriver
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager

# class TestLogin(unittest.TestCase):

#   def setUp(self):
#     self.browser = webdriver.Chrome(ChromeDriverManager().install())

def test_success_login(driver):
  # steps
  # driver = self.browser
  # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
  # time.sleep(1)
  driver.find_element(By.NAME, "username").send_keys("Admin")
  # time.sleep(1)
  driver.find_element(By.NAME, "password").send_keys("admin123")
  # time.sleep(1)
  driver.find_element(By.CLASS_NAME, "oxd-button").click()
  # time.sleep(1)


    # validasi
    # current_url = driver.current_url
    # self.assertEqual(current_url, "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

# if __name__ == "__main__":
#   unittest.main()
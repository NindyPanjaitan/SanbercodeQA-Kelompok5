import unittest
import time
import pyautogui 
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import TC_Login

class PIM_Add_Employee(unittest.TestCase):
    loginPage = TC_Login.TestLoginOrangeHRM()
    
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.loginPage.driver = self.driver
    def test_a_add_employee_without_login_details(self):
        self.loginPage.test_a_login_OrangeHRM_success() 
        driver = self.driver
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]").click() #Click PIM Menu 
        time.sleep(2)
        PIM_PAGE = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span") #Validation for PIM Page
        self.assertEqual(PIM_PAGE.text, "PIM")
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]").click() #Click Add Employee
        time.sleep(2)
        ADD_EMPLOYEE_PAGE = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/h6") #Validation for Add Employee Page
        self.assertEqual(ADD_EMPLOYEE_PAGE.text, "Add Employee")
        time.sleep(2)
        driver.find_element(By.NAME,"firstName").send_keys("Nindy") #Input first name
        time.sleep(2)
        driver.find_element(By.NAME,"middleName").send_keys("Pitta") #Input middle name
        time.sleep(2)
        driver.find_element(By.NAME,"lastName").send_keys("PJT") #Input last name
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input").send_keys(Keys.CONTROL + "a") #input Employee ID
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input").send_keys("2010") #input Employee ID
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div/button").click() #Upload images
        time.sleep(3)
        pyautogui.write(r"C:\Users\Formulatrix\OneDrive\Pictures\testgambar.jpg")
        time.sleep(3)
        pyautogui.press("enter")
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click() #click save button
        time.sleep(2)
        assert driver.find_element(By.XPATH, "//*[@id='oxd-toaster_1']") #validate notification
        time.sleep(5)
        Personal_Details = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6") #Validation for personal detail page
        self.assertEqual(Personal_Details.text, "Personal Details")
        time.sleep(5)
    
    def test_b_add_employee_with_login_details_n_enable_status(self):
        self.loginPage.test_a_login_OrangeHRM_success() 
        driver = self.driver
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]").click() #Click PIM Menu 
        time.sleep(2)
        PIM_PAGE = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span") #Validation for PIM Page
        self.assertEqual(PIM_PAGE.text, "PIM")
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]").click() #Click Add Employee
        time.sleep(2)
        ADD_EMPLOYEE_PAGE = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/h6") #Validation for Add Employee Page
        self.assertEqual(ADD_EMPLOYEE_PAGE.text, "Add Employee")
        time.sleep(2)
        driver.find_element(By.NAME,"firstName").send_keys("Nindy") #Input first name
        time.sleep(2)
        driver.find_element(By.NAME,"middleName").send_keys("Pitta") #Input middle name
        time.sleep(2)
        driver.find_element(By.NAME,"lastName").send_keys("PJT") #Input last name
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input").send_keys(Keys.CONTROL + "a") #input Employee ID
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input").send_keys("909090") #input Employee ID
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div/button").click() #Upload images
        time.sleep(3)
        pyautogui.write(r"C:\Users\Formulatrix\OneDrive\Pictures\testgambar.jpg")
        time.sleep(3)
        pyautogui.press("enter")
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span").click() #Switch on login details 
        time.sleep(2)
        username = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[1]/label") #validate username
        self.assertEqual(username.text, "Username")
        time.sleep(1)
        status = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[1]/label") #validate status
        self.assertEqual(status.text, "Status")
        time.sleep(1)
        password = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[1]/label") #validate password
        self.assertEqual(password.text, "Password")
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label/span").click() #Check Enabled Status
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input").send_keys("Nindy0001") #input Username
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 5000)")
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input").send_keys("Semangat12345!") #input Password
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input").send_keys("Semangat12345!") #input Confirm Password
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click() #click save button
        time.sleep(2)
        assert driver.find_element(By.XPATH, "//*[@id='oxd-toaster_1']") #validate notification
        time.sleep(5)
        Personal_Details = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6") #Validation for personal detail page
        self.assertEqual(Personal_Details.text, "Personal Details")
        time.sleep(5) 
        
    def test_c_add_employee_with_login_details_n_disable_status(self):
        self.loginPage.test_a_login_OrangeHRM_success() 
        driver = self.driver
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]").click() #Click PIM Menu 
        time.sleep(2)
        PIM_PAGE = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span") #Validation for PIM Page
        self.assertEqual(PIM_PAGE.text, "PIM")
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]").click() #Click Add Employee
        time.sleep(2)
        ADD_EMPLOYEE_PAGE = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/h6") #Validation for Add Employee Page
        self.assertEqual(ADD_EMPLOYEE_PAGE.text, "Add Employee")
        time.sleep(2)
        driver.find_element(By.NAME,"firstName").send_keys("Nindy") #Input first name
        time.sleep(2)
        driver.find_element(By.NAME,"middleName").send_keys("Pitta") #Input middle name
        time.sleep(2)
        driver.find_element(By.NAME,"lastName").send_keys("PJT") #Input last name
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input").send_keys(Keys.CONTROL + "a") #input Employee ID
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input").send_keys("123140") #input Employee ID
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div/button").click() #Upload images
        time.sleep(3)
        pyautogui.write(r"C:\Users\Formulatrix\OneDrive\Pictures\testgambar.jpg")
        time.sleep(3)
        pyautogui.press("enter")
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span").click() #Switch on login details 
        time.sleep(2)
        username = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[1]/label") #validate username
        self.assertEqual(username.text, "Username")
        time.sleep(1)
        status = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[1]/label") #validate status
        self.assertEqual(status.text, "Status")
        time.sleep(1)
        password = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[1]/label") #validate password
        self.assertEqual(password.text, "Password")
        time.sleep(1)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div").click() #Check Disabled Status
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input").send_keys("Nindy000") #input Username
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 5000)")
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input").send_keys("Semangat12345!") #input Password
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input").send_keys("Semangat12345!") #input Confirm Password
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click() #click save button
        time.sleep(2)
        assert driver.find_element(By.XPATH, "//*[@id='oxd-toaster_1']") #validate notification
        time.sleep(5)
        Personal_Details = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6") #Validation for personal detail page
        self.assertEqual(Personal_Details.text, "Personal Details")
        time.sleep(5)     
        
                
if __name__ == "__main__":
    unittest.main()

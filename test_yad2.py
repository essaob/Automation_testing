import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


# Launch Chrome using undetected_chromedriver
# options = uc.ChromeOptions()
# options.add_argument("--start-maximized")
#
# driver = uc.Chrome(options=options)
# driver.get("https://www.yad2.co.il/")
# sleep(5)
#
# # Optional login section (currently commented out)
# # Email = driver.find_element(By.CLASS_NAME, 'direction-ltr')
# # Email.send_keys('alobraessa2212@gmail.com')
# # sleep(2)
# # User_pass = driver.find_element(By.ID, 'password')
# # User_pass.send_keys('your_password_here')
# # sleep(2)
# # Login = driver.find_element(By.ID, 'login-button')
# # Login.click()
# # sleep(5)
#
# # Click on an element by XPath (Hebrew alt text: 'כניסה')
# element = driver.find_element(By.XPATH, "//img[@alt='רכב']")
# element.click()
# sleep(3)
#
# elements = driver.find_elements(By.XPATH, "//img[@data-testid='image']")
# if len(elements)>0 :
#     print("ok , number the elemnts = ", len(elements))

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.yad2.co.il/")
    # sleep(40)
    yield driver
    driver.quit()


# def test_Pagecar(driver):
#     element = driver.find_element(By.XPATH, "//img[@alt='רכב']")
#     element.click()
#     sleep(3)
#
#     elements = driver.find_elements(By.XPATH, "//img[@data-testid='image']")
#     if len(elements) > 0:
#         print("open page car , Successfully! , number the elemnts = ", len(elements))


def test_history(driver):
    element = driver.find_element(By.XPATH,"//*[@id='__next']/div[1]/div[1]/header/div[4]/div/button")
    sleep(5)
    element.click()
    sleep(3)
    elements = driver.find_elements(By.XPATH, "//*[@id='__next']/div[1]/div[1]/header/div[4]/section/ul[2]/li[3]/a/span[1]")
    elements[1].click()
    sleep(10)
    # element.click()
    # elements = driver.find_elements(By.XPATH, "//a[@data-v-5ff130d0='']")
    # if len(elements) > 0:
    #     print("History search , Successfully! , number the elemnts = ", len(elements))
    #



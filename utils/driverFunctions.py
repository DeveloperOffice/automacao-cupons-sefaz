from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.by import By
import time

def locateByXpath(driver, time, xpath):
    try:
        element = WebDriverWait(driver, time).until(
        EC.presence_of_element_located((By.XPATH, xpath))
        )

        return element
    
    except:
        print(f'Element not found by XPath: {xpath}')
        return    
                
    
def findElementByXpath(driver, xpath):
    try:
        element = driver.find_element(By.XPATH, xpath)

        return element
    
    except:
        print(f'Element not found by XPath: {xpath}')
        return
    
    
def findElementsByXpath(driver, xpath):
    try:
        elements = driver.find_elements(By.XPATH, xpath)
        
        return elements
    
    except:
        print(f'Elements not found by XPath: {xpath}')
        return
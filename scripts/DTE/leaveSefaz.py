from utils.driverFunctions import *


def leaveSefazDte(driver):
       
    userButtonSefaz = locateByXpath(driver, 30, '//*[@id="perfil-empresa"]/li[2]/a')
    userButtonSefaz.click()
    time.sleep(2)
    
    exitButtonSefaz = locateByXpath(driver, 30, '//*[@id="perfil-empresa"]/li[2]/ul/li[2]/div/a')
    exitButtonSefaz.click()
    time.sleep(2)
    
    driver.get('https://portal-dte.sefaz.ce.gov.br/#/home')
    
    time.sleep(2)
    
    userButtonDte = locateByXpath(driver, 30, '/html/body/my-app/header/div/div/nav/ul/li[3]/a')
    userButtonDte.click()
    
    time.sleep(3)
    
    exitButtonDte = locateByXpath(driver, 30, '/html/body/my-app/header/div[2]/div/nav/ul/li[2]/div/button')
    exitButtonDte.click()
    
    time.sleep(2)
from utils.driverFunctions import *

from selenium.webdriver.support.ui import Select

def loginAmbienteSeguro(driver, user, password):
    driver.get("https://servicos.sefaz.ce.gov.br/internet/AcessoSeguro/ServicoSenha/logarusuario/login.asp")
    
    time.sleep(2)
    
    print("Realizando LOGIN")
    
    #Preenchendo dados usuario
    userInput = locateByXpath(driver, 30, '//*[@id="txtUsuario"]')
    userInput.send_keys(user)
    time.sleep(0.5)
    
    #Preenchendo dados senha
    passwordInput = locateByXpath(driver, 30,  '//*[@id="txtSenha"]')
    passwordInput.send_keys(password)
    time.sleep(0.5)
    
    #Select BOX / seleciona CONTADOR
    select_element = findElementByXpath(driver, '//*[@id="cboTipoUsuario"]')
    select = Select(select_element)
    select.select_by_value("3")

    #Clica no botão entrar
    buttonLogin = findElementByXpath(driver, '//*[@id="btEntrar"]')
    buttonLogin.click()
    
    time.sleep(2)
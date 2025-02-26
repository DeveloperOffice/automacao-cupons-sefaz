from utils.driverFunctions import *

def LinkXML(driver):
    
    # Abrir a aba de downloads do Chrome
    driver.get("chrome://downloads/")

    # Aguardar um momento para a página carregar
    time.sleep(3)

    # Executar JavaScript para extrair os downloads
    downloadLink = driver.execute_script(
        "return document.querySelector('downloads-manager').shadowRoot.querySelector('downloads-item').shadowRoot.querySelector('a').href"
    )

    return downloadLink

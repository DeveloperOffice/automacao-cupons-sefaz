from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc

import os

def Chorme():
    try:
        # Configuração do Chrome
        service = Service(ChromeDriverManager().install())
        options = uc.ChromeOptions()

        # Obtém o caminho para a pasta do usuário
        user_data_dir = os.path.join(
            os.path.expanduser("~"), 
            "AppData", "Local", "Google", "Chrome", "User Data"
        )

        # Adiciona o argumento ao Selenium
        options.add_argument(f"--user-data-dir={user_data_dir}")
        options.add_argument("--profile-directory=Default")  # Modifique se necessário

        # Configurações para evitar bloqueios
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-gpu")
        options.add_argument("--allow-running-insecure-content")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--start-fullscreen")
        
        # Inicia o navegador
        driver = uc.Chrome(service=service, options=options)
        
        return driver
    
    except:
        raise Exception('Erro ao inicializar o Google, verifique se você possui o Google Chrome instalado e atualizado.')
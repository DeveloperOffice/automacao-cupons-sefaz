# Classes
from classes.login import user_login
from classes.CFElist import cfe_list

# Utils
from utils.CompanyFormater import formatCompanyCode
from utils.csvReader import readCSV
from utils.xml_organizer import *

# Importando navegador
from config.browserConfig import Chrome

# Importanto função de autenticação
from auth.validateAcess import authorize_access

# INTERFACE GRÁFICA
from Interface.front import startInterface
from Interface.errorWindow import error_message
from Interface.continueWindow import continue_message
from Interface.app_state import app_state

# Scripts todos os passos do DTE
from scripts.DTE.start import startProcess
from scripts.DTE.company_finder import companyFinder
from scripts.DTE.sigetWindow import enterSiget
from scripts.DTE.Break import passBreak
from scripts.DTE.searchCsv import downloadCsvAut, downloadCsvCancel

# Scripts todos os passos do Ambiente Seguro
from scripts.AmbienteSeguro.start import loginAmbienteSeguro
from scripts.AmbienteSeguro.enterFMeModule import enterMfeModule
from scripts.AmbienteSeguro.company_finder import company_finder_AmbSeg
from scripts.AmbienteSeguro.CfeQuery import cfeQuery

# Scripts para puxar todos os XML
from scripts.PullXML.LinkAPI import LinkXML
from scripts.PullXML.GetXML import getXML

import time
import os


downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

acessValidator = authorize_access()  # True or False


def initialize():
    try:

        startInterface()

        if app_state.next == True:
            driver = Chrome()

            startProcess(driver)

            formatedCode = formatCompanyCode(app_state.inscricao_estadual)

            companyFinder(driver, formatedCode)

            enterSiget(driver)

            passBreak(driver)

            responseAut = downloadCsvAut(driver)
            if responseAut == True:
                readCSV(downloads_path, "Autorizados")
                apagarCSV(downloads_path)

            responseCancel = downloadCsvCancel(driver)
            if responseCancel == True:
                readCSV(downloads_path, "Cancelados")
                apagarCSV(downloads_path)

            # Credenciais ambiente seguro
            user = user_login.username
            password = user_login.password

            loginAmbienteSeguro(driver, user, password)
            enterMfeModule(driver)
            company_finder_AmbSeg(driver, app_state.inscricao_estadual)

            # tem que ver a opção da janela
            cfeQuery(driver, cfe_list.totalList[0])

            filterList = analisadorXmls(cfe_list.totalList)
            linkApi = LinkXML(driver)

            continue_message(
                "Processo iniciado, o nevegador será fechado, o computador poderá ser utilizado normalmente enquanto os XMLS são baixados."
            )
            driver.quit()

            # Começar processo de download dos XMLS
            try:
                print(filterList[:10])
                for index, xml in enumerate(filterList):
                    getXML(xml, linkApi)
                    print(f"Processando {index + 1} de {len(filterList)} Xmls...")
                    print(xml)

                time.sleep(2)

                continue_message(
                    f"Processo finalizado, {len(filterList)} XMLs foram baixados, verificar pasta."
                )

            except:
                error_message(
                    "Ocorreu uma instabilidade no ambiente seguro, não foi possivel baixar todos os cupons, por gentileza, reinicie o programa."
                )

        else:
            raise Exception("Programa encerrado...")

    except Exception as e:
        print(f"Erro: {e}")


initialize()
organizarPastas()

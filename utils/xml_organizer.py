import os
import locale
from datetime import datetime
import shutil
import os
import glob

def analisadorXmls(lista):
    # Tenta definir o locale para português do Brasil
    try:
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    except locale.Error:
        print("Locale 'pt_BR.UTF-8' não está disponível. Usando configurações padrão.")

    # Obtém o caminho da área de trabalho e diretório de downloads
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    pastaPrincipal = os.path.join(desktop_path, "PastaOrganizada")
    
    arquivos_xml = []
    for root, dirs, files in os.walk(pastaPrincipal):
        for file in files:
            if file.endswith('.xml'):
                arquivos_xml.append(os.path.join(root, file))
    
    listaXMLS = [os.path.basename(caminho).replace('.xml', '') for caminho in arquivos_xml]
    # print('esses são os xml da pasta: ',listaXMLS[2:10])
    lista_sem_espacos = [item.strip() for item in lista]

    filtro = [item for item in lista_sem_espacos if item not in listaXMLS]
    print(f'Faltam apenas {len(filtro)} XML para serem baixados')
    
    return filtro

def apagarCSV(pasta):
    # Apaga todos os arquivos CSV na pasta
    for arquivo in glob.glob(os.path.join(pasta, "*.csv")):
        os.remove(arquivo)
        print(f"Arquivo apagado: {arquivo}")
        
def organizarPastas():
    # Tenta definir o locale para português do Brasil
    try:
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    except locale.Error:
        print("Locale 'pt_BR.UTF-8' não está disponível. Usando configurações padrão.")

    # Obtém o caminho da área de trabalho e diretório de downloads
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")

    meses_map = {
        1: "Janeiro",
        2: "Fevereiro",
        3: "Março",
        4: "Abril",
        5: "Maio",
        6: "Junho",
        7: "Julho",
        8: "Agosto",
        9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro"
    }

    # Obtém o ano e o mês atuais
    ano = datetime.now().year
    ano_atual = str(ano)
    mes_atualNumero = datetime.now().month
    mes_atual = meses_map[mes_atualNumero]
    nome_mes = f"{mes_atualNumero:02d}-{mes_atual}"

    arquivos_existentes = set(os.listdir(downloads_dir))
    somaMov = 0
    somaDel = 0
    print('Organizando XMLS, aguarde...')  
    # Loop para criar diretórios apenas para arquivos XML
    for inscricao in arquivos_existentes:
        origem = os.path.join(downloads_dir,inscricao)
        if inscricao.lower().endswith('.xml'):
            # Verifica se a substring tem o comprimento esperado
            if len(inscricao) >= 6:
                mesnumero = inscricao[4:6]

                # Verifica se a substring é numérica antes de converter
                if mesnumero.isdigit():
                    mes_arquivo_numero = int(mesnumero)

                    # Obter o nome do mês correspondente ao número
                    ano_do_arquivo = f'20{inscricao[2:4].strip()}'
                    destino = os.path.join(desktop_path, 'PastaOrganizada', inscricao[6:20], ano_do_arquivo, f'{mes_arquivo_numero}-{meses_map[mes_arquivo_numero]}')

                    arquivoFinal = os.path.join(destino,inscricao)
                    # Verifica se o diretório já existe, se não, cria
                    if not os.path.exists(destino):
                        os.makedirs(destino)
                        print(f"Diretório criado para {inscricao[6:20]}/{ano_do_arquivo}/{mes_arquivo_numero}-{meses_map[mes_arquivo_numero]}")
                    
                    if not os.path.exists(arquivoFinal):
                        shutil.move(origem, destino)
                        # print(f'{inscricao} movido para {destino}')
                        somaMov = somaMov + 1
                    
                    else:
                        os.remove(origem)
                        # print(f'{inscricao}: O XML já existe na pasta, arquivo removido com sucesso')
                        somaDel = somaDel + 1  
                
                else:
                    print(f"Nome do arquivo inválido para conversão para mês: '{inscricao}'")
            else:
                print(f"Tamanho insuficiente para extrair mês do arquivo: '{inscricao}'")
              
    print(f'XMLS removidos: {somaDel}')
    print(f'XMLS organizados: {somaMov}')       
                
organizarPastas()
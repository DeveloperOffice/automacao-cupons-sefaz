<p align="center">
  <img src="./assets/read.png" alt="Office Logo" width="250px">
</p>

---

![Versão](https://img.shields.io/badge/version-2.0.0-blue)
![Status](https://img.shields.io/badge/status-Concluído-green)

# 📌 Sobre o Projeto

Este projeto realiza **automação de cupons fiscais da SEFAZ** utilizando Python e Selenium, otimizando processos e aumentando a produtividade.

---

## 🚀 Tecnologias Utilizadas

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github)

</div>

---

# 📖 Manual de Instalação

## 🛠️ 1. Pré-requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados:

✅ **Python 3.10+** → [Baixar aqui](https://www.python.org/downloads/)  
✅ **Git** → [Baixar aqui](https://git-scm.com/downloads)  
✅ **Google Chrome** → [Baixar aqui](https://www.google.com/chrome/)  
✅ **ChromeDriver** (mesma versão do Chrome) → [Baixar aqui](https://sites.google.com/chromium.org/driver/)

---

## 📥 2. Clonando o Repositório

Abra o **terminal** ou **Prompt de Comando** e execute:

```sh
git clone https://github.com/DeveloperOffice/automacao-cupons-sefaz
cd automacao-cupons-sefaz
```

## 📦 3. Instalando Dependências

Com o Python instalado, execute:

```sh
pip install -r requirements.txt
```

Se quiser usar um ambiente virtual (recomendado):

```sh
#Criando Ambiente Virtual
python -m venv venv

#Entrando Ambiente Virtual
venv\Scripts\

#Instalando Dependencias
pip install -r requirements.txt
```

## 🔑 4. Pegando Autenticação

É necessário criar um arquivo "T.py" e coloca-lo na pasta auth do projeto, o arquivo deve ter a seguinte estrutura:

###### T.py

```sh
TOKEN = "21avcas32v1asv1sd56v1as5v4as5v4"
```

O token deve ser fornecido pelo administrador

## 🚀 5. Executando o Projeto

Para iniciar o script de automação, execute:

```sh
python index.py
```

## 🛠️ 6. Possíveis Erros e Soluções

| **Erro**                                           | **Solução**                                                                                                  |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| `ModuleNotFoundError: No module named 'X'`         | Execute `pip install -r requirements.txt` novamente.                                                         |
| `chromedriver not found`                           | Baixe o [ChromeDriver](https://sites.google.com/chromium.org/driver/) correspondente à versão do seu Chrome. |
| `Navegador não abre` Mesmo executando corretamente | O projeto só funciona se o navegador chorme estiver na última versão `Atualize o seu navegador.`             |

## 📞 7. Suporte e Contato

📧 **Email:** [tecnologia@office-ce.com.br](mailto:tecnologia@office-ce.com.br)  
🐙 **GitHub Issues:** [Abrir uma issue](https://github.com/DeveloperOffice/automacao-cupons-sefaz/issues)  
💬 **Instagram:** [@officecontabilce](https://www.instagram.com/officecontabilce/)

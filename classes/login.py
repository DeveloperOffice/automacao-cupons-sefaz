import json
import os

class User_Login:
    
    CONFIG_FILE = "user_config.json"  # Nome do arquivo onde será salvo o usuário

    def __init__(self):
        """Inicializa a classe carregando apenas o nome de usuário do arquivo JSON."""
        self.username = ''
        self.password = None  # Senha nunca será salva
        self.load_credentials()

    def load_credentials(self):
        """Carrega o nome de usuário do arquivo JSON, se existir."""
        if os.path.exists(self.CONFIG_FILE):
            try:
                with open(self.CONFIG_FILE, "r") as file:
                    data = json.load(file)
                    self.username = data.get("username", None)
            except (json.JSONDecodeError, IOError):
                print("Erro ao carregar o arquivo de configuração. Definindo valores padrão.")
                self.username = ''
        else:
            self.username = ''

    def set_data(self, username, password):
        """Salva o nome de usuário e senha no arquivo JSON."""
        self.username = username
        self.password = password
        data = {"username": self.username}
        try:
            with open(self.CONFIG_FILE, "w") as file:
                json.dump(data, file, indent=4)
                
        except IOError:
            print("Erro ao salvar os dados de login.")
            
    def clear_username(self):
        """Remove o nome de usuário armazenado."""
        self.username = None
        if os.path.exists(self.CONFIG_FILE):
            os.remove(self.CONFIG_FILE)
            

user_login = User_Login()
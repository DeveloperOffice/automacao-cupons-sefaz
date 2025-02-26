class CfeList:
    """Classe para armazenar os dados globais do sistema."""
    
    def __init__(self):
        self.totalList = []

    def add_data_cfe(self, elements):
        """Atualiza os dados no estado global"""
        self.totalList.extend(elements)

# Criamos uma instância global da classe para armazenar os dados
cfe_list = CfeList()

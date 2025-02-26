class AppState:
    """Classe para armazenar os dados globais do sistema."""
    
    def __init__(self):
        self.inscricao_estadual = None
        self.mes = None
        self.ano = None
        self.next = False
    def set_data(self,inscricao_estadual, mes, ano):
        """Atualiza os dados no estado global"""
        self.inscricao_estadual = inscricao_estadual
        self.mes = mes
        self.ano = ano
        
    def autorizationNext(self, autorization):
        """Atualiza o estado global para permitir a próxima etapa"""
        self.next = autorization
# Criamos uma instância global da classe para armazenar os dados
app_state = AppState()

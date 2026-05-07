class SessaoService:
    def __init__(self, repository):
        self.repository = repository

    def consultar_sessao(self, sessao_id):
        sessao = self.repository.buscar_por_id(sessao_id)

        if sessao is None:
            raise ValueError("Sessão não encontrada")

        # aqui poderiam existir regras de negócio
        return sessao
    
    def listar_todas_sessoes(self):
        return self.repository.buscar_todas_sessoes()
    
    def listar_sessoes_em_andamento(self):
        """Retorna apenas sessões que estão em andamento"""
        return self.repository.buscar_sessoes_em_andamento()
    
    def listar_proximas_sessoes(self):
        """Retorna apenas próximas sessões agendadas"""
        return self.repository.buscar_proximas_sessoes()
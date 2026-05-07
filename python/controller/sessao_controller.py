from service.sessao_service import SessaoService


class SessaoController:
    def __init__(self, service):
        self.service = service

    def request_consulta_sessao(self, sessao_id):
        try:
            sessao = self.service.consultar_sessao(sessao_id)
            return sessao
        except ValueError as erro:
            return {"erro": str(erro)}
    
    def request_listar_todas(self):
        try:
            sessoes = self.service.listar_todas_sessoes()
            return sessoes
        except Exception as erro:
            return {"erro": str(erro)}
    
    def request_sessoes_em_andamento(self):
        try:
            sessoes = self.service.listar_sessoes_em_andamento()
            return sessoes
        except Exception as erro:
            return {"erro": str(erro)}
    
    def request_proximas_sessoes(self):
        try:
            sessoes = self.service.listar_proximas_sessoes()
            return sessoes
        except Exception as erro:
            return {"erro": str(erro)}

class FilmeController:
    def __init__(self, service):
        self.service = service

    def criar_filme(self, titulo, genero, duracao_minutos, classificacao_indicativa, sinopse):
        """Controller para criar novo filme"""
        return self.service.criar_novo_filme(titulo, genero, duracao_minutos, classificacao_indicativa, sinopse)

    def obter_filme(self, filme_id):
        """Controller para obter um filme específico"""
        return self.service.consultar_filme(filme_id)

    def obter_todos_filmes(self):
        """Controller para obter todos os filmes"""
        return self.service.listar_todos_filmes()

    def obter_filmes_em_cartaz(self):
        """Controller para obter filmes em cartaz"""
        return self.service.listar_filmes_em_cartaz()

    def atualizar_filme(self, filme_id, **kwargs):
        """Controller para atualizar um filme"""
        return self.service.atualizar_filme(filme_id, **kwargs)

    def remover_filme(self, filme_id):
        """Controller para remover um filme"""
        return self.service.remover_filme(filme_id)

    def tirar_filme_de_cartaz(self, filme_id):
        """Controller para tirar filme de cartaz"""
        return self.service.tirar_de_cartaz(filme_id)

    def colocar_filme_em_cartaz(self, filme_id):
        """Controller para colocar filme em cartaz"""
        return self.service.colocar_em_cartaz(filme_id)

    def obter_estatisticas(self):
        """Controller para obter estatísticas de filmes"""
        return self.service.obter_estatisticas()

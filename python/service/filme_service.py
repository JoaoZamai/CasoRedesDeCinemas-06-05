class FilmeService:
    def __init__(self, repository):
        self.repository = repository

    def criar_novo_filme(self, titulo, genero, duracao_minutos, classificacao_indicativa, sinopse):
        """Criar um novo filme com validações de negócio"""
        if not titulo or len(titulo.strip()) == 0:
            raise ValueError("Título do filme é obrigatório")
        
        if duracao_minutos and duracao_minutos <= 0:
            raise ValueError("Duração deve ser maior que 0")
        
        if classificacao_indicativa and (classificacao_indicativa < 0 or classificacao_indicativa > 18):
            raise ValueError("Classificação indicativa inválida")
        
        return self.repository.criar_filme(titulo, genero, duracao_minutos, classificacao_indicativa, sinopse)

    def consultar_filme(self, filme_id):
        """Consultar um filme específico"""
        filme = self.repository.buscar_por_id(filme_id)
        
        if filme is None:
            raise ValueError(f"Filme com ID {filme_id} não encontrado")
        
        return filme

    def listar_todos_filmes(self):
        """Retorna todos os filmes cadastrados"""
        return self.repository.buscar_todos_filmes()

    def listar_filmes_em_cartaz(self):
        """Retorna apenas os filmes que estão em cartaz"""
        return self.repository.buscar_filmes_em_cartaz()

    def atualizar_filme(self, filme_id, **kwargs):
        """Atualizar informações de um filme"""
        filme = self.repository.buscar_por_id(filme_id)
        
        if filme is None:
            raise ValueError(f"Filme com ID {filme_id} não encontrado")
        
        return self.repository.atualizar_filme(filme_id, **kwargs)

    def remover_filme(self, filme_id):
        """Remover um filme do catálogo"""
        filme = self.repository.buscar_por_id(filme_id)
        
        if filme is None:
            raise ValueError(f"Filme com ID {filme_id} não encontrado")
        
        return self.repository.deletar_filme(filme_id)

    def tirar_de_cartaz(self, filme_id):
        """Tirar um filme de cartaz"""
        return self.atualizar_filme(filme_id, em_cartaz=False)

    def colocar_em_cartaz(self, filme_id):
        """Colocar um filme em cartaz"""
        return self.atualizar_filme(filme_id, em_cartaz=True)

    def obter_estatisticas(self):
        """Retorna estatísticas sobre os filmes"""
        return {
            "total_filmes": self.repository.contar_filmes(),
            "filmes_em_cartaz": self.repository.contar_filmes_em_cartaz()
        }

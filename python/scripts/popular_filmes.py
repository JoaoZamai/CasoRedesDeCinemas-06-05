from repository.filme_repository import FilmeRepository
from service.filme_service import FilmeService

# Script para popular o banco de dados com filmes de exemplo

def popular_banco():
    """Popula o banco de dados com filmes de exemplo"""
    repository = FilmeRepository()
    service = FilmeService(repository)
    
    filmes = [
        {
            "titulo": "Duna: Parte Dois",
            "genero": "Ficção Científica",
            "duracao_minutos": 166,
            "classificacao_indicativa": 12,
            "sinopse": "Paulo Atreides viaja para o planeta Arrakis para vingança junto aos Fremen."
        },
        {
            "titulo": "Capitão América: Sentinela da Liberdade",
            "genero": "Ação/Aventura",
            "duracao_minutos": 124,
            "classificacao_indicativa": 12,
            "sinopse": "Sam Wilson assume o manto de Capitão América."
        },
        {
            "titulo": "Insidious: A Porta Vermelha",
            "genero": "Terror",
            "duracao_minutos": 110,
            "classificacao_indicativa": 16,
            "sinopse": "A saga de horror continua com novos mistérios sobrenaturais."
        },
        {
            "titulo": "Divertida Mente 2",
            "genero": "Animação/Comédia",
            "duracao_minutos": 96,
            "classificacao_indicativa": 0,
            "sinopse": "As emoções retornam em nova aventura na mente de Riley."
        },
        {
            "titulo": "Oppenheimer",
            "genero": "Drama/Histórico",
            "duracao_minutos": 180,
            "classificacao_indicativa": 14,
            "sinopse": "A história do criador da bomba atômica, J. Robert Oppenheimer."
        },
        {
            "titulo": "Barbie",
            "genero": "Comédia/Fantasia",
            "duracao_minutos": 114,
            "classificacao_indicativa": 12,
            "sinopse": "Barbie e Ken exploram o mundo real e descobrem mais sobre si mesmos."
        },
        {
            "titulo": "Killers of the Flower Moon",
            "genero": "Crime/Drama",
            "duracao_minutos": 206,
            "classificacao_indicativa": 16,
            "sinopse": "Série de assassinatos misteriosos envolvem a comunidade Osage."
        },
        {
            "titulo": "O Zona de Interesse",
            "genero": "Drama/História",
            "duracao_minutos": 188,
            "classificacao_indicativa": 14,
            "sinopse": "Retrato da vida cotidiana no lado alemão do Holocausto."
        },
    ]
    
    print("Populando banco de dados com filmes...")
    for filme_data in filmes:
        try:
            filme = service.criar_novo_filme(**filme_data)
            print(f"✓ Filme '{filme['titulo']}' adicionado com sucesso!")
        except Exception as e:
            print(f"✗ Erro ao adicionar '{filme_data['titulo']}': {e}")
    
    print("\nBanco de dados populado com sucesso!")
    
    # Mostrar estatísticas
    stats = service.obter_estatisticas()
    print(f"\nEstatísticas:")
    print(f"- Total de filmes: {stats['total_filmes']}")
    print(f"- Filmes em cartaz: {stats['filmes_em_cartaz']}")

if __name__ == "__main__":
    popular_banco()

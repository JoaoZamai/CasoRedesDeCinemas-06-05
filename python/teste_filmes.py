#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de teste para demonstrar as funcionalidades de gerenciamento de filmes
"""

from repository.filme_repository import FilmeRepository
from service.filme_service import FilmeService
from controller.filme_controller import FilmeController
from view.filme_view import FilmeView


def teste_funcionalidades():
    """Testa todas as funcionalidades do sistema de filmes"""
    
    print("\n" + "="*60)
    print("TESTE DO SISTEMA DE GERENCIAMENTO DE FILMES")
    print("="*60)
    
    # Inicializar camadas
    repository = FilmeRepository()
    service = FilmeService(repository)
    controller = FilmeController(service)
    
    # Teste 1: Criar alguns filmes
    print("\n[TEST 1] Criando filmes...")
    filmes_teste = [
        {
            "titulo": "Matrix",
            "genero": "Ficção Científica",
            "duracao_minutos": 136,
            "classificacao_indicativa": 14,
            "sinopse": "Um hacker descobre a verdade sobre o mundo em que vive."
        },
        {
            "titulo": "Inception",
            "genero": "Ficção Científica/Thriller",
            "duracao_minutos": 148,
            "classificacao_indicativa": 14,
            "sinopse": "Um ladrão que rouba segredos corporativos em mundos oníricos."
        },
        {
            "titulo": "Interestelar",
            "genero": "Ficção Científica/Drama",
            "duracao_minutos": 169,
            "classificacao_indicativa": 12,
            "sinopse": "Astronautas viajam por um buraco de minhoca para salvar a humanidade."
        }
    ]
    
    filmes_criados = []
    for filme_data in filmes_teste:
        try:
            filme = controller.criar_filme(**filme_data)
            filmes_criados.append(filme)
            print(f"  ✓ '{filme['titulo']}' criado com ID {filme['id']}")
        except ValueError as e:
            print(f"  ✗ Erro: {e}")
    
    # Teste 2: Listar todos os filmes
    print("\n[TEST 2] Listando todos os filmes...")
    todos_filmes = controller.obter_todos_filmes()
    print(f"  Total de filmes no banco: {len(todos_filmes)}")
    for f in todos_filmes:
        status = "✓ Em Cartaz" if f['em_cartaz'] else "✗ Fora de Cartaz"
        print(f"    - {f['titulo']} ({status})")
    
    # Teste 3: Listar filmes em cartaz
    print("\n[TEST 3] Listando filmes em cartaz...")
    em_cartaz = controller.obter_filmes_em_cartaz()
    print(f"  Filmes em cartaz: {len(em_cartaz)}")
    for f in em_cartaz:
        print(f"    - {f['titulo']} ({f['genero']})")
    
    # Teste 4: Tirar um filme de cartaz
    if filmes_criados:
        print(f"\n[TEST 4] Removendo '{filmes_criados[0]['titulo']}' de cartaz...")
        filme = controller.tirar_filme_de_cartaz(filmes_criados[0]['id'])
        print(f"  ✓ Filme removido de cartaz. Status: em_cartaz = {filme['em_cartaz']}")
    
    # Teste 5: Listar novamente filmes em cartaz
    print("\n[TEST 5] Listando filmes em cartaz novamente...")
    em_cartaz = controller.obter_filmes_em_cartaz()
    print(f"  Filmes em cartaz: {len(em_cartaz)}")
    for f in em_cartaz:
        print(f"    - {f['titulo']}")
    
    # Teste 6: Obter um filme específico
    if filmes_criados:
        print(f"\n[TEST 6] Consultando filme específico (ID {filmes_criados[0]['id']})...")
        filme = controller.obter_filme(filmes_criados[0]['id'])
        print(f"  Título: {filme['titulo']}")
        print(f"  Gênero: {filme['genero']}")
        print(f"  Duração: {filme['duracao_minutos']} minutos")
        print(f"  Classificação: {filme['classificacao_indicativa']}+")
        print(f"  Em Cartaz: {'Sim' if filme['em_cartaz'] else 'Não'}")
    
    # Teste 7: Atualizar um filme
    if len(filmes_criados) > 1:
        print(f"\n[TEST 7] Atualizando filme '{filmes_criados[1]['titulo']}'...")
        filme = controller.atualizar_filme(
            filmes_criados[1]['id'],
            titulo="Inception - Edição Estendida",
            genero="Ficção Científica"
        )
        print(f"  ✓ Filme atualizado:")
        print(f"    - Novo título: {filme['titulo']}")
        print(f"    - Novo gênero: {filme['genero']}")
    
    # Teste 8: Colocar filme de volta em cartaz
    if filmes_criados:
        print(f"\n[TEST 8] Colocando '{filmes_criados[0]['titulo']}' em cartaz...")
        filme = controller.colocar_filme_em_cartaz(filmes_criados[0]['id'])
        print(f"  ✓ Filme em cartaz. Status: em_cartaz = {filme['em_cartaz']}")
    
    # Teste 9: Estatísticas
    print("\n[TEST 9] Obtendo estatísticas...")
    stats = controller.obter_estatisticas()
    print(f"  Total de filmes: {stats['total_filmes']}")
    print(f"  Filmes em cartaz: {stats['filmes_em_cartaz']}")
    
    # Teste 10: Validações
    print("\n[TEST 10] Testando validações...")
    
    # Validar título vazio
    try:
        controller.criar_filme("", "Ação", 120, 12, "Sinopse")
        print("  ✗ Validação de título vazio falhou!")
    except ValueError as e:
        print(f"  ✓ Validação de título: {e}")
    
    # Validar duração negativa
    try:
        controller.criar_filme("Filme Teste", "Ação", -120, 12, "Sinopse")
        print("  ✗ Validação de duração negativa falhou!")
    except ValueError as e:
        print(f"  ✓ Validação de duração: {e}")
    
    # Validar filme inexistente
    try:
        controller.obter_filme(99999)
        print("  ✗ Validação de filme inexistente falhou!")
    except ValueError as e:
        print(f"  ✓ Validação de filme inexistente: {e}")
    
    print("\n" + "="*60)
    print("TESTES CONCLUÍDOS COM SUCESSO!")
    print("="*60 + "\n")


if __name__ == "__main__":
    teste_funcionalidades()

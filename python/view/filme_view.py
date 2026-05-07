class FilmeView:
    def __init__(self, controller):
        self.controller = controller

    def exibir_menu(self):
        """Exibe o menu de opções de filmes"""
        print("\n" + "="*50)
        print("GERENCIAMENTO DE FILMES")
        print("="*50)
        print("1. Visualizar todos os filmes")
        print("2. Visualizar filmes em cartaz")
        print("3. Criar novo filme")
        print("4. Atualizar filme")
        print("5. Tirar filme de cartaz")
        print("6. Colocar filme em cartaz")
        print("7. Remover filme")
        print("8. Ver estatísticas")
        print("0. Voltar")
        print("="*50)

    def listar_todos_filmes(self):
        """Exibe todos os filmes cadastrados"""
        filmes = self.controller.obter_todos_filmes()
        
        if not filmes:
            print("\nNenhum filme cadastrado.")
            return
        
        print("\n" + "="*80)
        print("TODOS OS FILMES")
        print("="*80)
        self._exibir_tabela_filmes(filmes)

    def listar_filmes_em_cartaz(self):
        """Exibe apenas os filmes em cartaz"""
        filmes = self.controller.obter_filmes_em_cartaz()
        
        if not filmes:
            print("\nNenhum filme em cartaz no momento.")
            return
        
        print("\n" + "="*80)
        print("FILMES EM CARTAZ")
        print("="*80)
        self._exibir_tabela_filmes(filmes)

    def _exibir_tabela_filmes(self, filmes):
        """Exibe filmes em formato de tabela"""
        print(f"{'ID':<5} {'Título':<35} {'Gênero':<15} {'Duração':<10} {'Cartaz':<7}")
        print("-"*80)
        
        for filme in filmes:
            titulo = filme['titulo'][:32] + "..." if len(filme['titulo']) > 32 else filme['titulo']
            genero = filme['genero'][:12] + "..." if filme['genero'] and len(filme['genero']) > 12 else (filme['genero'] or "N/A")
            duracao = f"{filme['duracao_minutos']}min" if filme['duracao_minutos'] else "N/A"
            cartaz = "Sim" if filme['em_cartaz'] else "Não"
            
            print(f"{filme['id']:<5} {titulo:<35} {genero:<15} {duracao:<10} {cartaz:<7}")
        
        print("-"*80)

    def criar_filme(self):
        """Interface para criar novo filme"""
        print("\n" + "="*50)
        print("CRIAR NOVO FILME")
        print("="*50)
        
        titulo = input("Título: ").strip()
        genero = input("Gênero: ").strip()
        
        while True:
            try:
                duracao = int(input("Duração (minutos): "))
                break
            except ValueError:
                print("Duração deve ser um número inteiro.")
        
        while True:
            try:
                classificacao = int(input("Classificação indicativa (0-18): "))
                if 0 <= classificacao <= 18:
                    break
                print("Classificação deve estar entre 0 e 18.")
            except ValueError:
                print("Classificação deve ser um número inteiro.")
        
        sinopse = input("Sinopse: ").strip()
        
        try:
            filme = self.controller.criar_filme(titulo, genero, duracao, classificacao, sinopse)
            print(f"\n✓ Filme '{titulo}' criado com sucesso! (ID: {filme['id']})")
        except ValueError as e:
            print(f"\n✗ Erro: {e}")

    def atualizar_filme(self):
        """Interface para atualizar filme"""
        self.listar_todos_filmes()
        
        try:
            filme_id = int(input("\nDigite o ID do filme a atualizar: "))
            filme = self.controller.obter_filme(filme_id)
            
            print("\nDeixe em branco para não alterar um campo.")
            titulo = input(f"Novo título ({filme['titulo']}): ").strip() or None
            genero = input(f"Novo gênero ({filme['genero']}): ").strip() or None
            sinopse = input(f"Nova sinopse ({filme['sinopse'][:30]}...): ").strip() or None
            
            kwargs = {}
            if titulo:
                kwargs['titulo'] = titulo
            if genero:
                kwargs['genero'] = genero
            if sinopse:
                kwargs['sinopse'] = sinopse
            
            if kwargs:
                filme = self.controller.atualizar_filme(filme_id, **kwargs)
                print(f"\n✓ Filme atualizado com sucesso!")
            else:
                print("\nNenhum campo foi alterado.")
        except ValueError as e:
            print(f"\n✗ Erro: {e}")

    def tirar_de_cartaz(self):
        """Interface para tirar filme de cartaz"""
        self.listar_filmes_em_cartaz()
        
        try:
            filme_id = int(input("\nDigite o ID do filme a tirar de cartaz: "))
            self.controller.tirar_filme_de_cartaz(filme_id)
            print(f"\n✓ Filme retirado de cartaz com sucesso!")
        except ValueError as e:
            print(f"\n✗ Erro: {e}")

    def colocar_em_cartaz(self):
        """Interface para colocar filme em cartaz"""
        self.listar_todos_filmes()
        
        try:
            filme_id = int(input("\nDigite o ID do filme a colocar em cartaz: "))
            self.controller.colocar_filme_em_cartaz(filme_id)
            print(f"\n✓ Filme colocado em cartaz com sucesso!")
        except ValueError as e:
            print(f"\n✗ Erro: {e}")

    def remover_filme(self):
        """Interface para remover filme"""
        self.listar_todos_filmes()
        
        try:
            filme_id = int(input("\nDigite o ID do filme a remover: "))
            confirmacao = input("Tem certeza? (s/n): ").lower()
            
            if confirmacao == 's':
                self.controller.remover_filme(filme_id)
                print(f"\n✓ Filme removido com sucesso!")
            else:
                print("\nOperação cancelada.")
        except ValueError as e:
            print(f"\n✗ Erro: {e}")

    def exibir_estatisticas(self):
        """Exibe estatísticas sobre filmes"""
        stats = self.controller.obter_estatisticas()
        
        print("\n" + "="*50)
        print("ESTATÍSTICAS DE FILMES")
        print("="*50)
        print(f"Total de filmes: {stats['total_filmes']}")
        print(f"Filmes em cartaz: {stats['filmes_em_cartaz']}")
        print("="*50)

    def run(self):
        """Loop principal da view"""
        while True:
            self.exibir_menu()
            opcao = input("Escolha uma opção: ").strip()
            
            if opcao == "1":
                self.listar_todos_filmes()
            elif opcao == "2":
                self.listar_filmes_em_cartaz()
            elif opcao == "3":
                self.criar_filme()
            elif opcao == "4":
                self.atualizar_filme()
            elif opcao == "5":
                self.tirar_de_cartaz()
            elif opcao == "6":
                self.colocar_em_cartaz()
            elif opcao == "7":
                self.remover_filme()
            elif opcao == "8":
                self.exibir_estatisticas()
            elif opcao == "0":
                print("\nVoltando ao menu principal...")
                break
            else:
                print("\nOpção inválida!")

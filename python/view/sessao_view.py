from datetime import datetime


class SessaoView:
    def __init__(self, controller):
        self.controller = controller

    def solicita_consulta(self):
        print("\n=== SISTEMA DE SESSÕES DE CINEMA ===\n")
        print("Escolha uma opção:")
        print("1. Ver sessão em andamento")
        print("2. Ver todas as sessões em andamento")
        print("3. Ver próximas sessões")
        print("4. Ver todas as sessões")
        print("5. Consultar sessão por ID")
        
        opcao = input("\nDigite a opção (1-5): ").strip()
        
        if opcao == "1":
            self._exibe_sessoes_em_andamento()
        elif opcao == "2":
            self._exibe_todas_em_andamento()
        elif opcao == "3":
            self._exibe_proximas()
        elif opcao == "4":
            self._exibe_todas()
        elif opcao == "5":
            self._consulta_por_id()
        else:
            print("Opção inválida!")
    
    def _exibe_sessoes_em_andamento(self):
        sessoes = self.controller.request_sessoes_em_andamento()
        if "erro" in sessoes:
            print(f"Erro: {sessoes['erro']}")
        elif not sessoes:
            print("Nenhuma sessão em andamento no momento.")
        else:
            print("\n=== SESSÕES EM ANDAMENTO ===\n")
            for sessao in sessoes:
                self._exibe_sessao(sessao)
    
    def _exibe_todas_em_andamento(self):
        sessoes = self.controller.request_sessoes_em_andamento()
        if "erro" in sessoes:
            print(f"Erro: {sessoes['erro']}")
        elif not sessoes:
            print("Nenhuma sessão em andamento no momento.")
        else:
            print("\n=== TODAS AS SESSÕES EM ANDAMENTO ===\n")
            for sessao in sessoes:
                self._exibe_sessao(sessao)
    
    def _exibe_proximas(self):
        sessoes = self.controller.request_proximas_sessoes()
        if "erro" in sessoes:
            print(f"Erro: {sessoes['erro']}")
        elif not sessoes:
            print("Nenhuma próxima sessão agendada.")
        else:
            print("\n=== PRÓXIMAS SESSÕES ===\n")
            for sessao in sessoes:
                self._exibe_sessao(sessao)
    
    def _exibe_todas(self):
        sessoes = self.controller.request_listar_todas()
        if "erro" in sessoes:
            print(f"Erro: {sessoes['erro']}")
        elif not sessoes:
            print("Nenhuma sessão disponível.")
        else:
            print("\n=== TODAS AS SESSÕES ===\n")
            for sessao in sessoes:
                self._exibe_sessao(sessao)
    
    def _consulta_por_id(self):
        sessao_id = int(input("Digite o ID da sessão: "))
        resposta = self.controller.request_consulta_sessao(sessao_id)
        if "erro" in resposta:
            print(f"Erro: {resposta['erro']}")
        else:
            print("\n=== DETALHES DA SESSÃO ===\n")
            self._exibe_sessao(resposta)
    
    def _exibe_sessao(self, sessao):
        print(f"ID: {sessao['id']}")
        print(f"Filme: {sessao['filme']}")
        print(f"Sala: {sessao['sala']}")
        print(f"Horário Início: {sessao['horario_inicio']}")
        print(f"Horário Fim: {sessao['horario_fim']}")
        print(f"Assentos Disponíveis: {sessao['assentos_disponiveis']}/{sessao['assentos_total']}")
        print(f"Status: {sessao['status']}")
        print("-" * 50)

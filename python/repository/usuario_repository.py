from datetime import datetime, timedelta


class SessaoRepository:
    def __init__(self):
        # simulando banco de dados com sessões de cinema
        agora = datetime.now()
        
        self._sessoes = {
            1: {
                "id": 1,
                "filme": "Duna: Parte Dois",
                "sala": 1,
                "horario_inicio": (agora - timedelta(minutes=30)).isoformat(),
                "horario_fim": (agora + timedelta(hours=2, minutes=30)).isoformat(),
                "assentos_total": 100,
                "assentos_disponiveis": 25,
                "status": "em_andamento"
            },
            2: {
                "id": 2,
                "filme": "Capitão América: Sentinela da Liberdade",
                "sala": 2,
                "horario_inicio": (agora + timedelta(minutes=45)).isoformat(),
                "horario_fim": (agora + timedelta(hours=3, minutes=15)).isoformat(),
                "assentos_total": 80,
                "assentos_disponiveis": 40,
                "status": "proxima"
            },
            3: {
                "id": 3,
                "filme": "Insidious: A Porta Vermelha",
                "sala": 3,
                "horario_inicio": (agora - timedelta(hours=1, minutes=15)).isoformat(),
                "horario_fim": (agora + timedelta(hours=1, minutes=15)).isoformat(),
                "assentos_total": 90,
                "assentos_disponiveis": 12,
                "status": "em_andamento"
            },
            4: {
                "id": 4,
                "filme": "Divertida Mente 2",
                "sala": 4,
                "horario_inicio": (agora + timedelta(hours=2)).isoformat(),
                "horario_fim": (agora + timedelta(hours=3, minutes=30)).isoformat(),
                "assentos_total": 110,
                "assentos_disponiveis": 60,
                "status": "proxima"
            },
            5: {
                "id": 5,
                "filme": "Oppenheimer",
                "sala": 5,
                "horario_inicio": (agora - timedelta(hours=3)).isoformat(),
                "horario_fim": (agora).isoformat(),
                "assentos_total": 85,
                "assentos_disponiveis": 0,
                "status": "finalizada"
            },
        }

    def buscar_por_id(self, sessao_id):
        return self._sessoes.get(sessao_id)
    
    def buscar_todas_sessoes(self):
        return list(self._sessoes.values())
    
    def buscar_sessoes_em_andamento(self):
        return [s for s in self._sessoes.values() if s["status"] == "em_andamento"]
    
    def buscar_proximas_sessoes(self):
        return [s for s in self._sessoes.values() if s["status"] == "proxima"]
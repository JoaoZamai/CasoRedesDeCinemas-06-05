from flask import Flask, jsonify, request, render_template_string


class SessaoViewWeb:
    def __init__(self, controller):
        self.app = Flask(__name__)
        self.controller = controller
        self._configurar_rotas()

    def _configurar_rotas(self):
        @self.app.route("/", methods=["GET"])
        def index():
            sessoes = self.controller.request_sessoes_em_andamento()
            html = self._gerar_html_index(sessoes)
            return render_template_string(html)
        
        @self.app.route("/sessoes/<int:sessao_id>", methods=["GET"])
        def consultar_sessao(sessao_id):
            resposta = self.controller.request_consulta_sessao(sessao_id)
            return jsonify(resposta)
        
        @self.app.route("/sessoes/em-andamento", methods=["GET"])
        def sessoes_em_andamento():
            sessoes = self.controller.request_sessoes_em_andamento()
            return jsonify(sessoes)
        
        @self.app.route("/sessoes/proximas", methods=["GET"])
        def proximas_sessoes():
            sessoes = self.controller.request_proximas_sessoes()
            return jsonify(sessoes)
        
        @self.app.route("/sessoes", methods=["GET"])
        def todas_sessoes():
            sessoes = self.controller.request_listar_todas()
            return jsonify(sessoes)

    def _gerar_html_index(self, sessoes):
        sessoes_html = ""
        if not isinstance(sessoes, list):
            sessoes = []
        
        for sessao in sessoes:
            sessoes_html += f"""
            <div class="sessao-card">
                <h3>{sessao['filme']}</h3>
                <p><strong>Sala:</strong> {sessao['sala']}</p>
                <p><strong>Início:</strong> {sessao['horario_inicio']}</p>
                <p><strong>Fim:</strong> {sessao['horario_fim']}</p>
                <p><strong>Assentos:</strong> {sessao['assentos_disponiveis']}/{sessao['assentos_total']} disponíveis</p>
                <p><strong>Status:</strong> <span class="status {sessao['status']}">{sessao['status']}</span></p>
            </div>
            """
        
        # Adiciona salas extras (simuladas)
        salas_extras = [
            {
                'filme': 'Aventura no Espaço',
                'sala': 'Sala 3',
                'horario_inicio': '19:00',
                'horario_fim': '21:15',
                'assentos_disponiveis': 45,
                'assentos_total': 100,
                'status': 'em_andamento'
            },
            {
                'filme': 'Vazio',
                'sala': 'Sala 4',
                'horario_inicio': '-',
                'horario_fim': '-',
                'assentos_disponiveis': 0,
                'assentos_total': 80,
                'status': 'finalizada'
            }
        ]
        
        for sala in salas_extras:
            sessoes_html += f"""
            <div class="sessao-card">
                <h3>{sala['filme']}</h3>
                <p><strong>Sala:</strong> {sala['sala']}</p>
                <p><strong>Início:</strong> {sala['horario_inicio']}</p>
                <p><strong>Fim:</strong> {sala['horario_fim']}</p>
                <p><strong>Assentos:</strong> {sala['assentos_disponiveis']}/{sala['assentos_total']} disponíveis</p>
                <p><strong>Status:</strong> <span class="status {sala['status']}">{sala['status']}</span></p>
            </div>
            """
        
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Cinema Oscar - Sessões em Andamento</title>
            <style>
                * {{
                    margin: 0;
                    padding: 0;
                    box-sizing: border-box;
                }}
                body {{
                    font-family: 'Arial', sans-serif;
                    background: linear-gradient(135deg, #0f0f0f 0%, #1a1a1a 100%);
                    color: #333;
                    min-height: 100vh;
                    padding: 40px 20px;
                }}
                .container {{
                    width: 100%;
                    min-height: 100vh;
                }}
                h1 {{
                    color: #ffd700;
                    text-align: center;
                    margin-bottom: 15px;
                    font-size: 2.5em;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
                }}
                .subtitle {{
                    color: #fff;
                    text-align: center;
                    margin-bottom: 40px;
                    font-size: 1.2em;
                }}
                .scroll-wrapper {{
                    overflow-x: auto;
                    overflow-y: hidden;
                    padding: 20px 0;
                    margin: 0 -20px;
                    padding-left: 20px;
                    padding-right: 20px;
                }}
                .scroll-wrapper::-webkit-scrollbar {{
                    height: 10px;
                }}
                .scroll-wrapper::-webkit-scrollbar-track {{
                    background: #333;
                    border-radius: 10px;
                }}
                .scroll-wrapper::-webkit-scrollbar-thumb {{
                    background: #ffd700;
                    border-radius: 10px;
                }}
                .scroll-wrapper::-webkit-scrollbar-thumb:hover {{
                    background: #ffed4e;
                }}
                .sessoes-grid {{
                    display: flex;
                    gap: 25px;
                    min-width: min-content;
                }}
                .sessao-card {{
                    background: linear-gradient(135deg, #ffffff 0%, #f5f5f5 100%);
                    border-radius: 12px;
                    padding: 25px;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
                    transition: all 0.3s ease;
                    min-width: 320px;
                    border: 3px solid transparent;
                }}
                .sessao-card:hover {{
                    transform: translateY(-8px) scale(1.02);
                    box-shadow: 0 8px 25px rgba(255,215,0,0.4);
                    border-color: #ffd700;
                }}
                .sessao-card h3 {{
                    margin-top: 0;
                    color: #e74c3c;
                    font-size: 1.4em;
                    margin-bottom: 15px;
                }}
                .sessao-card p {{
                    margin: 12px 0;
                    line-height: 1.6;
                }}
                .status {{
                    padding: 8px 15px;
                    border-radius: 6px;
                    font-weight: bold;
                    display: inline-block;
                }}
                .status.em_andamento {{
                    background-color: #2ecc71;
                    color: white;
                }}
                .status.proxima {{
                    background-color: #3498db;
                    color: white;
                }}
                .status.finalizada {{
                    background-color: #95a5a6;
                    color: white;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🎬 Cinema Oscar</h1>
                <div class="subtitle">Sessões em Andamento</div>
                <div class="scroll-wrapper">
                    <div class="sessoes-grid">
                        {sessoes_html}
                    </div>
                </div>
            </div>
        </body>
        </html>
        """

    def run(self):
        self.app.run(debug=True)

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
        
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Cinema - Sessões em Andamento</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 20px;
                    background-color: #1a1a1a;
                    color: #333;
                }}
                .container {{
                    max-width: 1200px;
                    margin: 0 auto;
                }}
                h1 {{
                    color: #fff;
                    text-align: center;
                    margin-bottom: 30px;
                }}
                .sessoes-grid {{
                    display: grid;
                    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
                    gap: 20px;
                }}
                .sessao-card {{
                    background: white;
                    border-radius: 8px;
                    padding: 20px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                    transition: transform 0.3s;
                }}
                .sessao-card:hover {{
                    transform: translateY(-5px);
                    box-shadow: 0 4px 12px rgba(0,0,0,0.2);
                }}
                .sessao-card h3 {{
                    margin-top: 0;
                    color: #e74c3c;
                }}
                .sessao-card p {{
                    margin: 10px 0;
                }}
                .status {{
                    padding: 5px 10px;
                    border-radius: 4px;
                    font-weight: bold;
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
                <h1>🎬 Sessões em Andamento - Cinema</h1>
                <div class="sessoes-grid">
                    {sessoes_html}
                </div>
            </div>
        </body>
        </html>
        """

    def run(self):
        self.app.run(debug=True)
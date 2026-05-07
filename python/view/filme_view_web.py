from flask import Flask, render_template, request, jsonify, redirect, url_for
from repository.filme_repository import FilmeRepository
from service.filme_service import FilmeService
from controller.filme_controller import FilmeController


class FilmeViewWeb:
    def __init__(self, controller):
        self.controller = controller
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        """Configura as rotas da aplicação"""
        
        @self.app.route('/filmes')
        def listar_todos_filmes():
            """Página com todos os filmes"""
            filmes = self.controller.obter_todos_filmes()
            stats = self.controller.obter_estatisticas()
            return render_template('filmes.html', 
                                 filmes=filmes, 
                                 titulo="Todos os Filmes",
                                 stats=stats)

        @self.app.route('/filmes/em-cartaz')
        def filmes_em_cartaz():
            """Página com filmes em cartaz"""
            filmes = self.controller.obter_filmes_em_cartaz()
            stats = self.controller.obter_estatisticas()
            return render_template('filmes.html', 
                                 filmes=filmes, 
                                 titulo="Filmes em Cartaz",
                                 stats=stats,
                                 em_cartaz=True)

        @self.app.route('/filmes/<int:filme_id>')
        def detalhe_filme(filme_id):
            """Página de detalhes de um filme"""
            try:
                filme = self.controller.obter_filme(filme_id)
                return render_template('detalhe_filme.html', filme=filme)
            except ValueError as e:
                return jsonify({'erro': str(e)}), 404

        @self.app.route('/filmes/criar', methods=['GET', 'POST'])
        def criar_filme():
            """Página e lógica para criar novo filme"""
            if request.method == 'POST':
                try:
                    titulo = request.form.get('titulo')
                    genero = request.form.get('genero')
                    duracao = int(request.form.get('duracao_minutos', 0))
                    classificacao = int(request.form.get('classificacao_indicativa', 0))
                    sinopse = request.form.get('sinopse')
                    
                    filme = self.controller.criar_filme(
                        titulo, genero, duracao, classificacao, sinopse
                    )
                    
                    return redirect(url_for('listar_todos_filmes'))
                except ValueError as e:
                    return render_template('criar_filme.html', erro=str(e))
            
            return render_template('criar_filme.html')

        @self.app.route('/api/filmes')
        def api_filmes():
            """API JSON com todos os filmes"""
            filmes = self.controller.obter_todos_filmes()
            return jsonify(filmes)

        @self.app.route('/api/filmes/em-cartaz')
        def api_filmes_em_cartaz():
            """API JSON com filmes em cartaz"""
            filmes = self.controller.obter_filmes_em_cartaz()
            return jsonify(filmes)

        @self.app.route('/api/filmes/<int:filme_id>/cartaz', methods=['POST'])
        def toggle_cartaz(filme_id):
            """API para adicionar/remover filme de cartaz"""
            try:
                acao = request.json.get('acao')
                
                if acao == 'adicionar':
                    filme = self.controller.colocar_filme_em_cartaz(filme_id)
                elif acao == 'remover':
                    filme = self.controller.tirar_filme_de_cartaz(filme_id)
                else:
                    return jsonify({'erro': 'Ação inválida'}), 400
                
                return jsonify({'sucesso': True, 'filme': filme})
            except ValueError as e:
                return jsonify({'erro': str(e)}), 404

        @self.app.route('/api/estatisticas')
        def api_estatisticas():
            """API com estatísticas de filmes"""
            stats = self.controller.obter_estatisticas()
            return jsonify(stats)

    def run(self, debug=True, port=5000):
        """Inicia o servidor web"""
        self.app.run(debug=debug, port=port)

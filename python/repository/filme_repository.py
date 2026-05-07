from database import Database


class FilmeRepository:
    def __init__(self):
        self.db = Database()

    def criar_filme(self, titulo, genero, duracao_minutos, classificacao_indicativa, sinopse, em_cartaz=True):
        """Criar um novo filme no banco de dados"""
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('''
                INSERT INTO filmes (titulo, genero, duracao_minutos, classificacao_indicativa, sinopse, em_cartaz)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (titulo, genero, duracao_minutos, classificacao_indicativa, sinopse, em_cartaz))
            
            conn.commit()
            filme_id = cursor.lastrowid
            return self.buscar_por_id(filme_id)
        finally:
            conn.close()

    def buscar_por_id(self, filme_id):
        """Buscar um filme pelo ID"""
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('SELECT * FROM filmes WHERE id = ?', (filme_id,))
            row = cursor.fetchone()
            return dict(row) if row else None
        finally:
            conn.close()

    def buscar_todos_filmes(self):
        """Retorna todos os filmes do banco de dados"""
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('SELECT * FROM filmes ORDER BY titulo')
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        finally:
            conn.close()

    def buscar_filmes_em_cartaz(self):
        """Retorna apenas os filmes em cartaz"""
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('SELECT * FROM filmes WHERE em_cartaz = 1 ORDER BY titulo')
            rows = cursor.fetchall()
            return [dict(row) for row in rows]
        finally:
            conn.close()

    def atualizar_filme(self, filme_id, **kwargs):
        """Atualizar informações de um filme"""
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        try:
            campos_permitidos = {'titulo', 'genero', 'duracao_minutos', 'classificacao_indicativa', 'sinopse', 'em_cartaz'}
            campos = {k: v for k, v in kwargs.items() if k in campos_permitidos}
            
            if not campos:
                return self.buscar_por_id(filme_id)
            
            set_clause = ', '.join([f'{k} = ?' for k in campos.keys()])
            valores = list(campos.values()) + [filme_id]
            
            cursor.execute(f'''
                UPDATE filmes 
                SET {set_clause}, atualizado_em = CURRENT_TIMESTAMP
                WHERE id = ?
            ''', valores)
            
            conn.commit()
            return self.buscar_por_id(filme_id)
        finally:
            conn.close()

    def deletar_filme(self, filme_id):
        """Deletar um filme do banco de dados"""
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('DELETE FROM filmes WHERE id = ?', (filme_id,))
            conn.commit()
            return True
        finally:
            conn.close()

    def contar_filmes(self):
        """Retorna o total de filmes"""
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('SELECT COUNT(*) as total FROM filmes')
            row = cursor.fetchone()
            return row['total']
        finally:
            conn.close()

    def contar_filmes_em_cartaz(self):
        """Retorna o total de filmes em cartaz"""
        conn = self.db.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute('SELECT COUNT(*) as total FROM filmes WHERE em_cartaz = 1')
            row = cursor.fetchone()
            return row['total']
        finally:
            conn.close()

import sqlite3
import os
from datetime import datetime

DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'cinema.db')


class Database:
    def __init__(self, path=DATABASE_PATH):
        self.path = path
        self.init_database()

    def get_connection(self):
        """Retorna uma conexão com o banco de dados"""
        conn = sqlite3.connect(self.path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_database(self):
        """Inicializa o banco de dados criando as tabelas necessárias"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # Criar tabela de filmes
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS filmes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                genero TEXT,
                duracao_minutos INTEGER,
                classificacao_indicativa INTEGER,
                sinopse TEXT,
                em_cartaz BOOLEAN DEFAULT 1,
                data_inicio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                data_fim TIMESTAMP,
                criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        conn.commit()
        conn.close()

    def close(self):
        """Fecha a conexão com o banco de dados"""
        pass

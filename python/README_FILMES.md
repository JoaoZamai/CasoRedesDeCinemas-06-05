# Sistema de Gerenciamento de Filmes - Cinema

## Descrição

Sistema completo de gerenciamento de filmes para um cinema, com banco de dados SQLite. Permite visualizar todos os filmes cadastrados e filtrar apenas os que estão em cartaz.

## Arquitetura

O projeto segue o padrão **MVC (Model-View-Controller)** com separação em camadas:

```
database.py
    ↓
repository/filme_repository.py (Acesso aos dados)
    ↓
service/filme_service.py (Lógica de negócio)
    ↓
controller/filme_controller.py (Orquestração)
    ↓
view/ (Apresentação - CLI e Web)
```

## Estrutura de Arquivos

```
python/
├── database.py                          # Gerenciamento do banco SQLite
├── repository/
│   └── filme_repository.py             # Repository para filmes
├── service/
│   └── filme_service.py                # Serviço de filmes
├── controller/
│   └── filme_controller.py             # Controller de filmes
├── view/
│   ├── filme_view.py                   # Interface CLI
│   └── filme_view_web.py               # Interface Web (Flask)
├── templates/                          # Templates HTML
│   ├── filmes.html                    # Lista de filmes
│   ├── detalhe_filme.html             # Detalhes do filme
│   └── criar_filme.html               # Formulário de criação
├── scripts/
│   └── popular_filmes.py              # Script para popular BD
└── teste_filmes.py                    # Script de testes
```

## Banco de Dados

### Tabela: `filmes`

```sql
CREATE TABLE filmes (
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
```

## Funcionalidades

### 1. Visualizar Todos os Filmes
Lista todos os filmes cadastrados no banco de dados.

```python
filmes = controller.obter_todos_filmes()
```

### 2. Visualizar Filmes em Cartaz
Filtra apenas os filmes que estão em cartaz (em_cartaz = 1).

```python
filmes_em_cartaz = controller.obter_filmes_em_cartaz()
```

### 3. Criar Novo Filme
Adiciona um novo filme ao banco de dados.

```python
filme = controller.criar_filme(
    titulo="Matrix",
    genero="Ficção Científica",
    duracao_minutos=136,
    classificacao_indicativa=14,
    sinopse="Um hacker descobre a verdade..."
)
```

### 4. Atualizar Filme
Modifica as informações de um filme existente.

```python
filme = controller.atualizar_filme(
    filme_id=1,
    titulo="Novo Título",
    genero="Novo Gênero"
)
```

### 5. Tirar/Colocar em Cartaz
Gerencia o status "em_cartaz" de um filme.

```python
# Tirar de cartaz
controller.tirar_filme_de_cartaz(filme_id=1)

# Colocar em cartaz
controller.colocar_filme_em_cartaz(filme_id=1)
```

### 6. Remover Filme
Deleta um filme do banco de dados.

```python
controller.remover_filme(filme_id=1)
```

### 7. Estatísticas
Obtém informações agregadas sobre filmes.

```python
stats = controller.obter_estatisticas()
# {'total_filmes': 10, 'filmes_em_cartaz': 8}
```

## Como Usar

### 1. Inicializar o Banco de Dados

O banco é criado automaticamente na primeira execução. Um arquivo `cinema.db` será criado no diretório `python/`.

### 2. Popular com Dados Iniciais

```bash
cd python
python scripts/popular_filmes.py
```

Isso criará 8 filmes de exemplo no banco de dados.

### 3. Executar Testes

```bash
python teste_filmes.py
```

Executa uma bateria de testes para validar todas as funcionalidades.

### 4. Interface CLI

```python
from repository.filme_repository import FilmeRepository
from service.filme_service import FilmeService
from controller.filme_controller import FilmeController
from view.filme_view import FilmeView

repository = FilmeRepository()
service = FilmeService(repository)
controller = FilmeController(service)
view = FilmeView(controller)

view.run()  # Inicia o menu interativo
```

### 5. Interface Web

```python
from repository.filme_repository import FilmeRepository
from service.filme_service import FilmeService
from controller.filme_controller import FilmeController
from view.filme_view_web import FilmeViewWeb

repository = FilmeRepository()
service = FilmeService(repository)
controller = FilmeController(service)
view = FilmeViewWeb(controller)

view.run(debug=True, port=5000)
```

Acesse `http://localhost:5000/filmes` no navegador.

## Endpoints da API Web

### Lista
- `GET /filmes` - Todos os filmes
- `GET /filmes/em-cartaz` - Filmes em cartaz
- `GET /filmes/<id>` - Detalhes de um filme

### Criar
- `GET /filmes/criar` - Formulário
- `POST /filmes/criar` - Criar novo filme

### APIs JSON
- `GET /api/filmes` - JSON com todos os filmes
- `GET /api/filmes/em-cartaz` - JSON com filmes em cartaz
- `GET /api/estatisticas` - JSON com estatísticas
- `POST /api/filmes/<id>/cartaz` - Toggle cartaz

## Validações

- **Título**: Obrigatório e não pode estar vazio
- **Duração**: Deve ser maior que 0 minutos
- **Classificação**: Deve estar entre 0 e 18 anos
- **Filme não encontrado**: Validação de ID existente

## Exemplo de Uso Completo

```python
# Inicializar
from repository.filme_repository import FilmeRepository
from service.filme_service import FilmeService
from controller.filme_controller import FilmeController

repo = FilmeRepository()
service = FilmeService(repo)
controller = FilmeController(service)

# Criar filme
filme = controller.criar_filme(
    "Avatar",
    "Ficção Científica",
    162,
    12,
    "Uma aventura em um mundo alienígena"
)

# Listar em cartaz
em_cartaz = controller.obter_filmes_em_cartaz()
print(f"Filmes em cartaz: {len(em_cartaz)}")

# Remover de cartaz
controller.tirar_filme_de_cartaz(filme['id'])

# Atualizar
filme = controller.atualizar_filme(filme['id'], titulo="Avatar - Edição Estendida")

# Colocar de volta
controller.colocar_filme_em_cartaz(filme['id'])

# Estatísticas
stats = controller.obter_estatisticas()
print(f"Total: {stats['total_filmes']}, Em Cartaz: {stats['filmes_em_cartaz']}")
```

## Banco de Dados

O banco SQLite é armazenado em:
```
python/cinema.db
```

Para visualizar ou manipular diretamente:
```bash
sqlite3 python/cinema.db
sqlite> SELECT * FROM filmes;
```

## Dependências

- Python 3.6+
- SQLite3 (incluído no Python)
- Flask (para interface web)

## Instalação de Dependências

```bash
pip install flask
```

## Notas

- O sistema valida automaticamente todas as entradas
- Todas as datas são armazenadas em UTC
- Filmes em cartaz têm `em_cartaz = 1`
- O banco é persistente - os dados não são perdidos ao fechar a aplicação

# Sistema de Sessões de Cinema

Sistema simples para visualizar sessões em andamento em um cinema.

## Estrutura do Projeto

```
python/
├── main.py                          # Aplicação CLI (terminal)
├── app.py                           # Aplicação Web (Flask)
├── repository/
│   ├── __init__.py
│   ├── usuario_repository.py        # (legado)
│   └── sessao_repository.py         # Gerencia dados de sessões
├── service/
│   ├── __init__.py
│   ├── usuario_service.py           # (legado)
│   └── sessao_service.py            # Lógica de negócio de sessões
├── controller/
│   ├── __init__.py
│   ├── usuario_controller.py        # (legado)
│   └── sessao_controller.py         # Controlador de sessões
└── view/
    ├── __init__.py
    ├── usuario_view.py              # (legado)
    ├── usuario_view_web.py          # (legado)
    ├── sessao_view.py               # Interface CLI
    └── sessao_view_web.py           # Interface Web
```

## Como Usar

### Interface CLI (Terminal)

Para executar a aplicação em modo terminal:

```bash
python main.py
```

Opções disponíveis:
1. Ver sessão em andamento
2. Ver todas as sessões em andamento
3. Ver próximas sessões
4. Ver todas as sessões
5. Consultar sessão por ID

### Interface Web

Para executar a aplicação web:

```bash
python app.py
```

Endpoints disponíveis:
- `http://localhost:5000/` - Página inicial com sessões em andamento
- `http://localhost:5000/sessoes` - Todas as sessões (JSON)
- `http://localhost:5000/sessoes/em-andamento` - Apenas em andamento (JSON)
- `http://localhost:5000/sessoes/proximas` - Próximas sessões (JSON)
- `http://localhost:5000/sessoes/<id>` - Detalhes de uma sessão específica (JSON)

## Dados de Exemplo

O sistema vem pré-carregado com 5 sessões de exemplo:

1. **Duna: Parte Dois** - Sala 1 - EM ANDAMENTO
   - Horário: há 30 minutos atrás até +2h30min
   - Assentos: 25/100 disponíveis

2. **Capitão América: Sentinela da Liberdade** - Sala 2 - PRÓXIMA
   - Horário: +45 minutos até +3h15min
   - Assentos: 40/80 disponíveis

3. **Insidious: A Porta Vermelha** - Sala 3 - EM ANDAMENTO
   - Horário: 1h15min atrás até +1h15min
   - Assentos: 12/90 disponíveis

4. **Divertida Mente 2** - Sala 4 - PRÓXIMA
   - Horário: +2 horas até +3h30min
   - Assentos: 60/110 disponíveis

5. **Oppenheimer** - Sala 5 - FINALIZADA
   - Horário: 3 horas atrás até agora
   - Assentos: 0/85 disponíveis

## Status das Sessões

- **em_andamento**: Sessão ativa, filme está sendo exibido
- **proxima**: Sessão agendada para em breve
- **finalizada**: Sessão já terminou

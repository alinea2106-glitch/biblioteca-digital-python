# Biblioteca Digital em Python

Este projeto é um sistema simples de gerenciamento de documentos para uma biblioteca digital.

## Funcionalidades
- Listar documentos por tipo e ano
- Adicionar novos documentos
- Renomear documentos existentes
- Remover documentos

## Estrutura do projeto
- src/ → código principal (main.py)
- tests/ → testes automatizados
- docs/ → relatórios e documentação
- CONTRIBUTING.md → guia de contribuição

## Como usar
1. Clone o repositório:
   git clone https://github.com/alinea2106-glitch/biblioteca-digital-python
   cd biblioteca-digital-python

2. Execute os comandos:
   python src/main.py listar
   python src/main.py adicionar --arquivo exemplo.pdf
   python src/main.py renomear --arquivo exemplo.pdf --novo_nome novo.pdf
   python src/main.py remover --arquivo novo.pdf

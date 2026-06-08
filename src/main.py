import os
from pathlib import Path
import argparse

# Função para listar documentos
def listar_documentos(base_dir="documentos"):
    arquivos = {}
    for root, _, files in os.walk(base_dir):
        for file in files:
            ext = Path(file).suffix
            ano = Path(root).name if Path(root).name.isdigit() else "Desconhecido"
            arquivos.setdefault(ext, {}).setdefault(ano, []).append(file)
    return arquivos

# Função para adicionar documento
def adicionar_documento(caminho, destino="documentos"):
    Path(destino).mkdir(parents=True, exist_ok=True)
    os.rename(caminho, os.path.join(destino, os.path.basename(caminho)))

# Função para renomear documento
def renomear_documento(caminho_antigo, novo_nome):
    os.rename(caminho_antigo, novo_nome)

# Função para remover documento
def remover_documento(caminho):
    os.remove(caminho)

# Interface de linha de comando
parser = argparse.ArgumentParser(description="Sistema de Gerenciamento da Biblioteca Digital")
parser.add_argument("acao", choices=["listar", "adicionar", "renomear", "remover"])
parser.add_argument("--arquivo", help="Caminho do arquivo")
parser.add_argument("--novo_nome", help="Novo nome para renomear")

args = parser.parse_args()

if args.acao == "listar":
    print(listar_documentos())
elif args.acao == "adicionar":
    adicionar_documento(args.arquivo)
elif args.acao == "renomear":
    renomear_documento(args.arquivo, args.novo_nome)
elif args.acao == "remover":
    remover_documento(args.arquivo)

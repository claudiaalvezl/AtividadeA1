from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
NOME_ARQUIVO = 'livros.json'

def ler_dados():
    if not os.path.exists(NOME_ARQUIVO):
        return []
    with open(NOME_ARQUIVO, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_dados(dados):
    with open(NOME_ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# 1. Listar todos os livros - READ -
@app.route('/livros', methods=['GET'])
def listar_livros():
    return jsonify(ler_dados()), 200

# 2. Cadastrar novo livro - CREATE -
@app.route('/livros', methods=['POST'])
def cadastrar_livro():
    novo_livro = request.get_json()
    dados = ler_dados()
    novo_id = dados[-1]['id'] + 1 if dados else 1
    novo_livro['id'] = novo_id
    dados.append(novo_livro)
    salvar_dados(dados)
    return jsonify(novo_livro), 201

# 3. Atualizar um livro - UPDATE -
@app.route('/livros/<int:id>', methods=['PUT'])
def atualizar_livro(id):
    dados = ler_dados()
    livro_atualizado = request.get_json()
    for i, livro in enumerate(dados):
        if livro['id'] == id:
            dados[i].update(livro_atualizado)
            dados[i]['id'] = id
            salvar_dados(dados)
            return jsonify(dados[i]), 200
    return jsonify({"erro": "Livro não encontrado"}), 404

# 4. Remover um livro - DELETE - 
@app.route('/livros/<int:id>', methods=['DELETE'])
def excluir_livro(id):
    dados = ler_dados()
    novos_dados = [l for l in dados if l['id'] != id]
    if len(novos_dados) < len(dados):
        salvar_dados(novos_dados)
        return jsonify({"mensagem": "Livro removido com sucesso"}), 200
    return jsonify({"erro": "Livro não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
# Documentação da API de Livros

Esta API permite o gerenciamento completo de um acervo de livros via JSON.

## Endpoints Disponíveis:

* *Listar Livros (GET):* http://127.0.0.1:5000/livros
* *Cadastrar Livro (POST):* http://127.0.0.1:5000/livros
  * Exemplo de corpo: {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
* *Atualizar Livro (PUT):* http://127.0.0.1:5000/livros/<id>
* *Excluir Livro (DELETE):* http://127.0.0.1:5000/livros/<id>
*
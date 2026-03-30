O projeto consiste em uma API robusta desenvolvida com *Python* e o framework *Flask* para o gerenciamento de uma biblioteca digital.
A aplicação permite realizar todas as operações de um CRUD (Create, Read, Update, Delete), utilizando um arquivo *JSON* como persistência de dados.

## Funcionalidades da API

A API expõe os seguintes endpoints para manipulação do acervo de livros:

| Operação - Método - Endpoint - Descrição
| :------ - :------ - :------ - :------ 
| *Listar* - GET - /livros - Retorna a lista completa de livros no acervo.
| *Cadastrar* - POST - /livros - Adiciona um novo título ao arquivo JSON.
| *Atualizar* - PUT - /livros/<id> - Modifica as informações de um livro existente.
| *Excluir* - DELETE - /livros/<id> - Remove um registro do acervo permanentemente.

## Tecnologias e Ferramentas

* *Linguagem:* Python 3.x
* *Framework Web:* Flask
* *Armazenamento:* JSON (Persistência em arquivo local)
* *Editor:* Visual Studio Code

## Como Configurar e Rodar o Projeto

Siga os passos abaixo para executar a aplicação em sua máquina local:

### 1. Instalação das Dependências
Certifique-se de ter o Python instalado. No terminal do VS Code, instale o Flask:
``` Digite 
pip install flask

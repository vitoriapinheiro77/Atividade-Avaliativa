# Atividade Avaliativa - CRUD com MongoDB e Python

Este projeto é uma atividade que simula as operações de CRUD (Create, Read, Update, Delete) usando MongoDB em um container Docker e a biblioteca pymongo no Python. O tema escolhido foi um cardápio de restaurante para tornar o exercício prático e divertido.

# Tecnologias utilizadas
- Python 3
- MongoDB (rodando no Docker)
- Biblioteca pymongo

# Como rodar o projeto

# 1. Clonar o repositório

git clone git@github.com:vitoriapinheiro77/Atividade-Avaliativa.git
cd Atividade-avaliativa

# 2. Subir o MongoDB no Docker

docker run -d --name mongo-restaurante -p 27017:27017 mongo

# 3. Criar e ativar a virtualenv (opcional)

python -m venv venv
venv\Scripts\activate - no Windows

# 4. Instalar dependências

pip install pymongo

# 5. Rodar o código

python cardapio.py

#  O QUE O CODIGO FAZ?

O código crud_cardapio.py realiza:

CREATE: insere itens no cardápio (ex: Pizza e Suco).

READ: lista todos os itens do cardápio.

UPDATE: atualiza o preço de um item.

DELETE: remove um item do cardápio.



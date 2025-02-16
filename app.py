#importar biblioteca
from flask import Flask, request, jsonify

"""
Esse código se basa em um aplicação API simples usando Framework Flask. Nele, são
criadas duas requisições, a primeira tipo get e a segunda tipo post. A primeira
criar um endpoint http://127.0.0.1:5000 com extensão /hello, que retorna uma saudação
do desenvolvedor deste código. A segunda, cria um endpoint http://127.0.0.1:5000 com extensão
/numeros que envia o a soma de dos números em formato json. Nessa funçao se selecionam todos
os valores no dos dados json, faz a soma e envia o resultado também em formato json.
Essa função possui rotinas de revisão de error esperados ou inesparados para a requisição.
"""

# Argumento da app
app = Flask(__name__)


@app.get("/hello")   # Endpoint >> http://127.0.0.1:5000/hello
def greatings():     # Função de busca do enpoint que retorna uma saudação.
    return "Olá, sou Carlos"  # Retorna essa mensagem quando é usado um browser http://127.0.0.1:5000/hello


@app.post("/numeros")  # Endpoint >> http://127.0.0.1:5000/numeros
def sum_numbers():     # Função de envio de dos números que são somados.
    try:               # Try analiza algum error de formato no json.
        # Request dados json
        numbers = request.get_json()
        
        # Soma os numeros
        soma = sum(numbers.values())
        return jsonify({"Resultado da soma:": soma}), 201
    
    except Exception as e:   #  Armazena um erro inesperado e muestra.
        return jsonify({"formato invalido": str(e)}), 400
    
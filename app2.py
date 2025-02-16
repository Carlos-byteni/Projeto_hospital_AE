from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

"""
Esse código se basa em um aplicação de requisição de envio de dados formato json
a través da rota http://127.0.0.1:5002//login. Aqui é necesário digitar corretamente
os dados do usuário e o password. Se os dados são enviados corretamente, o código envia
um toke de segurança JWT, uma vez gerado o token, o usuário deverá inseri-lo no
cabeçalho do Header na requisição Get da rota protegida. Uma vez esse token inserido
no cabeçalho, o usuário pode ser logado no sistema. O código possui algumas verificações
de eventuais errors nas requisição dos dados json.
"""

app2 = Flask(__name__)

app2.config['SECRET_KEY'] = "c96d59374eff48e3a78d100cc496ea08"
jwt = JWTManager(app2)

@app2.route('/login', methods=['POST'])
def login():
    try:
        # São obtidos os valores do json. 
        username = request.json.get('username', None)
        password = request.json.get('password', None)

        # Verifica se dados json que contem informação.
        if not username:
            return "Falta infomação usuario", 400
        if not password:
            return "Falta informação password", 400
        
        if username == 'admin' and password == '1234':
            # Use-se "create_access_toke para identificar o usuário com o token gerado."
            token_acesso = create_access_token(identity=username)
            # Retorna o token.
            return jsonify(token_acesso=token_acesso), 200
        return jsonify({"msg":"Acesso negado"}), 401
    
    except AttributeError:
        return "informacao incompleta", 400
       
@app2.route("/secret", methods=["GET"])
# @jwt_required() protege "/secret", permite que o usuário envie o token no cabeçalho de requisição.
@jwt_required()
def secret():
    # Identifica o usuário a partir de jwt token enviado.
    user = get_jwt_identity()  
    print(user)
    # Retorna o nome do usuário logado (admin) quando usado o token.
    return jsonify(logado_como=user), 200

if __name__ == '__main__':
    app2.run(debug=True, port=5002)

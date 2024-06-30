from flask import Flask, jsonify, request

app = Flask(__name__)

celulares = [
    {
        'id': 1,
        'modelo': 'iPhone 13',
        'marca': 'Apple',
        'data_lancamento': '2021-09-24'
    },
    {
        'id': 2,
        'modelo': 'Galaxy S21',
        'marca': 'Samsung',
        'data_lancamento': '2021-01-29'
    },
    {
        'id': 3,
        'modelo': 'Pixel 6',
        'marca': 'Google',
        'data_lancamento': '2021-10-28'
    },
    {
        'id': 4,
        'modelo': 'OnePlus 9',
        'marca': 'OnePlus',
        'data_lancamento': '2021-03-23'
    },
    {
        'id': 5,
        'modelo': 'Xperia 1 III',
        'marca': 'Sony',
        'data_lancamento': '2021-08-19'
    }, 
    {
        'id': 6,
        'modelo': 'Mi 11',
        'marca': 'Xiaomi',
        'data_lancamento': '2021-01-01'
    },
    {
        'id': 7,
        'modelo': 'Moto G100',
        'marca': 'Motorola',
        'data_lancamento': '2021-04-20'
    },
]

# Consultar todos os celulares
@app.route('/celulares', methods=['GET'])
def obter_celulares():
    return jsonify({'celulares': celulares}), 200

# Consultar celular por id
@app.route('/celulares/<int:id>', methods=['GET'])
def obter_celular_por_id(id):
    celular = next((celular for celular in celulares if celular['id'] == id), None)
    if celular:
        return jsonify(celular), 200
    return jsonify({'erro': 'Celular não encontrado'}), 404

# Editar celular por id
@app.route('/celulares/<int:id>', methods=['PUT'])
def editar_celular_por_id(id):
    celular_alterado = request.get_json()
    celular = next((celular for celular in celulares if celular['id'] == id), None)
    if celular:
        celular.update(celular_alterado)
        return jsonify(celular), 200
    return jsonify({'erro': 'Celular não encontrado'}), 404

# Incluir novo celular
@app.route('/celulares', methods=['POST'])
def incluir_novo_celular():
    novo_celular = request.get_json()
    if not novo_celular.get('modelo') or not novo_celular.get('marca') or not novo_celular.get('data_lancamento'):
        return jsonify({'erro': 'Dados inválidos'}), 400
    novo_celular['id'] = len(celulares) + 1
    celulares.append(novo_celular)
    return jsonify(novo_celular), 201

# Excluir celular por id
@app.route('/celulares/<int:id>', methods=['DELETE'])
def excluir_celular(id):
    celular = next((celular for celular in celulares if celular['id'] == id), None)
    if celular:
        celulares.remove(celular)
        return jsonify({'mensagem': 'Celular excluído com sucesso'}), 200
    return jsonify({'erro': 'Celular não encontrado'}), 404

# Tratamento de erro para rotas não encontradas
@app.errorhandler(404)
def pagina_nao_encontrada(e):
    return jsonify({'erro': 'Página não encontrada'}), 404

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)

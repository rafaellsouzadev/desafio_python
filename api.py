from flask import Flask, jsonify, request, make_response, abort
from database import db
from model.filme import FILMES, FILMESEncoder
from flask_cors import CORS

app =Flask(__name__)
app.config['DEBUG']=True
app.json_encoder = FILMESEncoder
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(request):
    return make_response(jsonify({'Status': 404, 'Error': 'Resource not found'}), 404)


@app.route('/', methods=['GET'])
def home():
    return (
        '<h1>Desafio Infinity School</h1>'
        '<p>Desenvolvido por: Rafael de Souza Alves</p>'
    )

@app.route('/api/v1/resource/filmes', methods=['GET'])
def lists():
    return jsonify({'Filmes': db})



#print(db[0].nome)
t1 = 0.0
t2 = 0.0
t3 = 0.0
t4 = 0.0
for n in db:
    t1 = n
    for y in db:
        t2 = y
        for a in db:
           t3 = a
           for b in db:
             t4 = b
    if (t1.tempo + t2.tempo) < 3.0 or (t3.tempo + t4.tempo) < 3.0:
        print(f"Tempo: {t1.tempo} nome: {t1.nome}")
    elif (t1.tempo + t2.tempo) > 3.0 or (t3.tempo + t4.tempo) > 3.0:
        print(f"Tempo maior que 3.0: {t1.tempo} nome: {t1.nome}")


app.run()
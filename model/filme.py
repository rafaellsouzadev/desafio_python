from flask.json import JSONEncoder

class FILMES(object):
    id = 1

    def __init__(self, nome, tempo,):
        self.nome = nome
        self.tempo = tempo
        self.id = FILMES.id
        FILMES.id += 1

class FILMESEncoder(JSONEncoder):
    def default(self, obj):
         if isinstance(obj, FILMES):
             return obj.__dict__
         return super(FILMESEncoder, self).default(obj)

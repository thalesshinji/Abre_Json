import json

class Abre_Json:

    def __init__(self, caminho):

        self.caminho = caminho

    def apenas_le_json_retorna_lista_python(self):

        with open(self.caminho, 'r', encoding = 'utf-8') as f:

            data = json.load(f)

            print(type(data))

            return data
    
    def le_json_retorna_string_de_json(self, indentacao):

        with open(self.caminho, 'r') as f:
            
            data = json.load(f)

            content = json.dumps(data, indent= indentacao)

            print(type(content))

            return content
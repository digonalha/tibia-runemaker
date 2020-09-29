import json


class Config():
    data = {}

    def get(self):
        try:
            with open('config.txt') as json_file:
                return json.load(json_file)
        except:
            return []

    def create(self, new_config):
        data['config'] = self.get()
        data['config'].append(new_config)

        with open('config.txt', 'w') as outfile:
            json.dump(data, outfile)

    def list_config(self):
        try:
            print('#. Configuraçoes:\n0. Criar nova')
            with open('config.txt') as json_file:
                order = 0
                data = json.load(json_file)
                for p in data['config']:
                    order += 1
                    print(str(order) + '. Character: ' + p['name'])
        except:
            print('Ocorreu um erro ao tentar carregar as configurações')
        finally:
            input(':: ')

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
            print('#. Configuraçoes:')
            with open('config.txt') as json_file:
                data = json.load(json_file)
                for p in data['people']:
                    print('Name: ' + p['name'])
                    print('Website: ' + p['website'])
                    print('From: ' + p['from'])
                    print('')
        except:
            return
        finally:
            print('0. Criar nova')
            input(':: ')

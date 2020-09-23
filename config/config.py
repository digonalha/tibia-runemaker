import json


class Config():
    def get(self):
        try:
            with open('config.txt') as json_file:
                return json.load(json_file)
        except:
            return []

    def create(self, new_config):
        data = {}
        data['config'] = self.get()
        data['config'].append(new_config)

        with open('config.txt', 'w') as outfile:
            json.dump(data, outfile)

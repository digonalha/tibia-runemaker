import datetime
import psutil
import subprocess
import re
import platform
import numpy
import pygetwindow
import os
import json
import uuid
from dotenv import load_dotenv


load_dotenv()

PROCNAME = 'client.exe'
client_path = os.getenv('CLIENT_PATH')
character_name = os.getenv('CHARACTER_NAME')


class Tools:
    def is_time_between(self):
        """retorna verdadeiro se o horario for entre 06:10 AM e 5:55AM (evitando o server save dos servers BR)"""
        now_time = datetime.datetime.now().time()
        start = datetime.time(6, 10)
        end = datetime.time(5, 55)
        if now_time >= start or now_time <= end:
            return True
        else:
            return False

    def check_is_opened(self):
        for proc in psutil.process_iter():
            if proc.name() == PROCNAME:
                return True
        return False

    def is_tibia_focused(self):
        try:
            if (platform.system() == 'Windows'):
                win = pygetwindow.getWindowsWithTitle('Tibia')
                if (win):
                    win[0].activate()
                    return True
                else:
                    return False
        except:
            return False

    def open_tibia_if_closed(self):
        if (not self.check_is_opened()):
            print('- opening client.')
            os.startfile(client_path + '/Tibia.exe')

    def set_tibia_renderer(self):
        filename = client_path + 'packages\Tibia\conf\clientoptions.json'
        with open(filename, 'r') as f:
            data = json.load(f)
            options = data['options']
            options['rendererIndex'] = 3   # remove remaining part
            options['frameRateLimit'] = 10
            # options['rendererChangeConfirmationRequired'] = 'true'

        os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def exit_handler(self):
        self.kill_tibia_process()
        filename = client_path + 'packages\Tibia\conf\clientoptions.json'
        with open(filename, 'r') as f:
            data = json.load(f)
            options = data['options']
            options['rendererIndex'] = 0   # remove remaining part
            options['frameRateLimit'] = 130
            # options['rendererChangeConfirmationRequired'] = 'true'

        os.remove(filename)
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

        self.open_tibia_if_closed()

    def kill_tibia_process(self):
        for proc in psutil.process_iter():
            if (proc.name() == PROCNAME):
                proc.kill()

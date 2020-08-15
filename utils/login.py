# -*- coding: utf-8 -*-
import base64
import struct
import hmac
import hashlib
import time
from dotenv import load_dotenv

from .tools import Tools
from .gamewindow import GameWindow
from .keyboard import Keyboard
import os

load_dotenv()

tools = Tools()
gamewindow = GameWindow()
keyboard = Keyboard()

password = os.getenv('PASSWORD')
auth_token = os.getenv('AUTH_TOKEN')
character_name = os.getenv('CHARACTER_NAME')


class Login:
    def get_hotp(self, secret, intervals_no):
        key = base64.b32decode(secret, True)
        msg = struct.pack(">Q", intervals_no)
        h = hmac.new(key, msg, hashlib.sha1).digest()
        o = h[19] & 15
        h = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000
        return h

    def get_totp(self, secret):
        return self.get_hotp(secret, intervals_no=int(time.time())//30)

    def get_auth_token(self, secret):
        try:
            return str(self.get_totp(secret)).zfill(6)
        except:
            print('Erro no método get_auth_token')

    def start_login(self):
        # open_tibia_if_closed()
        tools.is_tibia_focused()
        gamewindow.set_chat_off()

        if (gamewindow.check_offline()):
            keyboard.press_esc(3)
            time.sleep(3)
            keyboard.type(password)

            time.sleep(2)
            keyboard.press_enter()

            time.sleep(5)
            keyboard.type(self.get_auth_token(auth_token))

            time.sleep(2)
            keyboard.press_enter()

            time.sleep(5)
            print(character_name)
            keyboard.type(character_name)
            time.sleep(1)
            keyboard.press_enter()

            time.sleep(4)
            if (gamewindow.check_offline()):
                self.start_login()
        else:
            pass

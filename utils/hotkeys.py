from .keyboard import Keyboard, Key
from pynput.keyboard import Controller
from .tools import Tools
import time

kbc = Controller()
keyboard = Keyboard()
tools = Tools()


class Hotkeys():
    def rotate_char(self):
        with kbc.pressed(Key.ctrl):
            keyboard.press_key(Key.right)
            keyboard.press_key(Key.left)

    def send_msg(self, msg=str):
        keyboard.type(msg)
        time.sleep(0.5)
        keyboard.press_key(Key.enter)

    def open_npc_chat(self):
        with kbc.pressed(Key.shift):
            keyboard.press_key('n')

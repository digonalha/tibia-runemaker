from pynput.keyboard import Key, Controller
import time

kbc = Controller()


class Keyboard:
    def press_key(self, key):
        time.sleep(0.219)
        kbc.press(key)
        time.sleep(0.231)
        kbc.release(key)

    def press_esc(self, qtd=1):
        for i in range(0, qtd):
            self.press_key(Key.esc)

    def press_enter(self):
        self.press_key(Key.enter)

    def type(self, string):
        kbc.type(string)

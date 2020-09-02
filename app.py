#!/usr/bin/env python3

import time
import os

from utils.login import Login
from utils.tools import Tools
from utils.gamewindow import GameWindow
from utils.hotkeys import Hotkeys


tools = Tools()
gamewindow = GameWindow()
login = Login()
hotkeys = Hotkeys()


class App():
    def runemaker(self):
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(
                'starting runemaker.\nsource code: https://github.com/digonalha/tibia-runemaker\n')
            make_arrow = input(
                '1. Make arrows\n2. Make runes\n\nSelect: ') == '1'

            x = 0
            tools.open_tibia_if_closed()
            login.start_login()

            gamewindow.set_chat_off()
            gamewindow.close_all_windows()
            gamewindow.show_equips()

            self.check_supplies()
            self.default_action()

            while (True):
                gamewindow.set_chat_off()
                if (tools.is_time_between()):
                    self.cast_spell(make_arrow)

                    if (x % 4 == 0):
                        login.start_login()
                        self.check_supplies()
                    if (x > 10):
                        self.default_action()
                        x = 0

                    x += 1
                    time.sleep(5)
        except:
            raise

    def cast_spell(self, make_arrow):
        if (make_arrow):
            gamewindow.check_diamond_arrow()
        else:
            gamewindow.check_avalanche()

    def check_supplies(self):
        gamewindow.check_food_and_blank_runes()
        gamewindow.check_softboots()
        gamewindow.check_lifering()

    def default_action(self):
        gamewindow.drop_runes()
        hotkeys.rotate_char()
        gamewindow.eat()


app = App()

if (__name__ == "__main__"):
    app.runemaker()

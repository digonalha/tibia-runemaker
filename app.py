#!/usr/bin/env python3

from utils.login import Login
from utils.tools import Tools
from utils.gamewindow import GameWindow
from utils.hotkeys import Hotkeys
import time

tools = Tools()
gamewindow = GameWindow()
login = Login()
hotkeys = Hotkeys()


class App():
    def runemaker(self):
        try:
            print(
                'starting runemaker by digonalha. https://github.com/digonalha/tibia-runemaker')
            x = 0
            login.start_login()

            gamewindow.set_chat_off()
            gamewindow.close_all_windows()
            gamewindow.show_equips()

            self.check_supplies()
            self.default_action()

            while (True):
                gamewindow.set_chat_off()
                if (tools.is_time_between()):
                    gamewindow.check_avalanche()

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

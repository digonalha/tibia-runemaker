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
            tools.set_tibia_renderer()
            tools.open_tibia_if_closed()

            cast_spell = self.print_cabecalho()

            x = 0
            global character_name
            login.start_login(character_name)

            gamewindow.set_chat_off()
            gamewindow.close_all_windows()
            gamewindow.show_equips()

            self.check_supplies()
            self.default_action()

            while (True):
                gamewindow.set_chat_off()
                if (tools.is_time_between()):
                    self.cast_spell(cast_spell)

                    if (x % 4 == 0):
                        login.start_login(character_name)
                        self.check_supplies()
                    if (x > 10):
                        self.default_action()
                        x = 0

                    x += 1
                    time.sleep(5)
        except:
            raise

    def print_cabecalho(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(
            'iniciando runemaker.\ncodigo-fonte: https://github.com/digonalha/tibia-runemaker\n')
        global character_name
        character_name = input(
            '#. Nome do personagem: ')

        make_arrow = input(
            '1. fazer diamond arrows\n2. fazer spectral bolts\n3. fazer avalanches\n\nselecione (1, 2 ou 3): ')

        return make_arrow

    def cast_spell(self, cast_spell):
        opt = int(cast_spell)
        if (opt == 1):
            gamewindow.check_arrow_or_bolt(
                'diamond_with_mana.png', 'diamond_without_mana.png')
        elif (opt == 2):
            gamewindow.check_arrow_or_bolt(
                'spectral_with_mana.png', 'spectral_without_mana.png')
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

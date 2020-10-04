#!/usr/bin/env python3

from utils.hotkeys import Hotkeys
from utils.gamewindow import GameWindow
from utils.tools import Tools
from utils.login import Login
from config.config import Config
import time
import os
import threading


tools = Tools()
gamewindow = GameWindow()
login = Login()
hotkeys = Hotkeys()
config = Config()


class App():
    def main(self):
        try:
            x = 0
            exit_request = False
            global character_name, spell_to_use, exit_request

            # config.list_config()

            tools.set_tibia_renderer()
            tools.open_tibia_if_closed()

            cast_spell = self.print_cabecalho()
            login.start_login(character_name)
            gamewindow.close_all_windows()
            gamewindow.show_equips()

            while (not exit_request):
                gamewindow.set_chat_off()

                if (tools.is_time_between()):
                    self.cast_spell(spell_to_use)

                    if (x % 4 == 0):
                        tools.open_tibia_if_closed()
                        login.start_login(character_name)
                        self.check_supplies()
                    if (x > 10):
                        tools.open_tibia_if_closed()
                        self.default_action()
                        x = 0

                    x += 1
                    time.sleep(5)
        except BaseException as e:
            print('\nOcorreu um erro: ' + e.message)
        finally:
            restart_tibia = input(
                '\nDeseja abrir o tibia com o render correto? y/n: ') == 'y'
            if (restart_tibia):
                tools.exit_handler()

    def print_cabecalho(self):
        global character_name, spell_to_use, use_ring, use_soft, buy_supply, force_focus
        os.system('cls' if os.name == 'nt' else 'clear')
        print(
            'iniciando runemaker.\ncodigo-fonte: https://github.com/digonalha/tibia-runemaker\n')

        character_name = input('#. Nome do personagem: ')
        use_ring = input(
            '#. Usar life ring? y/n: ') == 'y'
        use_soft = input(
            '#. Usar soft boots? y/n: ') == 'y'
        buy_supply = input(
            '#. Auto refill (Necessário estar perto de um NPC)? y/n: ') == 'y'
        force_focus = input(
            '#. Forçar foco na janela do tibia? y/n: ') == 'y'
        spell_to_use = input(
            '#. Selecione a spell: \n   1. diamond arrows\n   2. spectral bolts\n   3. avalanches\n\n:: ')

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
        global use_ring, use_soft, buy_supply

        if (buy_supply):
            gamewindow.check_food_and_blank_runes()
        if (use_soft):
            gamewindow.check_softboots()
        if (use_ring):
            gamewindow.check_lifering()

    def default_action(self):
        gamewindow.drop_runes()
        hotkeys.rotate_char()
        gamewindow.eat()


app = App()

if (__name__ == "__main__"):
    app.main()

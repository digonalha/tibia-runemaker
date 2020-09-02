from .mouse import Mouse
from .keyboard import Keyboard, Key
from .hotkeys import Hotkeys
from .tools import Tools
from .imagefind import ImageFind

tools = Tools()
mouse = Mouse()
hotkeys = Hotkeys()
keyboard = Keyboard()
image_find = ImageFind()


class GameWindow:
    def show_equips(self):
        '''abre a janela de equipamentos caso fechada'''
        mouse.locate_and_click('btn_show_equipments.png')
        self.open_main_bp()

    def open_main_bp(self):
        '''abre a mochila principal (necessário para dar stow/jogar runas no chão)'''
        mouse.locate_and_click('main_bp.png', right=True)

    def close_all_windows(self):
        '''fecha todas as janelas abertas no jogo (backpacks, npc trade, skills, etc...)'''
        tools.is_tibia_focused()

        for i in range(0, 10):
            position = image_find.search('btn_close.png', precision=0.99)
            if (position):
                mouse.click_on_position(position, right=False)
            else:
                break

    def set_chat_off(self):
        mouse.locate_and_click('chat_on.png', keep_trying=False, timeout=0)

    def talk_with_npc(self, msg=str):
        self.set_chat_off()
        hotkeys.open_npc_chat()
        mouse.locate_and_click('chat_off.png', keep_trying=True, timeout=3)
        keyboard.press_key(Key.enter)
        hotkeys.send_msg('hi')
        hotkeys.send_msg(msg)

    def buy_food(self):
        self.talk_with_npc('supplies')
        mouse.locate_and_click('buy_food.png', keep_trying=True, timeout=3)
        self.scroll_to_max_and_buy()

    def buy_blank_runes(self):
        self.talk_with_npc('runes')
        mouse.locate_and_click('buy_blankrunes.png',
                               keep_trying=True, timeout=3)
        self.scroll_to_max_and_buy()

    def scroll_to_max_and_buy(self):
        mouse.click_and_drag(image_find.search(
            'scroll_horizontal.png'), image_find.search('scroll_to_max.png'))
        ok_button_position = image_find.search('btn_ok.png')

        for i in range(0, 2):
            mouse.click_on_position(ok_button_position, right=False)

    def check_food_and_blank_runes(self):
        if (image_find.search('acabou_food.png')):
            self.buy_food()
        if (image_find.search('acabou_runes.png')):
            self.pick_blank_runes()
            # self.buy_blank_runes()

    def drop_runes(self):
        tot = image_find.search_count('rune_to_drop.png')
        to_local = image_find.search('drop_spot.png')

        for i in range(0, tot):
            bp_rune_position = image_find.search('rune_to_drop.png')
            if (bp_rune_position and to_local):
                mouse.click_and_drag(bp_rune_position, to_local)
                keyboard.press_enter()
            else:
                break

    def pick_blank_runes(self):
        blank_rune_position = image_find.search('blank_rune_spot.png')
        to_local = image_find.search('main_bp.png')

        if (blank_rune_position and to_local):
            mouse.click_and_drag(blank_rune_position, to_local)
            keyboard.press_enter()

    def check_offline(self):
        main_screen = image_find.search('main_screen.png')
        disconnected = image_find.search('disconnected.png')

        if (main_screen or disconnected):
            return True

        return False

    def check_softboots(self):
        if (tools.is_tibia_focused()):
            boh_equipada = image_find.search('boh.png')
            descalco = image_find.search('descalco.png')
            sem_soft_nova = image_find.search('nsb.png')
            worn_softboots = image_find.search('wsb.png', precision=1)

            if ((worn_softboots or boh_equipada or descalco) and (sem_soft_nova is None)):
                # hotkey da soft boots
                mouse.locate_and_click('htk_soft_boots.png')
            elif (sem_soft_nova and (worn_softboots or boh_equipada)):
                return False

        return True

    def check_lifering(self):
        if (tools.is_tibia_focused()):
            has_lifering = image_find.search('lifering.png')
            no_ring_equiped = image_find.search('noring.png')

            if (has_lifering and no_ring_equiped):
                # hotkey do life ring
                mouse.click_on_position(has_lifering, right=False)
            else:
                return False

        return True

    def check_avalanche(self):
        if (tools.is_tibia_focused()):
            mouse.locate_and_click('htkavalanche.png')

    def check_diamond_arrow(self):
        if (tools.is_tibia_focused()):
            without_mana = image_find.search('diamond_without_mana.png')
            have_mana = image_find.search('diamond_with_mana.png')

            if (without_mana):
                while without_mana:
                    keyboard.press_key(Key.f2)
                    without_mana = image_find.search(
                        'diamond_without_mana.png')

                have_mana = image_find.search('diamond_with_mana.png')
                mouse.click_on_position(have_mana, right=False)
            elif (have_mana):
                mouse.click_on_position(have_mana, right=False)

    def eat(self):
        has_food = image_find.search('food.png')
        if (has_food):
            mouse.click_on_position(has_food, right=False)

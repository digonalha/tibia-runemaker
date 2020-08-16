from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from imagefind import ImageFind
from tools import Tools
import time

image_find = ImageFind()
tools = Tools()
mouse = MouseController()


class Mouse:
    def set_position(self, position):
        mouse.position = (position[0], position[1])
        time.sleep(0.2)

    def click_and_drag(self, from_local, to_local):
        self.set_position(from_local)
        mouse.press(Button.left)
        time.sleep(0.5)
        self.set_position(to_local)
        mouse.release(Button.left)

    def ctrl_right_click(self, local):
        with KeyboardController.pressed(Key.ctrl):
            mouse.click(local[0], local[1])

    def click_on_position(self, local, right):
        self.set_position(local)

        if (right):
            mouse.click(Button.right)
        else:
            mouse.click(Button.left)

    def locate_and_click(self, img_name=str, right=False, keep_trying=False, timeout=0, qtd_click=1):
        target = image_find.search(img_name)

        if (target):
            for i in range(0, qtd_click):
                self.click_on_position(target, right)
                return True
        elif (keep_trying and timeout != 0):
            timeout -= 1
            tools.is_tibia_focused()
            time.sleep(0.2)
            self.locate_and_click(
                img_name, right, keep_trying, timeout, qtd_click)
        else:
            return False

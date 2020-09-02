import cv2
import pyautogui
import numpy
import os


class ImageFind():
    def search(self, image, precision=0.93):
        im = pyautogui.screenshot()
        img_path = '{}\images\{}'.format(os.path.abspath(os.getcwd()), image)
        # im.save(img_path)

        img_rgb = numpy.array(im)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(img_path, 0)

        if (template is None):
            return None

        template.shape[::-1]

        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        if max_val < precision:
            return None

        return max_loc

    def search_count(self, image, precision=0.9):
        img_rgb = pyautogui.screenshot()

        img_path = '{}\images\{}'.format(os.path.abspath(os.getcwd()), image)

        img_rgb = numpy.array(img_rgb)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(img_path, 0)

        if (template is None):
            return 0

        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        loc = numpy.where(res >= precision)
        count = 0
        for pt in zip(*loc[::-1]):
            # cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2) // Uncomment to draw boxes around found occurrences
            count = count + 1
        # cv2.imwrite('result.png', img_rgb) // Uncomment to write output image with boxes drawn around occurrences
        return count

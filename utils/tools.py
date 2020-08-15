import datetime
import psutil
import os
import subprocess
import re

PROCNAME = "client"


class Tools:
    def is_time_between(self):
        """retorna verdadeiro se o horario for entre 06:10 AM e 5:55AM (evitando o server save de Venebra)"""
        now_time = datetime.datetime.now().time()
        start = datetime.time(6, 10)
        end = datetime.time(5, 55)
        if now_time >= start or now_time <= end:
            return True
        else:
            return False

    def check_is_opened(self):
        proc_opened = False

        for proc in psutil.process_iter():
            if proc.name() == PROCNAME:
                proc_opened = True
                break

        return proc_opened

    def is_tibia_focused(self):
        return True
        # TODO: aprender a manipular janela do windows. ver nicmd http://www.nirsoft.net/utils/nircmd.html
        # search = "Tibia"
        # subprocess.Popen("wmctrl -a " + search, shell=True)

        # #if (nobody_onscreen()):
        # cmd = "wmctrl -lp | grep $(xprop -root | grep _NET_ACTIVE_WINDOW | head -1 | \\awk '{print $5}' | sed 's/,//' | sed 's/^0x/0x0/')"
        # result = str(subprocess.check_output(cmd, shell=True))

        # if re.search(search, result):
        #     return True
        # else:
        #     return False

    def open_tibia_if_closed(self):
        if (not self.check_is_opened()):
            os.popen("/home/digo/Documents/Tibia/Tibia").read()

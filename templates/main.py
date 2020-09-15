"""Tela da aplicaçao de alteracao de arqid"""
import importlib
import sys
from tkinter import Button, Checkbutton, Entry, Frame, IntVar, Label

sys.path.append("..")


class MainWindow:
    """Montando a tela"""
    # pylint: disable=too-many-instance-attributes

    def __init__(self, master=None):
        self.etrade_checked = IntVar()
        self.gourmet_checked = IntVar()
        self.default_font = ("Segoe", "11")
        self.font_input = ("Segoe", "10")
        self.create_frames(master)
        self.create_check_boxes(master)
        self.create_buttons(master)
        # self.load_paths()

    def create_name_frame(self, master=None):
        self.txt_path_repository = Frame(master)
        self.txt_path_repository["padx"] = '50'
        self.txt_path_repository.pack()

        self.repo_label = Label(self.txt_path_repository, text="Character",
                                font=self.default_font)
        self.repo_label.pack(side='top')

        self.path_repo = Entry(self.txt_path_repository)
        self.path_repo["width"] = 20
        self.path_repo["font"] = self.font_input
        self.path_repo['highlightbackground'] = "green"
        self.path_repo.pack(side='top')

    def create_password_frame(self, master=None):
        self.txt_path_repository = Frame(master)
        self.txt_path_repository["padx"] = '50'
        self.txt_path_repository.pack()

        self.repo_label = Label(self.txt_path_repository, text="Password",
                                font=self.default_font)
        self.repo_label.pack(side='top')

        self.path_repo = Entry(self.txt_path_repository)
        self.path_repo["width"] = 20
        self.path_repo["font"] = self.font_input
        self.path_repo['highlightbackground'] = "green"
        self.path_repo.pack(side='top')

    def create_token_frame(self, master=None):
        self.txt_path_repository = Frame(master)
        self.txt_path_repository["padx"] = '50'
        self.txt_path_repository.pack()

        self.repo_label = Label(self.txt_path_repository, text="Auth token",
                                font=self.default_font)
        self.repo_label.pack(side='top')

        self.path_repo = Entry(self.txt_path_repository)
        self.path_repo["width"] = 20
        self.path_repo["font"] = self.font_input
        self.path_repo['highlightbackground'] = "green"
        self.path_repo.pack(side='top', expand='YES')

    def create_frames(self, master=None):
        """Criando os frames(txtedits) da aplicacao"""
        self.create_name_frame(master)
        self.create_password_frame(master)
        self.create_token_frame(master)

    def create_buttons(self, master=None):
        """Criando os botoes da aplicacao"""

        self.txt_container = Frame(master)
        self.txt_container.pack()

        self.btn_container = Frame(master)
        self.btn_container["padx"] = 20
        self.btn_container["pady"] = 10
        self.btn_container.pack()

        self.txt_status = Label(self.txt_container,
                                text="Status")
        self.txt_status["font"] = ("Arial", "9", "bold")
        self.txt_status.pack(side='top')

        self.mensagem = Label(self.txt_container,
                              text="",
                              foreground="green")
        self.mensagem["font"] = ("Arial", "9", "bold")
        self.mensagem.pack(anchor="center")

        self.btn_save_path = Button(self.btn_container,
                                    text="Xaxing!",
                                    width=12,
                                    command=self.save_path_click)
        self.btn_save_path.pack(side='left')

    def save_path_click(self):
        print('test')

    def create_check_boxes(self, master=None):
        self.chk_container = Frame(master)
        self.chk_container["padx"] = 20
        self.chk_container["pady"] = 10
        self.chk_container.pack()

        self.chk_etrade = Checkbutton(self.chk_container,
                                      text='Usar life ring',
                                      variable=self.etrade_checked,
                                      onvalue=1,
                                      offvalue=0)
        self.chk_etrade["padx"] = 5
        self.chk_etrade.pack(side='left')
        self.chk_gourmet = Checkbutton(self.chk_container,
                                       text='Usar mana potion',
                                       variable=self.gourmet_checked,
                                       onvalue=1,
                                       offvalue=0)
        self.chk_gourmet["padx"] = 20
        self.chk_gourmet.pack(side='right')

    def refresh_msg_color(self, result: str):
        if 'Verifique' in result:
            self.mensagem["foreground"] = "red"
        elif 'Os caminhos' in result:
            self.mensagem["foreground"] = "red"
        else:
            self.mensagem["foreground"] = "green"

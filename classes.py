import tkinter as tk
import tkinter.ttk as ttk

class main_window():
    def __init__(self, app):
        self.app = app
        self.app.title('Continuous plant with discrete controller')
        self.app.geometry('400x400')
        self.init_ui()

    def init_ui(self):
        self.tab_control = ttk.Notebook(self.app)
        self.tab_model = ttk.Frame(self.tab_control)
        self.tab_parameters = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_model, text='Modeling')
        self.tab_control.add(self.tab_parameters, text='Parameters')
        self.tab_control.pack(expand=1, fill='both')
        



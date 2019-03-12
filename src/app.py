import kivy

from kivy.uix.label import Label
from kivy.app import App
from .splash import LoginPage


class KeepStockApp(App):

    def build(self):
        return LoginPage()

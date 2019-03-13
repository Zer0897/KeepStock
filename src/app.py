import kivy

from kivy.uix.label import Label
from kivy.app import App
from .splash import SplashPage


class KeepStockApp(App):

    def build(self):
        return SplashPage()

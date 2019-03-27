import widget
from kivy.app import App
from pages.manager import PageManager


class KeepStockApp(App):

    def build(self):
        return PageManager()

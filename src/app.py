import widget
from kivy.app import App
from pages.manager import Manager


class KeepStockApp(App):

    def build(self):
        return Manager()

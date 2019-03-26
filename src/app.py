from kivy.app import App
from manager import Manager


class KeepStockApp(App):

    def build(self):
        return Manager()

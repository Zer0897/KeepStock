import src.widget.form
from kivy.app import App
from src.page.manage import PageManager


class KeepStockApp(App):

    def build(self):
        return PageManager()

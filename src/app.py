import widget.form
from kivy.app import App
from page.manage import PageManager


class KeepStockApp(App):

    def build(self):
        return PageManager()

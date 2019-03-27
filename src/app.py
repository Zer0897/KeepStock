from kivy.app import App
from src.page import View
from src.widget import NavigationBar


class KeepStockApp(App):

    def build(self):
        return View()

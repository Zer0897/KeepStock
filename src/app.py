from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from splash import SplashPage, LoginPage
from menu import MenuPage


class KeepStockApp(App):

    pages = {
        'splash': SplashPage,
        'menu': MenuPage,
        'login': LoginPage
    }

    def build(self):
        manager = ScreenManager()
        for name, page in self.pages.items():
            manager.add_widget(page(name=name))
        return manager

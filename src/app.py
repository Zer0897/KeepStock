from kivy.app import App
from src.page import BaseView

from src.widget import WIDGET_KV
from src.page import PAGE_KV


class KeepStockApp(App):

    def build(self):
        self.load_kv(str(WIDGET_KV))
        self.load_kv(str(PAGE_KV))

        return BaseView()

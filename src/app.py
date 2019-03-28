from kivy.app import App, Builder

from src.widget import WIDGET_KV
from src.page import PAGE_KV

Builder.load_file(str(WIDGET_KV))
Builder.load_file(str(PAGE_KV))


class KeepStockApp(App):
    pass

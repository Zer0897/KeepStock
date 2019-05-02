from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen


class BaseView(BoxLayout):
    pass


class PrimaryView(BaseView):
    pass


class SecondaryView(BaseView):
    pass


class InventoryView(Screen):
    pass


class Page(Screen):
    pass


class InventoryViewPage(Page):
    pass


class EditPage(Page):
    pass


class InPage(Page):
    pass


class OutPage(Page):
    pass


class ScanPage(Page):
    pass

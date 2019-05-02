from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from src.widget.base import Page
from src.widget.navigate import DropDownMenu
from kivy.clock import Clock


class BaseView(BoxLayout):
    pass


class PrimaryView(BaseView):
    pass


class SecondaryView(BaseView):
    pass


class InventoryView(Screen):
    pass


class InventoryViewPage(Page):

    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)

        Clock.schedule_once(self.build)

    def build(self, *args):
        self.header.content.add_widget(
            DropDownMenu.auto_detect(self.ids['manager'])
        )


class EditPage(Page):
    pass


class InPage(Page):
    pass


class OutPage(Page):
    pass


class ScanPage(Page):
    pass

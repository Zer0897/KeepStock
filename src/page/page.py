from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.screenmanager import Screen
from src.widget.base import Page
from src.widget.navigate import DropDownMenu


class BaseView(BoxLayout):
    pass


class PrimaryView(BaseView):
    pass


class SecondaryView(BaseView):
    pass


class InventoryView(Screen):
    pass


class InventoryViewPage(Page):

    def build(self, *args):
        container = BoxLayout()
        position = AnchorLayout()

        position.add_widget(DropDownMenu.auto_detect(
            self.ids['manager'], navconfig={'size_hint_x': .5}
        ))
        container.add_widget(position)
        self.ids['header'].content.add_widget(container)


class EditPage(Page):
    pass


class InPage(Page):
    pass


class OutPage(Page):
    pass


class ScanPage(Page):
    pass

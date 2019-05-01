from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from src.widget.navigate import DropDownMenu


class BaseView(BoxLayout):
    pass


class PrimaryView(BaseView):
    pass


class SecondaryView(BaseView):
    pass


class InventoryView(Screen):
    pass


class Page(Screen):
    sub_pages = ListProperty()

    def on_sub_pages(self, *args):
        menu = DropDownMenu()
        menu.manager = self.ids['manager']
        menu.name = 'View'
        menu.items = self.sub_pages
        self.header.add_widget(menu)


class SubPage(Screen):
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

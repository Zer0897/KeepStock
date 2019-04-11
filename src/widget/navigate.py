from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty, ObjectProperty, StringProperty
from kivy.uix.behaviors.togglebutton import ToggleButtonBehavior
from kivy.uix.dropdown import DropDown
from typing import NamedTuple
from src.widget.base import PrimaryButton


class NavigationItem(NamedTuple):
    text: str
    screen_id: str


class NavigationButton(ToggleButtonBehavior, PrimaryButton):
    manager = ObjectProperty(None)
    navigation: NavigationItem = ObjectProperty(None)

    def on_release(self, *args):
        if not self.manager.transition.is_active:
            self.manager.current = self.text.lower()
        self.update_state()

    def update_state(self):
        for btn in self.parent.children:
            if btn.navigation.screen_id == self.manager.current:
                btn.state = 'down'
            else:
                btn.state = 'normal'


class NavigationBehavior:
    manager = ObjectProperty(None)
    items = ListProperty()
    item_height = '50sp'

    def on_items(self, *args):
        group_id = ''.join(item.screen_id for item in self.items)
        for item in self.items:
            btn = self.create_button(group=group_id)
            btn.navigation = item
            self.add_button(btn)
            btn.update_state()

    def add_button(self, btn):
        self.add_widget(btn)

    def create_button(self, **kwds):
        btn = NavigationButton(**kwds)
        btn.manager = self.manager
        if btn.text.lower() == self.manager.current.lower():
            btn.state = 'down'
        return btn


class NavigationBar(BoxLayout, NavigationBehavior):

    def add_button(self, btn):
        self.buttons.add_widget(btn)


class DropDownMenu(DropDown, NavigationBehavior):
    manager = ObjectProperty(None)

    def create_button(self, **kwds):

        def select(btn):
            self.select(btn.text)

        btn = NavigationButton(**kwds)
        btn.manager = self.manager
        btn.size_hint_y = None
        btn.height = self.item_height
        btn.bind(on_select=select)
        return btn


class NavigationMenu(BoxLayout):
    manager = ObjectProperty(None)
    items = ListProperty(None)
    item_height = StringProperty(None)

    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)
        self.dropdown = DropDownMenu()


class HeaderBar(BoxLayout):
    pass

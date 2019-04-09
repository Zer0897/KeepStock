from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.behaviors.togglebutton import ToggleButtonBehavior
from kivy.uix.dropdown import DropDown
from functools import partial
from src.widget.base import PrimaryButton


class NavigationButton(ToggleButtonBehavior, PrimaryButton):
    def on_press(self, *args):
        if not self.parent.manager.transition.is_active:
            self.parent.manager.current = self.text.lower()

        for w in self.parent.children:
            if w.text.lower() == self.parent.manager.current.lower():
                w.state = 'down'
            else:
                w.state = 'normal'


class NavigationBehavior:
    items = ListProperty()
    item_height = '20sp'

    def on_items(self, *args):
        group_id = ''.join(self.items)
        for item in self.items:
            self.add_button(
                self.create_button(text=item, group=group_id)
            )

    def add_button(self, btn):
        self.add_widget(btn)

    def create_button(self, **kwds):
        btn = NavigationButton(**kwds)
        if btn.text.lower() == self.manager.current.lower():
            btn.state = 'down'
        return btn


class NavigationBar(BoxLayout, NavigationBehavior):

    def add_button(self, btn):
        self.buttons.add_widget(btn)


class DropDownMenu(DropDown, NavigationBehavior):

    def create_button(self, **kwds):

        def select(btn):
            self.select(btn.text)

        btn = NavigationButton(**kwds)
        btn.size_hint_y = None
        btn.height = self.item_height
        btn.bind(on_select=select)
        return btn


class NavigationMenu(BoxLayout):
    pass


class HeaderBar(BoxLayout):
    pass

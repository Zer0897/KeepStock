from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.behaviors.togglebutton import ToggleButtonBehavior

from src.widget.base import PrimaryButton


class NavigationButton(ToggleButtonBehavior, PrimaryButton):

    def on_state(self, widget, value):
        self.disabled = value == 'down'


class NavigationBar(BoxLayout):
    items = ListProperty()

    def on_items(self, *args):
        for item in self.items:
            self.add_widget(NavigationButton(text=item, group='1'))

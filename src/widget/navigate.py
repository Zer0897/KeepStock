from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.behaviors.togglebutton import ToggleButtonBehavior

from src.widget.base import PrimaryButton


class NavigationButton(ToggleButtonBehavior, PrimaryButton):
    pass


class NavigationBar(BoxLayout):
    items = ListProperty()

    def on_items(self, *args):
        for item in self.items:
            btn = NavigationButton(text=item, group=str(self.id))
            self.add_widget(btn)
            if btn.text.lower() == self.manager.current.lower():
                btn.state = 'down'

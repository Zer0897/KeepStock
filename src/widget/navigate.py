from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.uix.behaviors.togglebutton import ToggleButtonBehavior

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


class NavigationBar(BoxLayout):
    items = ListProperty()

    def on_items(self, *args):
        group_id = ''.join(self.items)
        for item in self.items:
            btn = NavigationButton(text=item, group=group_id)
            self.buttons.add_widget(btn)
            if btn.text.lower() == self.manager.current.lower():
                btn.state = 'down'


class HeaderBar(BoxLayout):
    pass

from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from collections import deque
from kivy.clock import Clock
from src.path import IMAGES


class BaseLabel(Label):
    pass


class PrimaryLabel(BaseLabel):
    pass


class SecondaryLabel(BaseLabel):
    pass


class TitleLabel(PrimaryLabel):
    pass


class HeadingLabel(SecondaryLabel):
    pass


class BaseButton(Button):
    pass


class PrimaryButton(BaseButton):
    pass


class SecondaryButton(BaseButton):
    pass


class HeaderBar(BoxLayout):
    menu_icon = IMAGES / 'menu-icon.png'
    back_arrow = IMAGES / 'back-arrow.png'


class Page(Screen):
    _history = deque(maxlen=3)

    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)

        if hasattr(self, 'build'):
            Clock.schedule_once(self.build)

    def on_leave(self, *args):
        type(self)._history.appendleft(self.name)

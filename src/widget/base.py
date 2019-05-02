from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty, ListProperty


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
    pass


class Page(Screen):
    _last = None

    def on_leave(self, *args):
        type(self)._last = self.name

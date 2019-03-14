from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.properties import ListProperty


# class Form(GridLayout):




class Entry(TextInput):

    def update_padding(self, *args):
        text_width = self._get_text_width(
            self.text,
            self.tab_width,
            self._label_cached
        )
        self.padding_x = (self.width - text_width) / 2


class NamedEntry(BoxLayout):
    pass


class BaseLabel(Label):
    pass
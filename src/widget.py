from kivy.uix.textinput import TextInput
from kivy.uix.label import Label


class Entry(TextInput):

    def update_padding(self, *args):
        text_width = self._get_text_width(
            self.text,
            self.tab_width,
            self._label_cached
        )
        self.padding_x = (self.width - text_width) / 2


class BaseLabel(Label):
    pass
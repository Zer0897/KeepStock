from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class Entry(TextInput):

    def update_padding(self, *args):
        text_width = self._get_text_width(
            self.text,
            self.tab_width,
            self._label_cached
        )
        self.padding_x = (self.width - text_width) / 2


class Notification(Popup):

    @classmethod
    def info(cls, txt):
        pop = cls(content=Label(text=txt), title='Info')
        pop.open()
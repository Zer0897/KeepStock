from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.properties import ListProperty


class Form(BoxLayout):

    entries = ListProperty()
    private = ListProperty()
    required = ListProperty()

    def on_entries(self, *args):
        for name in self.entries:
            self.add_widget(
                NamedEntry(name=name)
            )
    def on_private(self, *args):
        for entry in self.children:
            if entry.name in self.private:
                entry.password = True

    def on_required(self, *args):
        for entry in self.children:
            if entry.name in self.required:
                entry.required = True


class Entry(TextInput):

    def update_padding(self, *args):
        text_width = self._get_text_width(
            self.text,
            self.tab_width,
            self._label_cached
        )
        self.padding_x = (self.width - text_width) / 2


class NamedEntry(BoxLayout):

    def __init__(self, *args, name: str = '', **kwds):
        self.id = self.name = name

        super().__init__(*args, **kwds)


class BaseLabel(Label):
    pass
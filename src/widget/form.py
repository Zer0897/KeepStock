from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty

from typing import Callable, Optional


class Entry(TextInput):
    pass


class NamedEntry(BoxLayout):
    pass


class Form(BoxLayout):

    entries = ListProperty()
    private = ListProperty()
    required = ListProperty()

    def __apply_all(self, fn: Callable, entries: Optional[Entry] = None):
        for entry in entries or self.as_list():
            fn(entry)

    def on_entries(self, *args):

        def add(name):
            widget = NamedEntry()
            widget.name = name
            self.add_widget(widget)

        self.__apply_all(add, self.entries)

    def on_private(self, *args):
        self.__apply_all(
            lambda widget: setattr(widget, 'password', widget.name in self.private)
        )

    def on_required(self, *args):
        self.__apply_all(
            lambda widget: setattr(widget, 'required', widget.name in self.required)
        )

    def as_dict(self) -> dict:
        return {w.name: w.value.text for w in self.as_list()}

    def as_list(self) -> list:
        return [w for w in self.children if w.name in self.entries]

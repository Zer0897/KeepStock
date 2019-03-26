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

    def as_dict(self) -> dict:
        return {w.name: w.value.text for w in self.as_list()}

    def as_list(self) -> list:
        return [w for w in self.children if w.name in self.entries]


class Entry(TextInput):
    ...


class NamedEntry(BoxLayout):

    def __init__(self, *args, name: str = '', **kwds):
        self.id = self.name = name

        super().__init__(*args, **kwds)


class BaseLabel(Label):
    pass
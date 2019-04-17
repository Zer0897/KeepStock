from kivy.properties import StringProperty
from kivy.uix.popup import Popup

from enum import Enum
from kivy.uix.boxlayout import BoxLayout


class Info(BoxLayout):
    message = StringProperty()


class Warn(Info):
    pass


class Err(Warn):
    pass


class Severity(Enum):
    INFO = Info
    WARNING = Warn
    ERROR = Err


class Notification(Popup):

    def __init__(self, *args, severity=Severity.INFO, **kwargs):
        self.severity = severity

        super().__init__(*args, **kwargs)

    @classmethod
    def __build(cls, severity: Severity, message: str):
        cls(severity=severity).show(message)

    @classmethod
    def info(cls, message: str):
        Notification.__build(Severity.INFO, message)

    @classmethod
    def warn(cls, message: str):
        Notification.__build(Severity.WARNING, message)

    @classmethod
    def err(cls, message: str):
        Notification.__build(Severity.ERROR, message)

    def show(self, message: str):
        self.content.message = message
        self.content.btn.bind(on_press=self.dismiss)
        self.open()

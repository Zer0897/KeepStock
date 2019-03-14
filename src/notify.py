
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from enum import Enum


class Notify(Label):
    message = StringProperty()


class Warn(Notify):
    pass


class Err(Warn):
    pass


class Severity(Enum):
    INFO = Notify
    WARNING = Warn
    ERROR = Err


class Notification(Popup):

    def __init__(self, *args, severity=Severity.INFO, **kwargs):
        self.severity = severity
        
        super().__init__(*args, **kwargs)


    def create(self, message: str):
        self.content.message = message
        self.open()

    @classmethod
    def info(cls, message: str):
        cls(severity=Severity.INFO).create(message)

    @classmethod
    def warn(cls, message: str):
        cls(severity=Severity.WARNING).create(message)

    @classmethod
    def err(cls, message: str):
        cls(severity=Severity.ERROR).create(message)

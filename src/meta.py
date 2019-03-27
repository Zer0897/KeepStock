import inspect
import importlib
from path import SRC
from kivy.uix.screenmanager import Screen


def get_pages() -> dict:
    pages = {}
    for name in map(inspect.getmodulename, SRC.rglob('*.py')):
        mod = importlib.import_module(name)
        members = inspect.getmembers(mod, inspect.isclass)
        pages.update(
            {name: cls for name, cls in members if issubclass(cls, Screen)}
        )
    return pages

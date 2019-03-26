import inspect
import importlib
from pathlib import Path
from kivy.uix.screenmanager import Screen

DIR = Path(__file__).parent


def get_pages():
    pages = {}
    for name in map(inspect.getmodulename, DIR.rglob('*.py')):
        mod = importlib.import_module(name)
        members = inspect.getmembers(mod, inspect.isclass)
        pages.update(
            {name: cls for name, cls in members if issubclass(cls, Screen)}
        )
    return pages

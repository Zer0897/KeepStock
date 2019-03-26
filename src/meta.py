import inspect
import importlib
from pathlib import Path

SRC = Path(__file__).parent

def __get_module_names():
    return map(inspect.getmodulename, SRC.rglob('*.py'))

def __get_modules(*names):
    return map(importlib.import_module, names)

def get_pages():
    names = __get_module_names()

    pages = {}
    for mod in __get_modules(*names):
        members = inspect.getmembers(mod, inspect.isclass)
        pages.update(
            {name: cls for name, cls in members if 'Page' in name}
        )
    return pages

print(get_pages())

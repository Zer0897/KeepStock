from kivy.lang import Builder

from . import KV
from .app import KeepStockApp

for file in KV.rglob('*.kv'):
    Builder.load_file(str(file))

if __name__ == '__main__':
    KeepStockApp().run()

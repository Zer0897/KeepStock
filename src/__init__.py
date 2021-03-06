import sys
from kivy.app import Builder
from src.page import KV_FILES as page_kv
from src.widget import KV_FILES as widget_kv
from src.path import ROOT
from contextlib import suppress

with suppress(ImportError):
    import stackprinter
    stackprinter.set_excepthook(style='darkbg3')


for kv in page_kv + widget_kv:
    Builder.load_file(str(kv))

sys.path.append(str(ROOT))

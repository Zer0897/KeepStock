from __future__ import annotations
from src.widget.notify import Notification
from kivy.garden.zbarcam.zbarcam import ZBarCam
from kivy.clock import Clock


class ScannerException(Exception):
    pass


class Scanner(ZBarCam):

    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)

        self.capture = Clock.schedule_once(self.parse, 0)

    def on_symbols(self, *args):
        self.capture()

    def parse(self, *args):
        if self.symbols:
            data = self.symbols[0].data.decode('utf-8')
            Notification.info(data)
            self.play = False

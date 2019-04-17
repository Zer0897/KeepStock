from src.widget.notify import Notification
from kivy.garden.zbarcam.zbarcam import ZBarCam
from kivy.clock import Clock


class ScannerException(Exception):
    pass


class Scanner(ZBarCam):

    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)

        self.capture = Clock.create_trigger(self.parse, .05)
        self.bind(symbols=self.capture)

    def parse(self, *args):
        if self.symbols:
            data = self.symbols[0].data.decode('utf-8')
            Notification.info(data)
            self.play = False

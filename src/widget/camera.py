from src.widget.notify import Notification
from kivy.garden.zbarcam.zbarcam import ZBarCam
from kivy.clock import Clock


class ScannerException(Exception):
    pass


class Scanner(ZBarCam):

    def capture(self, *args):
        if self.symbols:
            Notification.info(self.parse())
            self.play = False

        elif self.play:
            Clock.schedule_once(self.capture)

    def parse(self):
        try:
            return self.symbols[0].data.decode('utf-8')
        except IndexError as e:
            raise ScannerException("No data detected") from e

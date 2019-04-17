from src.widget.notify import Notification
from kivy.garden.zbarcam.zbarcam import ZBarCam
from kivy.clock import Clock


class Scanner(ZBarCam):

    def capture(self, *args):
        if not self.symbols:
            if self.play:
                Clock.schedule_once(self.capture)
        else:
            Notification.info('\n'.join(str(sym.data) for sym in self.symbols))
            self.play = False

from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout

from .widget import Notification

class LoginPage(GridLayout):

    def submit(self):
        print(self.ids.username.text, self.ids.password.text, sep='\n')
        Notification.info('Test')


class SplashPage(AnchorLayout):
    pass

from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout

from .notify import Notification

class LoginPage(GridLayout):

    def submit(self):
        Notification.info('This is a longer test, with more text. I want more text so I can test the limits of the label widget I am using.')


class SplashPage(AnchorLayout):
    pass


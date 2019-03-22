from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout

from notify import Notification

class LoginPage(BoxLayout):

    def submit(self):
        Notification.info('Foo')


class SplashPage(AnchorLayout):
    pass


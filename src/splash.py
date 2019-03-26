from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout

from notify import Notification

class LoginPage(BoxLayout):

    def submit(self):
        if not all(self.form.as_dict().values()):
            Notification.info('All fields are required.')



class SplashPage(AnchorLayout):
    pass


from kivy.uix.screenmanager import Screen
from src.widget import Notification


class LoginPage(Screen):

    def submit(self):
        if not all(self.form.as_dict().values()):
            Notification.info('All fields are required.')
        else:
            self.manager.current = 'MenuPage'


class SplashPage(Screen):
    pass

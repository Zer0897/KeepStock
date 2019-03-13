from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout


class LoginPage(GridLayout):

    def submit(self):
        print(self.ids.username.text, self.ids.password.text, sep='\n')


class SplashPage(AnchorLayout):
    pass

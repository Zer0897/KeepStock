from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout

class LoginPage(GridLayout):

    def submit(self, f_user, f_pass):
        print(f_user, f_pass)


class SplashPage(AnchorLayout):
    pass

from kivy.uix.boxlayout import BoxLayout


class LoginPage(BoxLayout):

    def submit(self, f_user, f_pass):
        print(f_user, f_pass)

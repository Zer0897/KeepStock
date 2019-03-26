import meta
from kivy.uix.screenmanager import ScreenManager


class Manager(ScreenManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, page in meta.get_pages().items():
            self.add_widget(page(name=name))

        self.current = 'SplashPage'

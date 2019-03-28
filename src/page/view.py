from kivy.uix.boxlayout import BoxLayout


class BaseView(BoxLayout):
    pass


class PrimaryView(BaseView):
    pass


class SecondaryView(BaseView):
    pass


class Page(PrimaryView):
    pass


class Window(SecondaryView):
    pass

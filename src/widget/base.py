from kivy.uix.label import Label
from kivy.uix.button import Button


class BaseLabel(Label):
    pass


class PrimaryLabel(BaseLabel):
    pass


class SecondaryLabel(BaseLabel):
    pass


class TitleLabel(PrimaryLabel):
    pass


class HeadingLabel(SecondaryLabel):
    pass


class BaseButton(Button):
    pass


class PrimaryButton(BaseButton):
    pass


class SecondaryButton(BaseButton):
    pass


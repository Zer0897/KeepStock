from __future__ import annotations
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors.togglebutton import ToggleButtonBehavior
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, TransitionBase
from kivy.clock import Clock, ClockEvent
from kivy.uix.dropdown import DropDown
from typing import NamedTuple, Optional, List
from dataclasses import dataclass
from src.widget.base import PrimaryButton


@dataclass
class NavigationItem:
    text: str
    id: str
    transition: TransitionBase = None


class NavigationButton(ToggleButtonBehavior, PrimaryButton):
    managers = dict()
    navigation: NavigationItem = ObjectProperty(None)

    _current_event: Optional[ClockEvent] = None

    def __navigate(self):
        prev = self.manager.transition
        if self.navigation.transition:
            self.manager.transition = self.navigation.transition
        self.manager.current = self.navigation.id
        self.manager.transition = prev

    def on_press(self, *args):

        def navigate(*args):
            self.selected = True

        if NavigationButton._current_event is not None:
            NavigationButton._current_event.cancel()

        if self.manager.transition.is_active:
            duration = self.manager.transition.duration
            progress = self.manager.current_screen.transition_progress
            time_remaining = duration - (duration * progress)
        else:
            time_remaining = -1  # Instant

        NavigationButton._current_event = Clock.schedule_once(navigate, time_remaining)

    def update_group(self):
        for btn in self.group_widgets():
            btn.refresh()

    def refresh(self):
        self.selected = self.selected  # State of button reflects the current screen

    def group_widgets(self) -> List[NavigationButton]:
        return ToggleButtonBehavior.get_widgets(self.group)

    @property
    def selected(self) -> bool:
        return self.navigation.id == self.manager.current

    @selected.setter
    def selected(self, val: bool):
        if val:
            self.__navigate()
            self.state = 'down'
        else:
            self.state = 'normal'

    @property
    def manager(self) -> ScreenManager:
        return NavigationButton.managers.get(self.group)


class NavigationContainerBehavior:
    manager = ObjectProperty(None)
    items = ListProperty()
    item_height = '50sp'

    def on_items(self, *args):
        btn_group = '|'.join(item.id for item in self.items)
        NavigationButton.managers[btn_group] = self.manager
        for item in self.items:
            btn = self.create_button(group=btn_group)
            btn.navigation = item
            self.add_button(btn)

    def add_button(self, btn: NavigationButton):
        self.add_widget(btn)

    def create_button(self, **kwds):
        return NavigationButton(**kwds)


class NavigationBar(BoxLayout, NavigationContainerBehavior):

    def add_button(self, btn):
        self.buttons.add_widget(btn)


class DropDownMenu(BoxLayout, NavigationContainerBehavior):

    def __init__(self, *args, **kwds):
        self.dropdown = DropDown()
        super().__init__(*args, **kwds)

    def create_button(self, **kwds):
        btn = NavigationButton(**kwds)
        btn.size_hint_y = None
        btn.height = self.item_height
        return btn

    def add_button(self, btn):
        self.dropdown.add_widget(btn)

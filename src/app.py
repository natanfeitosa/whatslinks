import typing as t
import kivy
kivy.require('2.1.0')

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager

from src.utils import dynamic_class_import


def load_all_screens() -> t.List[Screen]:
    paths = [
        'home.Home',
        'qrcode.QRCode',
        'history.History',
    ]

    screens = []
    
    for path in paths:
        screen = dynamic_class_import(f'src.screens.{path}')
        screen.name = screen.__class__.__name__
        screens.append(screen)
    
    return (screens)


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_screens()
    
    def load_screens(self):
        for screen in load_all_screens():
            if screen not in self.screens:
                # screen.manager = self
                self.add_widget(screen)


class MainWindow(Screen):

    def change_screen(self, screen_name):
        manager: ScreenManager = self.ids.manager
        # manager.switch_to(manager.get_screen(screen_name))
        manager.current = screen_name

class App(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.load_all_kv_files(self.directory)
    
    def build(self):
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.primary_hue = '800'
        return MainWindow()
    
    # def change_screen(self, instance):
    #     print(dir(self.get_running_app()))

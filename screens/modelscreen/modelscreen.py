from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivymd.app import MDApp
app = MDApp.get_running_app()


class ModelScreen(MDScreen):
    pass


Builder.load_file('modelscreen.kv')

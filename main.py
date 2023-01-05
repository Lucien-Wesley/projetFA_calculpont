import sys
import os
# os.environ["KIVY_NO_CONSOLELOG"] = '1'

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(os.path.dirname(sys.argv[0]))

    return os.path.join(base_path, relative_path)

from kivy.config import Config
Config.set('kivy', 'exit_on_escape', '0')

from kivy.core.window import Window
from kivy.resources import resource_add_path
from kivy.uix.screenmanager import ScreenManager, FadeTransition
from kivymd.app import MDApp
from kivy.properties import NumericProperty, StringProperty

resource_add_path(resource_path(os.path.join('screens', 'presplash')))
resource_add_path(resource_path(os.path.join('screens', 'mainscreen')))
resource_add_path(resource_path(os.path.join('screens', 'modelscreen')))
resource_add_path(resource_path(os.path.join('screens', 'resultscreen')))


class K10BridgeProject(MDApp):

    name = "K10BridgeProject"
    title = "K10BridgeProject"

    model = NumericProperty(0)
    dessin = StringProperty("")

    def build(self):
        from screens.presplash import presplash
        from screens.mainscreen import mainscreen
        from screens.modelscreen import modelscreen
        from screens.resultscreen import resultscreen

        self.root = ScreenManager()
        self.presplash = presplash.Presplash()
        self.mainscreen = mainscreen.MainScreen()
        self.modelscreen = modelscreen.ModelScreen()
        self.resultscreen = resultscreen.ResultScreen()
        self.screens = {
            "presplash": self.presplash,
            "mainscreen": self.mainscreen,
            "modelscreen": self.modelscreen,
            "resultscreen": self.resultscreen,
        }
        self.screen_history = []
        Window.bind(on_key_up=self.back_button)
        Window.softinput_mode = "below_target"
        self.root.transition = FadeTransition()
        self.switch_screen("presplash")

    def switch_screen(self, screen_name):
        self.root.switch_to(self.screens.get(screen_name))
        self.screen_history.append(screen_name)

    def back_button(self, instance, keyboard, *args):
        if keyboard in (1001, 27):
            self.screen_history.pop()
            if self.screen_history != []:
                self.root.switch_to(self.screens.get(self.screen_history[-1]))
            else:
                self.stop()
            return True


if __name__ == "__main__":
    K10BridgeProject().run()

import json

from kivy import platform
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.uix.screenmanager import SlideTransition, ScreenManagerException
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.lang.builder import Builder

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.navigationbar import MDNavigationBar, MDNavigationItem
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.textfield import MDTextFieldHelperText
from kivymd.uix.transition import MDFadeSlideTransition

#Load all modules from here
from assets.disclaimer_notes import notes
from dashboard import HomeScreen, ChatScreen

#setting global font and font-name for the app
LabelBase.register(name='T1Robit',
                   fn_regular='fonts/T1RobitTrial-Regular.otf',
                   fn_bold='fonts/T1RobitTrial-Bold.otf')

#load all kv files from here
Builder.load_file('KV/WelcomeScreen.kv')
Builder.load_file('KV/DisclaimerScreen.kv')
Builder.load_file('KV/Dashboard.kv')


#SCREENS --------------  SCREENS   --------------  SRCREENS  ------------------    #SCREENS
class WelcomeScreen(MDScreen):
    """Welcome screen with the app name and logo"""
    pass

class DisclaimerScreen(MDScreen):
    """a note about what the app is majorly used for,
    and some health related issues that should be taken
    care off"""
    text = notes
    # chip = HomeScreen.load_symptoms_chip()

class UnderLayout(MDScreen):
    """
    Just and underlaying screen for the dashboard
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_widget(Dashboard())

class Home(HomeScreen):
    pass

#BOX_LAYOUT --------------  OTHER   --------------  CLASSES  ------------------    #BOX_LAYOUT
class Dashboard(MDBoxLayout):
    """ The App Dashboard consist of the HomeScreen(), ChatScreen(), HistoryScreen() and SettingScreen()
        """
    def on_switch_tabs(self, bar: MDNavigationBar, item: MDNavigationItem, item_icon: str, item_text: str, ):
        self.ids.screen_manager.transition = MDFadeSlideTransition(direction='down')

        self.ids.screen_manager.current = item_icon or item_text





#MAIN_APP --------------  MAIN_APP   --------------  MAIN_APP  ------------------    #MAIN_APP
class MyFABApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = MDScreenManager(md_bg_color=self.theme_cls.surfaceColor)
        self.box = None
        # self.home = HomeScreen()
        # self.chat = ChatScreen()
        self.home = Home()
        # # home.load_sickness_data()
        # home.load_symptoms_chip()

    def load_symptoms_chip(self):
        self.home.load_symptoms_chip()
        
    def on_start(self):
        pass
    # @staticmethod
    # def on_start(self) -> None:
    #     """It is fired at the start of the application and requests the
    #     necessary permissions."""
    #     home = HomeScreen()
    #     home.load_sickness_data()
    #     home.load_symptoms_chip()
    #
    #     def callback(permission, results):
    #         if all([res for res in results]):
    #             Clock.schedule_once(self.set_dynamic_color)
    #
    #     if platform == "android":
    #         from android.permissions import Permission, request_permissions
    #
    #         permissions = [Permission.READ_EXTERNAL_STORAGE]
    #         request_permissions(permissions, callback)
    #

    # def on_resume(self, *args):
    #     """Updating the color scheme when the application resumes."""
    #     self.theme_cls.set_colors()

    # def set_dynamic_color(self):
    #     """When sets the `dynamic_color` value, the self method will be
    #     `called.theme_cls.set_colors()` which will generate a color
    #     scheme from a custom wallpaper if `dynamic_color` is `True`."""
    #
    #     self.theme_cls.dynamic_color = True

    def change_screen(self, w_scn, w_dir, some_agr):
        """
        :param w_scn: which Screen you are changing to e.g 'home'
        :param w_dir: for the SlideTransition which direction did you want e.g 'left', 'right'
        :param some_agr: optional space for button function if available
        :return:
        """
        self.root.transition = SlideTransition(direction=w_dir, duration=.5)
        self.root.current = w_scn
        some_agr = None

    def toggle_theme(self, is_dark):
        self.theme_cls.theme_style = (
            'Dark' if is_dark else 'Light'
        )

    def build(self):
        # """The app build"""
        self.title = 'My First Aid Box'
        self.icon = 'logo.jpg'
        # self.theme_cls.theme_style = 'Dark'
        # self.theme_cls.primary_palette = 'Red'
        self.sm = MDScreenManager(
            md_bg_color=self.theme_cls.surfaceColor,
        )
        screens = (WelcomeScreen(), DisclaimerScreen(), UnderLayout())
        for screen in screens:
            self.sm.add_widget(screen)

        for style in self.theme_cls.font_styles:
            font = self.theme_cls.font_styles[style]
            font[0] = 'T1Robit'

        # self.home.load_sickness_data()
        # self.chat.show_sickness_details()
        return self.sm



if __name__ == '__main__':
    Window.size = (320, 600)
    MyFABApp().run()
import json
import asynckivy

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.recycleview import RecycleView
from kivy.uix.screenmanager import FadeTransition, ScreenManager
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDButton, MDButtonText
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.chip import MDChip, MDChipText, MDChipLeadingIcon
from kivymd.uix.dialog import MDDialog, MDDialogHeadlineText, MDDialogSupportingText, MDDialogButtonContainer
from kivymd.uix.list import MDListItem, MDListItemHeadlineText
from kivymd.uix.navigationbar import MDNavigationItem, MDNavigationBar, MDNavigationItemIcon, MDNavigationItemLabel
from kivymd.uix.recycleview import MDRecycleView
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.transition import MDFadeSlideTransition

#Load all Screen KV file from here
Builder.load_file('KV/HomeScreen.kv')
Builder.load_file('KV/ChatScreen.kv')
Builder.load_file('KV/HistoryScreen.kv')
Builder.load_file('KV/SettingScreen.kv')


try:
    with open('health_data.json','r',encoding='utf-8') as data_file:
        get_sickness_data = json.load(data_file)
except FileNotFoundError:
    print('file not found')
    get_sickness_data = []
SICKNESS_ = get_sickness_data

class BaseMDNavigationItem(MDNavigationItem):
    icon = StringProperty()
    text = StringProperty()

class ListItem(MDListItem):
    icon = StringProperty()
    text = StringProperty()

class SicknessListItem(MDListItem):
    text = StringProperty()
    def switch_to_chat(self):
        self.chat = ChatScreen()

        return self.chat.show_sickness_details()

class CommonAssistChip(MDChip):
    text = StringProperty()

class HomeScreen(MDScreen):
    # def __init__(self):
    #     super().__init__()

        # try:
        #     with open('health_data.json','r',encoding='utf-8') as data_file:
        #         self.get_sickness_data = json.load(data_file)
        # except FileNotFoundError:
        #     print('file not found')
        #     self.get_sickness_data = []
        # self.sickness_ = self.get_sickness_data
        
    def load_sickness_data(self, text='', search=False):
        """ Asynchronously Build a list of Sicknesses available from the database
        :param text: User search input
        :param search: bool for search, defaults to False
        :return:
        """
        # try:
        #     with open('health_data.json','r',encoding='utf-8') as data_file:
        #         self.get_sickness_data = json.load(data_file)
        # except FileNotFoundError:
        #     print('file not found')
        #     self.get_sickness_data = []
        # self.sickness_ = self.get_sickness_data

        def add_sickness_list(sickness_name):
            """
            Add all conditions (sickness) name to the home screen
            :param sickness_name: name to be added to the recycle view
            :return:
            """
            self.ids.rv.data.append(
                {
                    'viewclass': 'SicknessListItem',
                    # 'icon': name_icon,
                    'text': sickness_name,
                    'callback': lambda x: x
                }
            )
        self.ids.rv.data = []

        for sickness_name in SICKNESS_:
                if search:
                    if text in sickness_name['name'].lower():
                        add_sickness_list(sickness_name['name'])
                else:
                    add_sickness_list(sickness_name['name'])

    def load_symptoms_chip(self):
        async def load_symptoms_chip():
            for symptoms in SICKNESS_:
                await asynckivy.sleep(0)
                for symptom in symptoms['keywords']:
                    await asynckivy.sleep(0)
                    chip = MDChip(
                        MDChipLeadingIcon(icon='plus'),
                        MDChipText(text=symptom),
                        type="assist",
                    )
                    chip.bind(active=lambda x:x)
                    self.ids.chip_box.add_widget(chip)

        asynckivy.start(load_symptoms_chip())

class ChatScreen(MDScreen):
    def show_sickness_details(self):
        self.homescreen = HomeScreen()

        self.homescreen.load_sickness_data()

class HistoryScreen(MDScreen):
    pass

class SettingScreen(MDScreen):
    def on_start(self):
        l = ['why ']

# class Dashboard(MDBoxLayout):
#     """
#     The App Dashboard consist of the HomeScreen(), ChatScreen(), HistoryScreen() and SettingScreen()
#     """
#     def on_switch_tabs(self, bar: MDNavigationBar, item: MDNavigationItem, item_icon: str, item_text: str,):
#         # self.manager.current = self.name
#         # home = HomeScreen()
#         # home.load_symptoms_chip()
#         self.ids.screen_manager.transition = MDFadeSlideTransition(direction='down')
#
#         self.ids.screen_manager.current = item_icon or item_text



# Builder.load_file('KV/Dashboard.kv')
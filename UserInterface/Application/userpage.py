
from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton, ListView
from kivy.properties import ObjectProperty, ListProperty
from faker import Faker
from kivy.adapters.dictadapter import DictAdapter
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.listview import ListItemButton, ListItemLabel, \
CompositeListItem, ListView
fake = Faker()




class DataItem(object):
    def __init__(self, name='', created_on="",  is_selected=False):
        self.name = name
        self.created_on = created_on
        self.is_selected = is_selected


class UserPage(Screen):
    data_items = ListProperty([])
    items = ListProperty([])
    app = ObjectProperty(None)
    transport = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(UserPage, self).__init__(**kwargs)

        self.data_items = [DataItem(name='cat', created_on=fake.date()),
              DataItem(name='dog', created_on=fake.date()),
              DataItem(name='frog', created_on=fake.date())]

        #self.data_items = [{'name': fake.name(),  'is_selected': False} for i in range(10)]


    def _args_converter(self, row_index, obj):
        __dict = {'name': obj.name, 
                'size_hint_y': None, 
                'height': 25, 
                }
        return __dict

    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'Login'
        self.manager.get_screen('Login').resetForm()

    def on_cancel(self):

        self.go_to_login()
    
    def add(self, *args):
        self.ids['VIEWlist'].adapter.data.append('txt')


    def go_to_login(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'Login'
        self.manager.get_screen('Login').resetForm()
        return  

    def selection_changed(self, *args):
        print ('You can even bind a callback that does something when your selection changes, if you want.')

    def  create_asset(self):
        print ("create asset has been clicked")


    def store_data(self):
        print ("Store data has been clicked")

    def transfer_asset(self):
        print ("Transfer asset has been clicked")

    

from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton, ListView
from kivy.properties import ObjectProperty, ListProperty
from faker import Faker
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.scrollview import ScrollView
from kivy.uix.listview import ListItemButton, ListItemLabel, \
CompositeListItem, ListView
from kivy.properties import ObjectProperty
from Application.table import MTable
fake = Faker()

data =    [
            {'name': 'name', 'score': 'score', 'car': 'car'},
            {'name': 'przyczajony', 'score': '1337', 'car': 'Fiat 126p'},
            {'name': 'Krusader Jake', 'score': '777', 'car': 'Ford'},
            {'name': 'dummy', 'score': '10', 'car': 'none'},
            {'name': 'dummy', 'score': '102', 'car': 'none'},
            {'name': 'dummy', 'score': '60', 'car': 'none'},
            {'name': 'dummy', 'score': '990', 'car': 'none'},
            {'name': 'dummy', 'score': '550', 'car': 'none'},
            {'name': 'dummy', 'score': '310', 'car': 'none'},
            {'name': 'dummy', 'score': '320', 'car': 'none'},
            {'name': 'dummy', 'score': '880', 'car': 'none'},
             {'name': 'dummy', 'score': '880', 'car': 'none'},
{'name': 'dummy', 'score': '880', 'car': 'none'},{'name': 'dummy', 'score': '880', 'car': 'none'},
{'name': 'dummy', 'score': '880', 'car': 'none'},{'name': 'dummy', 'score': '880', 'car': 'none'},
{'name': 'dummy', 'score': '880', 'car': 'none'},{'name': 'dummy', 'score': '880', 'car': 'none'},
{'name': 'dummy', 'score': '880', 'car': 'none'},{'name': 'dummy', 'score': '880', 'car': 'none'},
{'name': 'dummy', 'score': '880', 'car': 'none'},{'name': 'dummy', 'score': '880', 'car': 'none'},
{'name': 'dummy', 'score': '880', 'car': 'none'},{'name': 'dummy', 'score': '880', 'car': 'none'},
{'name': 'dummy', 'score': '880', 'car': 'none'},{'name': 'dummy', 'score': '880', 'car': 'none'},
{'name': 'dummy', 'score': '880', 'car': 'none'},{'name': 'dummy', 'score': '880', 'car': 'none'},
{'name': 'dummy', 'score': '880', 'car': 'none'},{'name': 'dummy', 'score': '880', 'car': 'none'},
{'name': 'dummy', 'score': '880', 'car': 'none'},{'name': 'dummy', 'score': '880', 'car': 'none'},
{'name': 'dummy', 'score': '880', 'car': 'none'},{'name': 'dummy', 'score': '880', 'car': 'none'},


        ]

f = MTable(data, cols=4)



class IPFSListButton(ListItemButton):
    def __init__(self, *args, **kwargs):
        super(IPFSListButton, self).__init__(*args, **kwargs)
        self.fbind('on_is_selected', self.print_info)
        self.fbind('on_press', self.print_info_p)

    def print_info(self,*args):
        print ("on_is_selected: item {}, is_selected: {}, index: {}".format(self, self.is_selected, self.index))
    def print_info_p(self,*args):
        print ("on_press: item {}, is_selected: {}, index: {}".format(self, self.is_selected, self.index))

    


class DataItem(object):
    def __init__(self, name='', created_on="",  is_selected=False):
        self.name = name
        self.created_on = created_on
        self.is_selected = is_selected


class UserPage(Screen):
    ##IPFSListButton now you can access it in .kv file by referring as root.IPFSListButton
    IPFSListButton = IPFSListButton
    data_items = ObjectProperty([])
    sorted_keys = ListProperty([])
    app = ObjectProperty(None)
    transport = ObjectProperty(None)
    #tab_1=ObjectProperty(None)

    def __init__(self, **kwargs):
        super(UserPage, self).__init__(**kwargs)
        #self.tab_1.bind(minimum_height=self.layout_content.setter('height'))
        self.ids.tab_1.add_widget(f)
        
        #self.data_items = [{'name': fake.name(),  'is_selected': False} for i in range(10)]



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


    

if __name__== "__main__":
    pass
    
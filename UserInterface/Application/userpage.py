
from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.adapters.listadapter import ListAdapter
from kivy.uix.listview import ListItemButton, ListView
from kivy.properties import ObjectProperty, ListProperty, StringProperty
from faker import Faker
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivy.uix.scrollview import ScrollView
from kivy.uix.listview import ListItemButton, ListItemLabel, \
CompositeListItem, ListView
from kivy.properties import ObjectProperty
from Application.table import MTable
from os.path import sep, expanduser, isdir, dirname
from kivy.garden.filebrowser import FileBrowser
from kivy.utils import platform
from kivy.uix.popup import Popup
import subprocess

fake = Faker()


data =  [{"file_name": fake.file_name(), "stored_on": fake.date(), "location": fake.sha1() } for i in range(50)]


f = MTable(data, cols=4)





class UserPage(Screen):
    ##IPFSListButton now you can access it in .kv file by referring as root.IPFSListButton
    data_items = ObjectProperty([])
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    ipfs_address = StringProperty("")
    file = 'enter zip path or select it'
    #tab_1=ObjectProperty(None)

    def __init__(self, **kwargs):
        super(UserPage, self).__init__(**kwargs)
        #self.tab_1.bind(minimum_height=self.layout_content.setter('height'))
        self.ids.tab_1.add_widget(f)
        
        #self.data_items = [{'name': fake.name(),  'is_selected': False} for i in range(10)]

    def generate_ipfs_address(self):
        """
        This initializes IPFS and get the public and private key
        """
        subprocess.Popen(['ipfs', 'init'], stderr=subprocess.PIPE)
        subprocess.Popen(['ipfs', 'daemon&'], stderr=subprocess.PIPE)
        subprocess.Popen(['ipfs', 'config', 'Addresses.Gateway', '/ip4/0.0.0.0/tcp/9001'])
        subprocess.Popen(['ipfs', 'config', 'Addresses.API', '/ip4/0.0.0.0/tcp/5001'])
        subprocess.Popen(['ipfs', 'config','--json', 'Experimental.FilestoreEnabled', 'true'])
        __id = json.loads(subprocess.check_output(['ipfs', 'id'], stderr=subprocess.PIPE).decode())
        
        self.ipfs_address = __id["ID"]

        ##In [45]: __id = json.loads(subprocess.check_output(['cat', "/data/ipfs/config"], stderr=subprocess.PIPE).decode())
        ##In [44]: __id["Identity"]["PrivKey"]


        print ("generate ipfs address has been clicked")

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

    def open(self, textfield_id):
        self.popup = Popup(title='Test popup',
                  content=self.explorer(),
                  size_hint=(None, None), size=(600, 600))
        self.popup.open()
        self.textid = textfield_id
    
    def explorer(self):
        if platform == 'win':
            user_path = dirname(expanduser('~')) + sep + 'Documents'
        else:
            user_path = expanduser('~') + sep + 'Documents'
        browser = FileBrowser(select_string='Select',
                          favorites=[(user_path, 'Documents')])
        browser.bind(
                on_success=self._fbrowser_success,
                on_canceled=self._fbrowser_canceled)
        return browser

    def _fbrowser_canceled(self, instance):
        print ('cancelled, Close self.')
        self.popup.dismiss()

    def _fbrowser_success(self, instance):
        print(instance.selection[0])
        self.file = instance.selection[0]

        f = self.ids[self.textid]
        f.text = self.file
        self.popup.dismiss()


    

if __name__== "__main__":
    pass
    
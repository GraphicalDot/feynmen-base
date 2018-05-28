
from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooser, FileChooser
from kivy.uix.floatlayout import FloatLayout
from os.path import sep, expanduser, isdir, dirname
from kivy.garden.filebrowser import FileBrowser
from kivy.utils import platform
from kivy.uix.popup import Popup
##THe documentation for this function which were copied are present at https://kivy.org/docs/api-kivy.uix.filechooser.html
import os
import sys
def str_to_class(str):
    return getattr(sys.modules[__name__], str)



class UserRegistration(Screen):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)
    file = 'enter zip path or select it'
    
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

    def on_submit(self):
        """
        Make an api request with the data to confirm the user registraion
        After succeful registration reset the form 
        """
        


        self.go_to_login()
        return        
    
    def on_cancel(self):

        self.go_to_login()


    def go_to_login(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'Login'
        self.manager.get_screen('Login').resetForm()
        return        
        
    
   
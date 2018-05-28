from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.clock import Clock
import time
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from userpage import UserPage
from user_registration import UserRegistration
from forgot_password import ForgotPassword
from kivy.storage.jsonstore import JsonStore
import hashlib
import six




import os
from alert import Alert

store = JsonStore('feynmen.json')





class LoginPage(Screen):
    def do_login(self, loginText, passwordText):

            
        app = App.get_running_app()
        print (app.get_application_config())

        app.username = loginText
        app.password = hashlib.sha3_256(passwordText.encode("utf-8")).hexdigest()

        if app.username == "" or app.password == "":
            Alert(title='Feynmen error message', text='username and password cannot be left blank')
            return             


        if store.exists("credentials"):
            username = store["credentials"].get('username')
            password = store["credentials"].get('password') #stored passwill will be sha3_256
            print ("Credentials found in the store", username, password)

        else:
            #TODO: Make an api request here
            username = "admin"
            password = hashlib.sha3_256("1234".encode("utf-8")).hexdigest()
            store.put("credentials", username=username, password=password)



        if app.username ==  username and app.password == password:
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'User'
        else:
            Alert(title='Feynmen error message', text='username and password entered are invalid')
            return 

        app.config.read(app.get_application_config())
        app.config.write()

    def do_registration(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'UserRegistration'    

    def do_forgot_password(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'ForgotPassword'    

    def resetForm(self):
        self.ids['username'].text = ""
        self.ids['password'].text = ""


class MainApp(App):
    username = StringProperty(None)
    password = StringProperty(None)
    
    def build(self):
        manager = ScreenManager()
        manager.add_widget(LoginPage(name='Login'))
        manager.add_widget(UserPage(name='User'))
        manager.add_widget(UserRegistration(name='UserRegistration'))
        manager.add_widget(ForgotPassword(name='ForgotPassword'))
        print ("This is the username stored in the application", self.username)
        return manager

    def get_application_config(self):
        if(not self.username):
            return super(MainApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(MainApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        )


if __name__ == "__main__":
    app = MainApp()
    app.run()





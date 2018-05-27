
from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition

class UserPage(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'Login'
        self.manager.get_screen('Login').resetForm()
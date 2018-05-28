
from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition
from Application.kivy_table.table import TableView, TableColumn, TableRow, TableCell, CustomTable


class UserPage(Screen):
    def __init__(self, **kwargs):
        super(UserPage, self).__init__(**kwargs)
   
    
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'Login'
        self.manager.get_screen('Login').resetForm()

    def on_cancel(self):

        self.go_to_login()


    def go_to_login(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'Login'
        self.manager.get_screen('Login').resetForm()
        return  

    def  create_asset(self):
        print ("create asset has been clicked")


    def store_data(self):
        print ("Store data has been clicked")

    def transfer_asset(self):
        print ("Transfer asset has been clicked")

    
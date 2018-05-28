from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from os.path import sep, expanduser, isdir, dirname
from kivy.utils import platform
from kivy.uix.popup import Popup


class RootWidget(FloatLayout):
    file = 'enter zip path or select it'
    
    def open(self):
        print("doing")
        self.popup = Popup(title='Test popup',
                  content=self.explorer(),
                  size_hint=(None, None), size=(600, 600))
        self.popup.open()
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
        self.popup.dismiss()

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MainApp().run()
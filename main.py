from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.webview import WebView


class MiniWebApp(BoxLayout):
    def __init__(self, **kwargs):
        super(MiniWebApp, self).__init__(**kwargs)
        self.orientation = 'vertical'

        self.add_widget(Label(text='Mini Web App'))
        webview = WebView('https://github.com/Arvind9684/ipl.git')
        self.add_widget(webview)


class MyApp(App):
    def build(self):
        return MiniWebApp()


if __name__ == '__main__':
    MyApp().run()
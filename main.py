from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout

# comment2


class ThudGame(BoxLayout):
    pass


class ThudApp(App):
    def build(self):
        return ThudGame()


if __name__ == '__main__':
    ThudApp().run()

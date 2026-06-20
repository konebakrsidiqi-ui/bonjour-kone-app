from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        lbl = Label(
            text="Bonjour M.KONE",
            font_size="28sp",
            halign="center",
            valign="middle"
        )
        layout.add_widget(lbl)
        return layout

if __name__ == "__main__":
    MainApp().run()

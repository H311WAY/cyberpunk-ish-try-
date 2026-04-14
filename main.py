from kivy.app import App
from kivy.uix.label import Label

class NPC(App):
    def build(self):
        return Label(text="Cyberpunk NPC Android build test")

NPC().run()

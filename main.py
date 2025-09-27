import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.text import LabelBase
import os

# Try to register Papyrus font safely
papyrus_path = os.path.join(os.path.dirname(__file__), 'Papyrus.ttf')
if os.path.exists(papyrus_path):
    LabelBase.register(name='Papyrus', fn_regular=papyrus_path)
    FONT_NAME = 'Papyrus'
else:
    print("Papyrus.ttf not found, falling back to default font.")
    FONT_NAME = None  # None = use system default


class RandomScriptureApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        if FONT_NAME:
            self.button = Button(
                text="The Word of the LORD",
                font_name=FONT_NAME,
                font_size="45sp",
                size_hint_y=None,   # don’t expand vertically
                height=80        # fixed button height in pixels
            )
            self.result = Label(
                text="Your Blessing Here",
                halign="center",
                valign="top",
                font_name=FONT_NAME,
                font_size="35sp"
            )
        else:
            self.button = Button(
                text="The Word of the LORD",
                font_size="45sp",
                size_hint_y=None,   # don’t expand vertically
                height=80        # fixed button height in pixels
            )
            self.result = Label(
                text="Your Blessing Here",
                halign="center",
                valign="top",
                font_size="35sp"
            )

        self.button.bind(on_press=self.show_random_line)
        layout.add_widget(self.button)


        # ensure wrapping works
        self.result.bind(
            width=lambda *x: self.result.setter("text_size")(self.result, (self.result.width, None))
        )
        layout.add_widget(self.result)

        # Load lines once at startup
        self.lines = self.load_lines()

        return layout

    def load_lines(self):
        try:
            with open("asv_spaces.txt", "r", encoding="utf-8") as f:
                return f.readlines()[2:]  # skip first 2 lines
        except FileNotFoundError:
            return []

    def show_random_line(self, instance):
        if self.lines:
            self.result.text = random.choice(self.lines).strip()
        else:
            self.result.text = "No lines available in asv.txt"

if __name__ == "__main__":
    RandomScriptureApp().run()

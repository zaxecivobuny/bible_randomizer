import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


PAPYRUS_FONT = "Papyrus.ttf"


class RandomLineApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical", padding=20, spacing=20)

        self.button = Button(
            text="Overcome the spider's curse",
            font_name=PAPYRUS_FONT,
            font_size="45sp",
            size_hint_y=None,   # don’t expand vertically
            height=80        # fixed button height in pixels
        )
        self.button.bind(on_press=self.show_random_line)
        layout.add_widget(self.button)

        self.result = Label(
            text="Your Blessing Here",
            halign="center",
            valign="top",
            font_name=PAPYRUS_FONT,
            font_size="35sp"
        )
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
            with open("asv.txt", "r", encoding="utf-8") as f:
                return f.readlines()[2:]  # skip first 2 lines
        except FileNotFoundError:
            return []

    def show_random_line(self, instance):
        if self.lines:
            self.result.text = random.choice(self.lines).strip()
        else:
            self.result.text = "No lines available in asv.txt"

if __name__ == "__main__":
    RandomLineApp().run()

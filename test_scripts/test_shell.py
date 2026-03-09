from textual.app import App, ComposeResult
from textual.widgets import Welcome

class JarvisTUI(App):
    def compose(self)-> ComposeResult:
        yield Welcome()

    def on_button_pressed(self)->None:
        self.exit()

if __name__ == "__main__":
    app = JarvisTUI()
    app.run()
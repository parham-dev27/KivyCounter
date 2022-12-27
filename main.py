import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang.builder import Builder
from kivy.properties import ObjectProperty
from os.path import exists

Builder.load_file("ui.kv")


class Screen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.refresh()

    label = ObjectProperty(None)
    
    def refresh(self):
        if exists("num.counter"):
            try: 
                with open("num.counter", "rb") as f:
                    num = int(f.read().decode())
                    self.label.text = str(num)
            except Exception:
                pass
        

    def add(self):
        num = str(int(self.label.text) + 1)
        try:
            with open("num.counter", "wb") as f:
                f.write(num.encode())
            self.refresh()
        except Exception:
            pass

    def reset(self):
        try:
            if exists("num.counter"):
                with open("num.counter", "wb") as f:
                    f.write("0".encode())
                self.refresh()
        except Exception:
            pass
        
class CounterApp(App):
    def build(self):
        return Screen()


if __name__ == "__main__":
    CounterApp().run()
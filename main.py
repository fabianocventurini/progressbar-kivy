from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty
from kivy.clock import Clock


class MyFirstWidget(BoxLayout):
    direction = NumericProperty(1)
    valor = NumericProperty(0)

    def ativarPgBar(self):
        Clock.schedule_interval(self.incremento, 1/25)
        self.ids.btn.disabled = True

    def incremento(self, *args):
        if self.ids.progress_bar.value >= 100 and self.direction == 1:
            self.direction = -1
        if self.ids.progress_bar.value <= 0 and self.direction == -1:
            self.direction = 1
        self.ids.progress_bar.value += self.direction

    def somar(self):
        self.valor += 1
        self.ids.lbl.text = str(self.valor)


class MainApp(App):
    def build(self):
        myfirstwidget = MyFirstWidget()
        return myfirstwidget


if __name__ == '__main__':
    MainApp().run()

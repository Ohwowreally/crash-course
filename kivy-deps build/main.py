from kivy.app import App

from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class TutorialApp(App):
    def build(self):
        b =  BoxLayout(orientation='vertical')
        t = TextInput(font_size=150,
                      size_hint_y=None,
                      height=200
                      text='default')

        f = Floatlayout()
        s = Scatter()
        l = Labeel(text='default',
                   font_size=150)
        
t.bind(text=l.setter('text'))

f.add_widget(s)
s.add_widget(l)

b.add_widget(t)
b.add_widget(f)
return b

if name == 'main':
    TutorialApp().run()
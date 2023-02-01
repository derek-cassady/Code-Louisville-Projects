from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('whatever.kv')

class MyGridLayout(GridLayout):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        #print(f"Hello {name}, you like {pizza} pizza, and your favorite color is {color}!")
        #print to screen
        #self.add_widget(Label(text = f"Hello {name}, you like {pizza} pizza, and your favorite color is {color}!"))
        print(f"Hello {name}, you like {pizza} pizza, and your favorite color is {color}!")
        # Clear input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""        


class AwesomeApp(App):
    def build(self):
        return MyGridLayout()



if __name__ == '__main__':
    AwesomeApp().run()
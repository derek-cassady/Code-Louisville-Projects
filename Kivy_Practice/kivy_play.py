from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix import actionbar

runTouchApp (Builder.load_string("""

<TabbedPanel>
    size_hint: 1, 1
    pos_hint: {'center_x': .5, 'center_y': .5}
    do_default_tab: False

    TabbedPanelItem:
 
        TabbedPanelItem:
        ActionBar:
            pos_hint: {'top':.5}

        ActionView:
            use_separator: True

        ActionButton:
            text: 'Btn2' 

        TabbedPanelItem:
            text: 'tab2'
        BoxLayout:
            Label:
                text: 'Second tab content area'
            Button:
                text: 'Button that does nothing'

        TabbedPanelItem:
            text: 'tab3'
        BoxLayout:
            Label:
                text: 'third tab content area'
            Button:
                text: 'Button'

"""))
class TabbedPanelApp(App):
    def build(self):
        return TabbedPanel()


if __name__ == '__main__':
    TabbedPanelApp().run()
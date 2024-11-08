import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ConverterApp(GridLayout):
    def __init__(self, **kwargs):
        super(ConverterApp, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text='Decimal Number:'))
        self.decimal_input = TextInput(multiline=False)
        self.add_widget(self.decimal_input)

        self.convert_button = Button(text='Convert')
        self.convert_button.bind(on_press=self.convert)
        self.add_widget(self.convert_button)

        self.binary_label = Label(text='Binary:')
        self.add_widget(self.binary_label)

        self.hex_label = Label(text='Hexadecimal:')
        self.add_widget(self.hex_label)

        self.octal_label = Label(text='Octal:')
        self.add_widget(self.octal_label)

    def convert(self, instance):
        try:
            decimal_number = int(self.decimal_input.text)
            binary_number = bin(decimal_number)[2:]  # Remove '0b' prefix
            hex_number = hex(decimal_number)[2:].upper()  # Remove '0x' prefix and convert to uppercase
            octal_number = oct(decimal_number)[2:]  # Remove '0o' prefix
            
            self.binary_label.text = f'Binary: {binary_number}'
            self.hex_label.text = f'Hexadecimal: {hex_number}'
            self.octal_label.text = f'Octal: {octal_number}'
        except ValueError:
            self.binary_label.text = 'Binary: Invalid input'
            self.hex_label.text = 'Hexadecimal: Invalid input'
            self.octal_label.text = 'Octal: Invalid input'

class MyApp(App):
    def build(self):
        return ConverterApp()

if __name__ == '__main__':
    MyApp().run()

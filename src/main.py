from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.core.window import Window

from converter import mxn_to_usd, usd_to_mxn, mxn_to_eur, eur_to_mxn


# Tamaño de la ventana
Window.size = (400, 500)

class ConversorApp(App):
    """Clase principal de la aplicación Kivy"""

    def build(self):
        """Construye la interfaz gráfica"""
        # Contenedor principal
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        # Título
        titulo = Label(text='Conversor de Monedas', size_hint_y=0.15, font_size='24sp', bold=True)
        main_layout.add_widget(titulo)
        # Layout para inputs 
        input_layout = GridLayout(cols=1, spacing=10, size_hint_y=0.35)
        # Label: Cantidad
        label_cantidad = Label(text='Cantidad:', size_hint_y=0.2)
        input_layout.add_widget(label_cantidad)
        # TextInput para cantidad
        self.cantidad_input = TextInput(hint_text='Ingresa la cantidad', input_filter='float', multiline=False, size_hint_y=0.3)
        input_layout.add_widget(self.cantidad_input)
        # Label: Conversión
        label_conversion = Label(text='Tipo de conversión:', size_hint_y=0.2)
        input_layout.add_widget(label_conversion)
        # Spinner para seleccionar conversión
        self.spinner_conversion = Spinner(text='Selecciona', values=('MXN > USD', 'USD > MXN', 'MXN > EUR', 'EUR > MXN'), size_hint_y=0.3)
        input_layout.add_widget(self.spinner_conversion)

        main_layout.add_widget(input_layout)
        # Botón Convertir
        boton_convertir = Button(text='Convertir', size_hint_y=0.15, background_color=(0.2, 0.6, 0.2, 1))
        boton_convertir.bind(on_press=self.realizar_conversion)
        main_layout.add_widget(boton_convertir)
        # Resultado
        self.resultado_label = Label(text='', size_hint_y=0.2, font_size='18sp', bold=True, color=(0, 0, 0, 1))
        main_layout.add_widget(self.resultado_label)
        # Botón Limpiar
        boton_limpiar = Button(text='Limpiar', size_hint_y=0.15, background_color=(0.2, 0.2, 0.6, 1))
        boton_limpiar.bind(on_press=self.limpiar)
        main_layout.add_widget(boton_limpiar)
        return main_layout

    def realizar_conversion(self, instance):
        """Realiza la conversión de moneda"""
        # Obtener valor ingresado
        valor_texto = self.cantidad_input.text.strip()
        tipo_conversion = self.spinner_conversion.text
        # Validar entrada
        if not valor_texto:
            self.resultado_label.text = 'ERROR: Ingresa una cantidad'
            self.resultado_label.color = (1, 0, 0, 1)  # Rojo
            return
        if tipo_conversion == 'Selecciona':
            self.resultado_label.text = 'ERROR: Selecciona una conversión'
            self.resultado_label.color = (1, 0, 0, 1)
            return
        try:
            cantidad = float(valor_texto)
            if cantidad < 0:
                self.resultado_label.text = 'ERROR: Cantidad debe ser positiva'
                self.resultado_label.color = (1, 0, 0, 1)
                return
            # Realizar conversión
            if tipo_conversion == 'MXN > USD':
                resultado = mxn_to_usd(cantidad)
                mensaje = f'{cantidad} MXN = {resultado} USD'
            elif tipo_conversion == 'USD > MXN':
                resultado = usd_to_mxn(cantidad)
                mensaje = f'{cantidad} USD = {resultado} MXN'
            elif tipo_conversion == 'MXN > EUR':
                resultado = mxn_to_eur(cantidad)
                mensaje = f'{cantidad} MXN = {resultado} EUR'
            elif tipo_conversion == 'EUR > MXN':
                resultado = eur_to_mxn(cantidad)
                mensaje = f'{cantidad} EUR = {resultado} MXN'
            else:
                mensaje = 'ERROR: Conversión no válida'
                self.resultado_label.color = (1, 0, 0, 1)
                self.resultado_label.text = mensaje
                return
            # Mostrar resultado
            self.resultado_label.text = mensaje
            self.resultado_label.color = (0, 0.7, 0, 1)  # Verde
        except ValueError:
            self.resultado_label.text = 'ERROR: Ingresa un número válido'
            self.resultado_label.color = (1, 0, 0, 1)  # Rojo

    def limpiar(self, instance):
        """Limpia los campos de entrada"""
        self.cantidad_input.text = ''
        self.spinner_conversion.text = 'Selecciona'
        self.resultado_label.text = ''

if __name__ == '__main__':
    ConversorApp().run()
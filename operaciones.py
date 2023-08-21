import math
import numpy as np

class Menu:
    def mostrar(self):
        print("Seleccione una operación:")
        print("1. Operaciones Básicas")
        print("2. Operaciones Trigonométricas")
        print("3. Operaciones Avanzadas")
        print("4. Operaciones Estadísticas")
        print("5. Salir")

class OperacionesBasicas:
    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "No se puede dividir por cero"

class OperacionesTrigonometricas:
    def seno(self, angulo):
        return math.sin(math.radians(angulo))

    def coseno(self, angulo):
        return math.cos(math.radians(angulo))

class OperacionesAvanzadas:
    def exponente(self, base, exponente):
        return base ** exponente

class OperacionesEstadisticas:
    def media(self, datos):
        return np.mean(datos)

    def mediana(self, datos):
        return np.median(datos)

    def desviacion_estandar(self, datos):
        return np.std(datos)
    
class CalculadoraCientifica:
    def __init__(self):
        self.op_basicas = OperacionesBasicas()
        self.op_trig = OperacionesTrigonometricas()
        self.op_avanzadas = OperacionesAvanzadas()
        self.op_estadisticas = OperacionesEstadisticas()

    def ejecutar(self):
        menu = Menu()

        while True:
            menu.mostrar()
            opcion = input("Ingrese el número de la operación deseada: ")

            if opcion == '5':
                print("¡Hasta luego!")
                break

            if opcion == '1':
                self.realizar_operaciones_basicas()
            elif opcion == '2':
                self.realizar_operaciones_trigonometricas()
            elif opcion == '3':
                self.realizar_operaciones_avanzadas()
            elif opcion == '4':
                self.realizar_operaciones_estadisticas()
            else:
                print("Opción inválida. Por favor, seleccione una opción válida.")

    def realizar_operaciones_trigonometricas(self):
        try:
            angulo = float(input("Ingrese el valor del ángulo: "))
            print("Seleccione una operación trigonométrica:")
            print("1. Seno")
            print("2. Coseno")
            op = input("Ingrese el número de la operación deseada: ")

            if op == '1':
                print("Resultado:", self.op_trig.seno(angulo))
            elif op == '2':
                print("Resultado:", self.op_trig.coseno(angulo))
            else:
                print("Operación inválida.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un valor numérico.")

    def realizar_operaciones_avanzadas(self):
        try:
            base = float(input("Ingrese la base: "))
            exponente = float(input("Ingrese el exponente: "))
            print("Seleccione una operación avanzada:")
            print("1. Exponente")
            op = input("Ingrese el número de la operación deseada: ")

            if op == '1':
                print("Resultado:", self.op_avanzadas.exponente(base, exponente))
            else:
                print("Operación inválida.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese valores numéricos.")

    def realizar_operaciones_estadisticas(self):
        try:
            datos = [float(x) for x in input("Ingrese los datos separados por espacios: ").split()]
            print("Seleccione una operación estadística:")
            print("1. Media")
            print("2. Mediana")
            print("3. Desviación Estándar")
            op = input("Ingrese el número de la operación deseada: ")

            if op == '1':
                media = self.op_estadisticas.media(datos)
                print("Media:", media)
            elif op == '2':
                mediana = self.op_estadisticas.mediana(datos)
                print("Mediana:", mediana)
            elif op == '3':
                desviacion = self.op_estadisticas.desviacion_estandar(datos)
                print("Desviación Estándar:", desviacion)
            else:
                print("Operación inválida.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese valores numéricos.")

if __name__ == "__main__":
    calc = CalculadoraCientifica()
    calc.ejecutar()


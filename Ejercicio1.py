if __name__ == '__main__':
    print("Ingrese 2 valores para ser operados:")
a = int(input())
b = int(input())   
class Calculadora:
    def sumar (a, b):
        return a + b
    def restar (a, b):
        return a - b  
    def multiplicar (a, b):
        return a * b
    def dividir (a, b):
        return a / b 
print("Elija la operacion a realizar:")
print("Suma: 1\nResta: 2\nMultiplicacion: 3\nDivision: 4")
operacion = int(input())
class Seleccion_Operacion:
    def operacion():
        if operacion == 1:
            print("El resultado es", Calculadora.sumar(a, b))
        elif operacion == 2:
            print("El resultado es", Calculadora.restar(a, b))
        elif operacion == 3:
            print("El resultado es", Calculadora.multiplicar(a, b))
        elif operacion == 4:
            print("El resultado es", Calculadora.dividir(a, b))
        else:
            print("Operacion no valida")
Seleccion_Operacion.operacion()





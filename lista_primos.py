if __name__ == '__main__':
    print("Ingrese los numeros separados por espacio:")
    entrada = input()
    lista = [int(x) for x in entrada.split()]
class Numeros:
    def es_primo(numero):
        if numero > 1:
            es_primo = True
            for i in range(2, numero):
                if numero % i == 0:
                    es_primo = False
            if es_primo == True:
                return True
            else:
                return False
        else:
            return False
class Seleccion_Primos:
    def mostrar():
        primos = []
        for n in lista:
            if Numeros.es_primo(n):
                primos.append(n)
        print("Los numeros primos son:", primos)

Seleccion_Primos.mostrar()

# Se require de la funcion random
import random


class Codebreaker:

    # Compara el valor ingresado por terminal con el generado
    def adivinar(self, truenumber, numero=None):
        if len(numero) != 4 or Codebreaker.repetido(numero) or Codebreaker.digito(numero):
            return "Error"

        resultado = ''
        for x in range(len(numero)):
            if truenumber[x] == numero[x]:
                resultado += 'X'

            elif numero[x] in truenumber:
                resultado += '_'
            else:
                resultado += '-'
        return resultado
    
    # Genera un numero aleatorio el cual hay que adivinar.
    def generar():
        numeros = list(range(10))  # Genera una lista del 0 al 9
        random.shuffle(numeros)  # Reordena la lista de digitos
        numero = numeros[:4]  # Asigna los cuatro primeros digitos
        return ''.join(map(str, numero))
    
    # Busca un caracter se repite en el valor ingresado
    def repetido(numero):
        for caracter in numero:
            if numero.count(caracter) > 1:
                return True
        return False
    
    # Verifica que seal solo numeros
    def digito(entrada):
        if entrada.isdigit():
            return False
        else:
            return True
        
    # Lee el archivo que tiene el texto con las instrucciones del juego
    def instrucciones(archivo_texto):
        with open(archivo_texto, 'r') as archivo:
            contenido = archivo.read()
            return contenido

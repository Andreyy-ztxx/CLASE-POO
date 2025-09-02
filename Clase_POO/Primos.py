#TAREA DE NUMEROS PRIMOS

def Primos(numero):
    if (numero < 2):
        return False
    for i in range (2, numero):
        if (numero % i == 0):
            return False
        return True

numer = 2
contador = 0
contador_primos= 0


       

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

while (contador < 1000): 

    if (Primos(numer)):
        print (numer) 
        contador_primos += 1
    contador += 1
    numer += 1
    if (contador_primos == 50):
        break
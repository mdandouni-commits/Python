# Python
[Practica1.py](https://github.com/user-attachments/files/27100312/Practica1.py)
dni = input("Posa el DN: ") # Pregunta el DNI
preu = input("Posa el preu de l'article: ") # Pregunta els preus
descompte = input("Posa el percentatge de descompte: ") # Pregunta el % de descompte
iva = input("Introdueix el percentatge d'IVA: ") # Pregunta el IVA

#Tot aquesta part transforma el (preu, descompte e iva) en float (numeros amb decimal)
preu = float(preu) 
descompte = float(descompte)
iva = float(iva)

#Calcula el preu de desconte
preu_descompte = preu - (preu * descompte / 100)
#Calcula el preu final
preu_final = preu_descompte + (preu_descompte * iva / 100)
#Pinta el DNI i el IVA amb descompte
print(dni)
print(preu_final, 1)
[Calculadora.py](https://github.com/user-attachments/files/27100334/Calculadora.py)
import random     # Pone um rango aleatorio
maquina = random.randint(1,101)   # Pone um rango aleatorio entre 1 a 100
user = 0     # Numero que pone el usuario
while user != maquina:   # Se repite infinitamente mientras que el numero no sea igual
    user = int(input("Empieza el juego pon un numero del 1 al 100:")) # Lee lo que escrives
    if user > maquina:   # El numero del user es mayor a maquina
        print("Es mas pequeño") # Te dice que es pequeño
    elif user < maquina: # El numero del user es menor a maquina
        print("Es mas grande") # Te dice que es grande
    else:  
        print("Ganador")  # Te dice que as ganado 
        print("Has ganado pero nos volveremos a ver") # Mensaje final

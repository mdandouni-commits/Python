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
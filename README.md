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

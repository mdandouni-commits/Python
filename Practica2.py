 Llistes per guardar els noms dels productes i els seus preus
productes = []
preus = []

print("Introdueix els productes de la llibreria (mínim 8)")
print("Escriu '$' com a nom per acabar o un preu <= 0")

# --- INTRODUCCIÓ DE PRODUCTES ---
while True:
    nom = input("Nom de l'article: ")

    # Condició de sortida per nom especial
    if nom == "$":
        if len(productes) >= 8:
            break
        else:
            print("Has d'introduir almenys 8 productes.")
            continue

    try:
        preu = float(input("Preu: "))
    except:
        print("Preu no vàlid.")
        continue

    # Condició de sortida per preu no vàlid
    if preu <= 0:
        if len(productes) >= 8:
            break
        else:
            print("Has d'introduir almenys 8 productes.")
            continue

    # Afegim el producte a les llistes
    productes.append(nom)
    preus.append(preu)

# --- MOSTRAR CATÀLEG ---
print("\nLLIBRERIA ESCOLAR")
print("-------------------------")

for i in range(len(productes)):
    print(f"{i+1} - {productes[i]:15} {preus[i]:.2f}€")

print("-------------------------")
print("0 - PAGAR")

# --- PROCÉS DE COMPRA ---
total = 0

while True:
    try:
        opcio = int(input("Quin article vols comprar? "))
    except:
        print("Opció no vàlida.")
        continue

    if opcio == 0:
        break

    # Comprovem que l'opció sigui correcta
    if 1 <= opcio <= len(productes):
        total += preus[opcio - 1]
        print(f"Has afegit: {productes[opcio - 1]}")
    else:
        print("Opció no vàlida.")

# --- MOSTRAR TOTAL ---
print(f"\nImport total a pagar: {total:.2f}€")
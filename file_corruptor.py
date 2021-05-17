from os import rename
from random import choice
from string import ascii_letters, digits


"""
1 KiloOctet (ko) = 1 000 octets
1 MégaOctet (Mo) = 1 000 000 octets
1 GigaOctet (Go) = 1 000 000 000 octets
"""

caractere = ["ø", "#", "¤", "£", "$", "§", "&", "¥", "¨", "á", "ð", "ÿ", "¶", "µ"]
for char in digits:
    caractere.append(digits)
    
for char in ascii_letters:
    caractere.append(digits)
    
ecriture = ""

print("Quel type de fichier voulez-vous corrompre?\n")

type_de_fichier = input("fichier.")

print("""\nQuelle taille voulez-vous que le fichier aie?

Exemple : 
1 KiloOctet (ko) = 1 000 octets
1 MégaOctet (Mo) = 1 000 000 octets
1 GigaOctet (Go) = 1 000 000 000 octets

""")
taille_du_fichier = input("Taille [en octets]: ")
taille = taille_du_fichier.split(" ")
taille_du_fichier = ""
for element in taille:
    taille_du_fichier += element
    


for i in range(int(taille_du_fichier)):
    ecriture += choice(caractere)

with open('fichier.txt', "w") as f :
    f.write(ecriture)
    f.close()

rename('fichier.txt', f'fichier.{type_de_fichier}')

input("\nFichier créé ;)")


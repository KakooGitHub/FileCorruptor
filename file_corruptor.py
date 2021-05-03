from os import rename

"""
1 KiloOctet (ko) = 1 000 octets
1 MégaOctet (Mo) = 1 000 000 octets
1 GigaOctet (Go) = 1 000 000 000 octets
"""

caractere = "ø"
ecriture = ""

print("Quel type de fichier voulez-vous corrompre?\n")

type_de_fichier = input("fichier.")

print("""\nQuelle taille voulez-vous que le fichier aie?

Exemple : 
1 KiloOctet (ko) = 1 000 octets
1 MégaOctet (Mo) = 1 000 000 octets
1 GigaOctet (Go) = 1 000 000 000 octets

""")
taille_du_fichier = input("Taille [en octets, sans espaces]: ")

for i in range(int(taille_du_fichier)):
    ecriture += caractere

with open('fichier.txt', "w") as f :
    f.write(ecriture)
    f.close()

rename('fichier.txt', f'fichier.{type_de_fichier}')

input("\nFichier créé ;)")


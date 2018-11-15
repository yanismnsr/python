#ce programme teste la fonction de chiffrement vigenere avec l'exemple donné sur wikipédia


from cryptographie.vigenere import *

texte = 'j\'adore ecouter la radio toute la journée'
cle = 'musique'
chiffre = vigenere(texte, cle)
print("le chiffrement de la chaine de caractères \"", texte, "\" est :")
print(chiffre)

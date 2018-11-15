#fonction qui effectue un chiffrement vigenère 
#la méthode est expliquée dans cette page https://fr.wikipedia.org/wiki/Chiffre_de_Vigen%C3%A8re


def vigenere(texte, cle):
    i = 0
    chiffre = ''
    while i < len(texte):
        j = 0
        while i < len(texte) and j < len(cle): 
            if 'a' <= texte[i] <= 'z':
                posCol = ord(texte[i]) - ord('a')
                carDecode = ((ord(cle[j]) + posCol) - ord('a'))%26 + ord('a')
                j += 1
                i += 1
                chiffre += chr(carDecode)
            else :
                chiffre += texte[i]
                i += 1
    return chiffre

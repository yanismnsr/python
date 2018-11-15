from cryptographie.cesar import *

#fonction qui effectue le chiffrement ROT13
def chiffrement_ROT13(ch):
    return chiffre_cesar(ch,13)


#fonction qui effectue le dechiffrement ROT13
def dechiffrement_ROT13(ch):
    return dechiffre_cesar(ch,13)

if __name__ == "__main__" :
    print(chiffrement_ROT13("yanis"))

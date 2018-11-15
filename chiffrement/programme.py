#le programme qui appelle les modules cesar et rot13 qui sont dans le package cryptographie 


#from cryptographie.cesar import *
from cryptographie.rot13 import *

#message = input("donnez un message ")
#dico_codes = {}

#print ("votre message est ", message)
#for i in range(1,26) :
#    code = ''
#    for j in range(len(message)) :
#        code += chiffre_cesar(message[j],i)
#    dico_codes [i] = code 


#print (dico_codes)

print("ce programme affiche le chiffrement de la chaine 'hello world !' selon le chiffrement ROT13")
chaine = "hello world !"
print (dechiffrement_ROT13(chaine))

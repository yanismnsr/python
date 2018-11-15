#######################
### le jeu de devin ###
#######################
#l'ordinateur essaie de deviner un nombre entre 1 et 100 que vous reteniez dans votre tete en 7 essaies 

#code
essaie = 0
found = False 
debut = 1
fin = 100
while not found :
    milieu = (debut + fin)//2
    print ('le nombre est-il égale, supérieur ou inférieur à ' + str(milieu) + '?')
    print ('répondre par e si égale, s si votre nombre est supérieur et i si votre nombre est inférieur')
    #saisie controlée 
    answer = input()
    while answer != 's' and answer != 'i' and answer != 'e':
        print ('répondre par e si égale, s si votre nombre est supérieur et i si votre nombre est inférieur')
        answer = input()
    if answer == 's':
        debut = milieu + 1
    elif answer == 'i':
        fin = milieu - 1
    else :
        found = True 
    essaie += 1
        

print ('j\'ai trouvé la réponse en ' + str(essaie) + ' essaies')
    
  
  
#######################
###      racine     ###
#######################
#fonction qui permet de calculer la racine d'une nombre donné en paramètre, en utilisant le recherche dichotomique 
from math import *

def sqrt(val):
    found = False
    debut = 0.0
    fin = val
    while not found :
        milieu = (debut+fin)/2
        if isclose(milieu*milieu,val) :
            found = True 
        elif milieu*milieu < val:
            debut = milieu
        else:
            fin = milieu
    return milieu


print(round(sqrt (9),8))


######################
###  same letters  ###
######################
#fonctions qui testent si 2 chaines de carachtères utilisent les meme lettres 

#fonction qui teste l'existance d'un caractère dans une chaine 
def existCarChaine(char,chaine):
    i = 0
    while i < len(chaine):
        if char == chaine[i]:
            return True
        i += 1
    return False
    
    
#fonction qui teste l'existance de tous les caractères d'une chaine dans l'autre 
def existChCh(chaine1, chaine2):
    i = 0
    while i < len(chaine1):
        if not existCarChaine(chaine1[i],chaine2):
            return False 
        i +=1
    return True 

    
#fonction qui teste si 2 chaines utilisent les memes caractères 
def meme_chaine(chaine1,chaine2):
    if not existChCh(chaine1,chaine2) or not existChCh(chaine2,chaine1):
        return False 
    return True 


#algorithme principale 
meme_chaine('yanis','sinay')





##########################
### same letters (tri) ###
##########################
#fonction qui teste si 2 chaine triées utilisent les memes caractères 

def meme_caractere_tri(chaine1,chaine2):
    i = 0
    j = 0
    while i < len(chaine1) and j < len(chaine2):
        if chaine1[i] != chaine2[j]:
            return False 
        while i< len(chaine1)-1 and chaine1[i] == chaine1[i+1]:
            i +=1
        while j < len(chaine2)-1 and chaine2[j] == chaine2[j+1] :
            j += 1
        i += 1
        j += 1
    if i == len(chaine1) and j == len(chaine2) :
        return True 
    else :
        return False
    
meme_caractere_tri('aaaabbbbbbbccccccdkkkkkrrrrr','aaabccccddkkkkr')

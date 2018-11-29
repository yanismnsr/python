###############################################################
######################## exercice 1 ###########################
###############################################################

#fonction qui teste si un caractère correspond à un nicliotide

def est_base(val) :
    return val == 'A' or val == 'C' or val == 'G' or val == 'T'
# complexité constante


###############################################################
######################## exercice 2 ###########################
###############################################################

#fonction qui teste si une chaine de caractère est une chaine d'adn
def est_adn(chaine) :
    i = 0
    while i < len(chaine) :
        if not est_base(chaine[i]):
            return False
        i += 1
    return True
# complexité linéaire



###############################################################
######################## exercice 3 ###########################
###############################################################

#fonction qui retourne un dictionnaire contenant le pourcentage de chaque nicliotide dans une chaine d'adn
def pourcentage_bases(chaine):
    i = 0
    dico = {'A':0 , 'G':0, 'C':0 , 'T':0}
    while i < len(chaine) :
        dico[chaine[i]] += 1
        i += 1
    dico ['A'] = dico['A']*100/len(chaine)
    dico ['G'] = dico['G']*100/len(chaine)
    dico ['C'] = dico['C']*100/len(chaine)
    dico ['T'] = dico['T']*100/len(chaine)
    return dico
#complexité linéaire


###############################################################
######################## exercice 4 ###########################
###############################################################

#programme qui fait une saisir controlée de façon à ce qu'on lui donne une chaine d'adn de plus de 8 caractère
#et affiche le pourcentage de chaque nicliotide de cette chaine 

#saisie répétée 
print("donner une séquence d'adn de minimum 8 bases")
chaine = input()
while not est_adn(chaine) or len(chaine)<8:
    print("donner une séquence d'adn de minimum 8 bases")
    chaine = input()

#affichage des pourcentages
print("voici le pourcentage de chaque base")
print(pourcentage_bases(chaine))




###############################################################
######################## exercice 5 ###########################
###############################################################

#fonction qui teste si une sequence adn est contenue dans une autre 
def contient_sequence(adn, sequence):
    if len(sequence)>len(adn):
        return 
    i = 0
    while i < len(adn):
        j = 0
        while i+j < len(adn) and j < len(sequence) and adn[i+j] == sequence[j] :
            j += 1
        if j == len(sequence) :
            return True
        i+=1
    return False
#complexité quadratique

print(contient_sequence("AAAAAAAATCAGGGGGG", "ATCAG"))






###############################################################
######################## exercice 6 ###########################
###############################################################

#fonction qui teste si une sequence est contenue dans un adn
#cette fonction retourne True si la sequence correspont à 80% à la séquence trouvée dans l'adn
def contient_sequence_similaire(adn, sequence):
    if len(sequence)>len(adn):
        return 
    i = 0
    while i < len(adn):
        j = 0
        lSim = 0
        lNSim = 0
        if adn[i] == sequence[0] :
            while i+j < len(adn) and j < len(sequence) :
                if adn[i+j] == sequence[j]:
                    lSim += 1
                j += 1
            pSim = lSim*100/len(sequence)
            if pSim >= 80 :
                return True
        i+=1
    return False
#complexité quadratique


print(contient_sequence_similaire("AAATCGTT", "AACGT"))


###############################################################
######################## exercice 7 ###########################
###############################################################

#fonction qui teste si une sequence adn est contenue dans un adn
#cette sequence peut se trouver dans 2 parties différentes de l'adn mais pas plus 
def contient_deux_parties(adn, sequence) :
    i = 0
    while i < len(adn) :
        j = 0
        nbParties = 0
        if adn[i] == sequence[0] :
            k = i
            nbParties += 1
            while k < len(adn) :
                while j < len(sequence) and adn[k] == sequence[j] :
                    j+=1
                    k+=1
                init = 0
                while j < len(sequence) and adn[k] != sequence[j] :
                    k += 1
                    init = 1
                if init == 1 :
                    nbParties += 1
            if j == len(sequence) and nbParties <= 2:
                return True
        i += 1
    return False
                

print("teste de la fonction contient_deux_parties")
print(contient_deux_parties("AAATGCCGTAAATC", "AATGAAATC"))

            


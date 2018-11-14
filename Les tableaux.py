#fonction permettant de creer un tableau de taille n contenant la valeur val en utilisant append 

def create_table_algo_append(n, val):
    i = 0
    tab = []
    while i < n:
        tab.append(val)
        i+=1
    return tab



#test de la rapidité de la fonction en créant 200 tableau de taille 0,100,200,500,1000,2000,5000,10000

from time import *

tabDeValeurs=[0,100,200,500,1000,2000,5000,10000]

tabChrono = []
j = 0
while j < len(tabDeValeurs):
    n = tabDeValeurs[j]
    i = 0
    somme = 0
    while i < 200 :
        tic = time()
        create_table_algo_append(n,1)
        i += 1
        tac = time()
        somme += tac-tic
    moyenne = somme/200
    j += 1
    tabChrono.append(str(round(moyenne*1000,2)))
    
print (tabChrono)



#fonction permettant de creer un tableau de taille n contenant la valeur val en utilisant insert 

def create_table_algo_insert(n, val):
    i = 0
    tab = []
    while i < n :
        tab.insert(0, val)
        i += 1
    return tab
    
    
    
    
    
#test de la rapidité de la fonction avec la meme méthode 

tabDeValeurs=[0,100,200,500,1000,2000,5000,10000]

tabChronoInsert = []
j = 0
while j < len(tabDeValeurs):
    tic = time()
    n = tabDeValeurs[j]
    i = 0
    somme = 0
    while i < 200 :
        tic = time()
        create_table_algo_insert(n,1)
        i += 1
        tac = time()
        somme += tac - tic
    moyenne = somme/200
    j += 1
    tabChronoInsert.append(str(round(moyenne*1000,2)))
    
print (tabChronoInsert)


#fonction permettant de copier un tableau 

#version avec append 
def copy_tab_algo(tab):
    i = 0
    copie = []
    while i < len(tab):
        copie.append(tab[i])
        i +=1
    return copie

#version avec insert
def copy_tab_algo2(tab):
    i = len(tab)-1
    copie = []
    while i >=0 :
        copie.insert(0,tab[i])
        i -= 1
    return copie 



#tester la rapidité des deux fonctions pour les comparer 

tabDeValeurs=[0,100,200,500,1000,2000,5000,10000]

dico1 = {}
dico2 = {}
i = 0 
while i < len(tabDeValeurs):
    tabTest = create_table_algo_append(tabDeValeurs[i], 0)
    j = 0
    somme = 0
    while j < 200 :                                           #test de la rapidité de la copie en utilisant append 
        tic = time()
        copy_tab_algo(tabTest)
        tac = time()
        j += 1
        somme += tac - tic
    moyenne = somme/200
    dico1[tabDeValeurs[i]] = round(moyenne*1000, 2)
    j = 0
    somme = 0
    while j < 200 :                                           #test de la rapidité de la copie en utilisant insert
        tic = time()
        copy_tab_algo2(tabTest)
        tac = time()
        j += 1
        somme += tac - tic
    moyenne = somme/200
    dico2[tabDeValeurs[i]] = round(moyenne*1000,2)
    i += 1
    
print(dico1)
print(dico2)

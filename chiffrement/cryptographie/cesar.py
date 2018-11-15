#chiffrement cesar 
def chiffre_cesar(m, n):
    m = m.lower()
    c = ""
    for mi in m:
        if(97 <= ord(mi) <= 122):
            c += chr( (ord(mi) + n - ord('a')) % 26 + ord('a'))
        else:
            c += mi
    return c


#dechiffrement cesar 
def dechiffre_cesar(c, n):

    c = c.lower()
    m = ""
    for ci in c:
        if(97 <= ord(ci) <= 122):
            m += chr( (ord(ci) - n - ord('a')) % 26 + ord('a'))
        else:
            m += ci
    return m



#la partie du code executée si seulement
#le script cesar.py est excuté

if __name__ == '__main__' :
    print(dechiffre_cesar("Le script cesar.py est execute !",10))

mots ='FORGES COFFRET FLORES NOIRCIR CLAPET ASTRILD CREPES NOIRCIR HANSES POIGNET'
a = 0
b = len(mots)
titi=''
for i in range(0, int(len(mots)/2)):
    if mots[i] == ' ':
        titi = titi + mots[abs(a-b)]
    a+=2
    b-=1

print(titi)
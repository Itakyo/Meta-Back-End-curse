 #AL UNIR CONJUNTOS NO SE REPITEN VALORES!!
 #set is not a sequence, it doesn't contain an ordered index of all elements inside
set1 = {1, 2, 3, 4, 5}
print(set1)

set1.add(6)#Agregar en la ultima posicion del set
print(set1)

set1.remove(2)#funcion de remover
print(set1)

set1.discard(2)#funcion de remover
print(set1)

set2={4, 5, 6, 7, 8}


print(set1.union(set2)) #AL UNIR CONJUNTOS NO SE REPITEN VALORES!!! FORMA1
print(set1 | set2) #AL UNIR CONJUNTOS NO SE REPITEN VALORES!!!  FORMA2

print(set1.intersection(set2))#METHOD TO SEE VALUES THAT WERE REPEATED FORMA1
print(set1 & set2)#METHOD TO SEE VALUES THAT WERE REPEATED FORMA2

print(set1.difference(set2)) # this should give me back all the elements that are only in set1 and not in set2
print(set1 - set2) # this should give me back all the elements that are only in set1 and not in set2

print(set1.symmetric_difference(set2)) # all of the elements that are present in set A. Or set B. But not in both sets
print(set1 ^ set2) # all of the elements that are present in set A. Or set B. But not in both sets

#!!!!print(set1[0])!!!!#set is not a sequence, it doesn't contain an ordered index of all elements inside
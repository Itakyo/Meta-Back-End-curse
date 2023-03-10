#Lists are a sequence of one or more different or similar datatypes.
#A list in Python is essentially a dynamic array that can hold any datatyp


list1 = [1, 2, 3, 4, 5]
list2 = ["A", "B", "C", "D", "E"]
list3 = ["Hello", 1, True, 40, 15.22]
list4= [1, [2,3], 2, 3]
list5 = [11, 22, 33, 44, 55]
list6 = [6, 7, 8, 9, 10, 1]

print(*list4)
print(*list4, sep=" ")

list1.insert(4,6)#Agreegar items escogiendo el indice de preferencia (4(ubicacion segun indice),6(valor a agregar))
print (list1, sep="  ")

list2.append("F")#Agreegar items forma2
print (list2)

list3.extend(["World", 6, 7])#Agreegar items forma3
print (list3)


list6.pop(5)#remover segun la ubicacion por indice recrodad que inicia en 0 forma1
print (list6)

del list5 [2]#remover segun la ubicacion por indice recrodad que inicia en 0 forma2
print (list5)

for i in list1:
    print("Value:",i)

#Por practicas de porgramacion se definen en parentecis
from operator import index


tuple = (1, "String", 4.5, True)
print(tuple[1])#imprime el vlaor ubbicado en el indice 1
print(type(tuple))
print(tuple.count("String"))#Cuenta la cantodad de resultados con el valor indicado en este caso "String"
print(tuple.index(4.5))#imprime la ubiucacion inidice donde se encuentra el valor dado

tuple [0]=5 #!!!IMPOSIBLE HACER ESTO EN UNA TUPLA NO SE PUEDEN MODIFICAR

for x in tuple:
    print(x)#imprime todos los valors dentro de la tupla
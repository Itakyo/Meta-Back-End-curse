from ast import arg
##with args, you could pass in any amount of non-keyword variables. With the kwargs, 
# you can pass in any amount of keyword arguments. 

###ARGS
def sum_of (*args):
    sum = 0
    for x in args:
        sum+= x
    return sum    


print (sum_of(4,5,6))    

######KWARGS


def sum_in(**kwargs):
    suma=0
    for k, v in kwargs.items():
        suma+= v
    return round(suma, 2) 

print (sum_in(coffe=2.99, cake=4.55, jiuce=2.99))   



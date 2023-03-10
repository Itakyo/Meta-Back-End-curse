#he purpose of scope is to protect the variable

#globar_scope

my_global = 10

def fn1():
    enclosed_v=8

    def fn2():
        local_V= 5
        print("Acces to global", my_global)
        print("Access  to enclosed", enclosed_v)
        print("Access  to enclosed", local_V)
    fn2()    
fn1()    
        
#print("Cant accces local", local_v)    #is not poible have to access a this V due to is not global vairable like my_global =10
#print("Cant accces enclosed", enclosed_v) # is not poible have to access a this V due to is not global vairable like my_global =10



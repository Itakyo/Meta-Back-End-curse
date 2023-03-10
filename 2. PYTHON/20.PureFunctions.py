#Pure functions will help prevent changes on the global scope ensuring data stays reliable. 
#Now I think it's time to offer you a step-by-step demonstration in VS Code of how to alter 
# a normal function to a pure function. Pure functions are especially useful because they 
# are easier to read, better to debug, and more consistent. 

my_list = [1,2,3]

def add_to_list (lst, item):
    nl = lst.copy()
    nl.append(item)
    return nl

new_list = add_to_list(my_list, 4 )

print(my_list)
print(new_list)
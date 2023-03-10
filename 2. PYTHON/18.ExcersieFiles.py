import random

f = open("petnames.txt", "r")
f_content=f.read()
print(f_content) 
f_content_list = f_content.split("\n") ###converti a lista
print(f_content_list)
print(random.choice(f_content_list))
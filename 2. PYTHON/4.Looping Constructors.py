#Music Taht spund again ansd aginn

Nombre = "Daniel"

for i in Nombre:
    print(i +"..."+Nombre )

for n in range(5+1):
    print(n, "Looping")

###### using the list##########   

favorites = ["Creme Brulee", "Apple Pie", "Churros","Tiramisu", "Chocolate Cake"]

for x in favorites:
     print("I like this ", x)  


count = 0

while count < len(favorites):
    print("I hate this", favorites[count])
    count +=1
    


for idx, item in enumerate (favorites):
     print(idx, item)  


for dessert in favorites:
    if dessert == 'Churros':
        print('Yes! One of my favorite desserts is', dessert) 

for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert) 
else:
    print('No sorry, that dessert is not on my list')  


for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert)
        break 
else:
    print('No sorry, not a dessert on my list')



#Continue
#Similar to break, continue can be used to control the iteration of the loop. The key difference is that it can allow 
# you to skip over a section of the loop but then continue on with the rest. If you change your code to this, you will
#  notice the outcome will print everything except the Churros dessert.

for dessert in favorites:
    if dessert == 'Churros':
        continue ########Arroja todo menos churros
    print('Other desserts I like are', dessert) 


#Pass
#The pass statement allows you to run through the loop in its entirety and effectively ignore that the if condition 
# has been satisfied.
for dessert in favorites:
    if dessert == 'Churros':
        pass ##arroja toooodo
    print('Other desserts I like are', dessert) 
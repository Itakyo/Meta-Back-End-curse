#siempre usan corchetes ""{}""
#funciona por medio de claves y conetenido
my_d={1: 'Test', 'name': 'jim'}

my_d[2]='Test 2' ##--> de esta forma se agrege un contenido al diccionario especificando su calve '2' y leugo el contenido 'Test2'
my_d[1]="Hola"#****> camnbie el contenido de la clave 1 ya que ya esxistia

for i in my_d: ## recorre las claves mas no els contenido
    print (i)

for k, v in my_d.items(): ##asi imprimo el contenido por cada una de sus claves recorridas. "V"
    print(v)

print(type(my_d))
print(my_d)
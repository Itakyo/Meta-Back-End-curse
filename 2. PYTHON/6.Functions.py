# A Python function is a modular piece of code that can be re-used repeatedly

#sintax
#  def <function name> (<params):
#    <task to complete>
#   def sum (x,y):
#      return x+y
def calculate_taxt(bill, tax_rate):
    return round ((bill * tax_rate) /100.0)

bill = 175.00
tax_rate = 15 

#sin definir funcion
total_tax = ( bill  *    tax_rate) / 100.0
print ("total tax is:", total_tax)

#con funcion definida, me ahorre volver a eclarar la operacion solo una linia pero por ser una funcion sencilla
print("total tax is:",calculate_taxt(bill, tax_rate))




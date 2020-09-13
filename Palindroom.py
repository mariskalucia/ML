# Hier word gevraagd om het woord
invoer = input("Een woord: ")
  
# Hier zet hij het input automatich om 
a = ''

for char in invoer:
  a = char + a
 
if invoer==a:
  print(invoer, "is een palindroom")
 
else:
  print(invoer, "is geen palindroom")
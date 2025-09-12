print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+     Leander´s Coffee Shop     +")
print("+           Welcome             +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees, which:")
print(" > Espresso")
print(" > Americano")
print(" > Latte")
print(" > Cappuccino")
print(" > Macchiato")
print(" > Mocha")
print(" > Flat White")
print("----------------------------")

price = 0

while True:
   coffee = input("What coffee do you want? ").title()
   if coffee in ["Espresso", "Americano", "Latte", "Cappuccino", "Macchiato", "Mocha", "Flat White"]:
      break
   else:
      print("We dont have that Coffee. Please choose from the menu.")
      
if coffee=="Espresso":
   price = price + 2.50
elif coffee=="Americano":
   price = price + 3
elif coffee=="Latte":
   price = price + 2.50
elif coffee=="Cappuccino":
   price = price + 3.00
elif coffee=="Macchiato":
   price = price + 2.50
elif coffee=="Mocha":
   price = price + 3.50
elif coffee=="Flat White":
   price = price + 2.50
else:
   print("We dont have that Coffee.")

while True:
   size = input("What size do you want? (Medium, Large, XL) ").title()
   if size in ["Medium", "Large", "Xl"]:
      break
   else:
      print("We dont have that size, Please choose from menu.")
   
if size=="Medium":
   price = price + 0
elif size=="Large":
   price = price + 1.00
elif size=="XL":
   price = price + 1.50
else:
   print("We only have medium, large and XL.")

while True:
   takeaway = input("Eat in or take away? ").title()
   if takeaway in ["Eat In", "Take Away"]:
      break
   else:
      print("We cant provide that. Please choose to eat in or take away.")

if takeaway=="Eat in":
   price = price + 0
elif takeaway=="Take away":
   price = price + 1.00

print("----------------------------")
print("Total Cost: £" + str(price))
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
coffee = input("What coffee do you want? ").title()
if coffee=="Espresso":
   price = price + 2.50
elif coffee=="Americano":
   price = price + 3
elif coffee=="Latte":
   price = price + 2.50
elif coffee=="Cappuccino":
   price = price + 3
elif coffee=="Macchiato":
   price = price + 2.50
elif coffee=="Mocha":
   price = price + 3.50
elif coffee=="Flat White":
   price = price + 2.50
else:
   print("We dont have that Coffee.")

size = input("What size you want? (Medium, Large, XL) ").title()
if size=="Medium":
   price = price + 0
elif size=="Large":
   price = price + 1.00
elif size=="XL":
   price = price + 1.50
else:
   print("We only have medium, large and XL.")

takeaway = input("Eat in or take away? ").title()
if takeaway=="Eat in":
   price = price + 0
elif takeaway=="Take away":
   price = price + 1.00

print("----------------------------")
print("Total Cost: £" + str(price))
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("+                               +")
print("+     Leander´s Coffee Shop     +")
print("+           Welcome             +")
print("+                               +")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
print("")
print("We serve the following coffees, which:") #alle de forskjelllige valgene
print(" > Espresso")
print(" > Americano")
print(" > Latte")
print(" > Cappuccino")
print(" > Macchiato")
print(" > Mocha")
print(" > Flat White")
print("----------------------------")

#start pris
price = 0

#en loop som spør hva du vil ha helt til du gir et riktig svar
while True:
   coffee = input("What coffee do you want? ").title()
   if coffee in ["Espresso", "Americano", "Latte", "Cappuccino", "Macchiato", "Mocha", "Flat White"]:
      break
   else:
      print("We dont have that Coffee. Please choose from the menu.")

#Prisen på de forskjellige kaffene
if coffee=="Espresso":
   price = price + 2.50
elif coffee=="Americano":
   price = price + 3.00
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

#spør hvilken størrelse du vil ha helt til du svarer riktig
while True:
   size = input("What size do you want? (Medium, Large, Xl) ").title()
   if size in ["Medium", "Large", "Xl"]:
      break
   else:
      print("We dont have that size, Please choose from menu.")
   
if size=="Medium":
   price = price + 0
elif size=="Large":
   price = price + 1.00
elif size=="Xl":
   price = price + 1.50
else:
   print("We only have medium, large and XL.")

#spør om du vil sitte inne eller ute helt til du svare riktig
while True:
   takeaway = input("Eat In or Take Away? ").title()
   if takeaway in ["Eat In", "Take Away"]:
      break
   else:
      print("We cant provide that. Please choose to eat in or take away.")

#pris for take away og eat in
if takeaway=="Eat In":
   price = price + 0
elif takeaway=="Take Away":
   price = price + 1.00

#regner sammen prisene og sier hvor mye det koster
print("----------------------------")
print("Total Cost: £" + str(price))

#en hygglig melding som sier hva du har bestilt
print("Thanks for visiting Leander´s Coffee Shop. Enjoy your " + size + " " + coffee + " :D")


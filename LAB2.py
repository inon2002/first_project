# Lesson 8 exercise

print("Now we will calculate your marketing: \ntomatoes = 3 NIS \ncucumbers = 2 NIS \ncola = 5 NIS \nchicken = 20 NIS")

tomato = int(input("How many tomatoes would you like to buy? "))
cucumber = int(input("How many cucumbers would you like to buy? "))
cola = int(input("How many cola would you like to buy? "))
chicken = int(input("How many chickens would you like to buy? "))

bill = (tomato * 3 + cucumber * 2 + cola * 5 + chicken * 20)
vat = (1.17 * bill)

print ("The bill + the VAT is: " + str("%.1f" % (bill + vat)) + " NIS")
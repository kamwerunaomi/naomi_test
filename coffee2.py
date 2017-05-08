def coffee():
	people=input("Please enter your name")
	milktype=input("Please say either milk or water")
	for x in people:
		if milktype==milk:	
			print("This is {}'s coffee".format(x))
			print("1.Take a cup")
			print("2.Put in the coffee")
			print("3.Add sugar")
			print("4.Pour in milk")
			print("5.Stir")
		elif milktype==water:
			print("This is {}'s coffee".format(x))
			print("1.Take a cup")
			print("2.Put in the coffee")
			print("3.Add sugar")
			print("4.Pour in water")
			print("5.Stir")
		else:
			print("No coffee")
coffee()


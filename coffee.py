def coffee():
	people=["Naomi","Eddie"]
	for x in people:
		print("This is {}'s coffee".format(x))
		print("1.Take a cup")
		print("2.Put in the coffee")
		print("3.Add sugar")
		print("4.Pour in milk")
		print("5.Stir")

def serve(x):
	coffee()
	print("This is your tasty coffee {}! Enjoy".format(x))

serve("Naomi")


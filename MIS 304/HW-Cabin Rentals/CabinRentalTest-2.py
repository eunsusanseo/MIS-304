
# ******** not yet complete ********
from CabinRental import CabinRental, HolidayCabinRental

def main():
	cabinRental = []
	try:
		#CR1 = CabinRental("CR1", 3)
		CR2 = HolidayCabinRental("CR4", 2, 2)
		#CR3 = CabinRental("CR9", 2)

		cabinRental.append(CR2)
		#rentals.append(CR2)

		# display the rentals
		print("Initial state of rentals: ")
		for n in range (len(cabinRental)):
			print("Cabin rental transaction #", n + 1)
			print(cabinRental[n])

	except ValueError as ve:
		print("Cabin number invalid")


main()
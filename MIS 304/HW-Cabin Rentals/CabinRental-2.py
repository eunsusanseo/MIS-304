class CabinRental:
	# constructor or initializer
	# receives cabin number and number of days
	def __init__(self, cabin_number = '', num_of_weekdays = 0):
		# sets cabin_number, weekly_rental_rate and num_of_weekdays
		# call set methods to set private instance variables
		self.setCabin_number(cabin_number)
		self.setWeekly_rental_rate(cabin_number)
		self.setNum_of_weekdays(num_of_weekdays)

	# mutator method for cabin_number
	def setCabin_number(self, cabin_number):
		if (cabin_number != "CR1" and cabin_number != "CR2" and cabin_number != "CR3" and cabin_number != "CR4" and cabin_number != "CR5" and cabin_number != "CR6"): 
			raise ValueError("Invalid cabin number")
		else:
			self.__cabin_number = cabin_number


	# mutator to set weekly_rental_rate based on cabin number
	def setWeekly_rental_rate(self, cabin_number):
		if (cabin_number == "CR1" or cabin_number == "CR2" or cabin_number == "CR3"):
			self.__weekly_rental_rate = 250.0
		if (cabin_number == "CR4" or cabin_number == "CR5" or cabin_number == "CR6"):
			self.__weekly_rental_rate = 400.0
		# raise error if cabin_number outside CR1-CR6

	def setNum_of_weekdays(self, num_of_weekdays):
		self.__num_of_weekdays = num_of_weekdays


	# accessor methods
	def getCabin_number(self):
		return self.__cabin_number

	def getWeekly_rental_rate(self):
		return self.__weekly_rental_rate
		
	def getNum_of_weekdays(self):
		return self.__num_of_weekdays

	def calculateCharge(self):
		#self.__weekly_charge = self.getNum_of_weekdays * self.getWeekly_rental_rate
		#return self.__weekly_charge

		self.__weekly_charge = self.__num_of_weekdays * self.__weekly_rental_rate
		return self.__weekly_charge
	
	def __str__(self):
		cabin_rental_message = "Cabin number: %s" %self.getCabin_number() + "\n" + \
		"Number of days: %d" %self.getNum_of_weekdays() + "\n" + \
		"Weekly Rate: %.2f" %self.getWeekly_rental_rate() + "\n" + \
		"Weekly Charge : %.2f" %self.calculateCharge()

		return cabin_rental_message


# subclass of cabin_rental class used for rentals during the weeks that include weekends and holidays
class HolidayCabinRental(CabinRental):
	# CONSTRUCTOR
	def __init__(self, cabin_number = '', num_of_weekdays = 0, num_of_holidays = 0):
		super().__init__(cabin_number, num_of_weekdays)
		self.setHoliday_rental_rate()
		self.setNum_of_holidays(num_of_holidays)

	def setNum_of_holidays(self, num_of_holidays):
		self.__num_of_holidays = num_of_holidays


	# MUTATOR method for holiday_rental_rate
	def setHoliday_rental_rate(self):
		self.__holiday_rental_rate = super().getWeekly_rental_rate() + 150.0
		#return self.__holiday_rental_rate
	
	# accessor methods
	def getHoliday_rental_rate(self):
		return self.__holiday_rental_rate

	def getNum_of_holidays(self):
		return self.__num_of_holidays


	def calculateCharge(self):
		self.__total_charge = super().calculateCharge() + self.__num_of_holidays * self.__holiday_rental_rate
		return self.__total_charge
	
	def __str__(self):
		holiday_rental_message = "Cabin number: %s" %super().getCabin_number() + "\n" + \
		"Number of days: %d" %self.getNum_of_holidays() + "\n" + \
		"Holiday Weekly Rate: %.2f" %self.getHoliday_rental_rate() + "\n" + \
		"Holiday Weekly Charge : %.2f" %self.calculateCharge()

		return holiday_rental_message
		
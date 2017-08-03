# program to validate credit card number

 # Susan (Eun) Seo
 # Sheena Wang
 # Joyce (Dong) Huang 
 
def main():
	card_sum = 0
	double_evens = 0
	final_sum_double_even = 0
	final_sum_odd = 0
	
	card = str(input("Enter credit card number: "))
	# length function doesn't work for int, so keep as string
	len_card = getSize(card)
	
	if ((len_card >= 13) or (len_card <= 16)):
		# 0. Start Luhn check
		# create reverse card string
		rev_card = ""
		for i in range (len_card -1, -1, -1):
			rev_card += card[i]

		# 1a. Double every second digit from R to L
		double_evens = sumOfDoubleEvenPlace(rev_card)

		# 1b. If doubling of a digit results in a two-digit number, add up two digits
		# 2. Add all single-digit numbers from Step 1
		
		final_sum_double_even = getDigit(double_evens)

		# 3. Add all odd digits from R to L
		final_sum_odd = sumOfOddPlace(rev_card)

		# 4. Sum results from steps 2 and 3
		card_sum = final_sum_double_even + final_sum_odd

		# 5. Check if step 4 divisible by 10
		if (isValid(card_sum) == True):
			if (card[0] == '4'):
				print("Your card is : Visa")
				print("The number is valid")
			elif (card[0] == '5'):
				print("Your card is : MasterCard")
				print("The number is valid")
			elif ((card[0] == '3') and (card[1] == '7')):
				print("Your card is : American Express")
				print("The number is valid")
			elif (card[0] == '6'):
				print("Your card is : Discover")
				print("The number is valid")
			else:
				print("Your credit card number is invalid")
		else:
			print("Your credit card number is invalid")
	else:
		print("Your credit card number is invalid")

# Return number of digits in card
def getSize(card_num):
	return len(card_num)

# 1a. Double every second digit from R to L
def sumOfDoubleEvenPlace(card_num):
	even_place = []
	new_even_place = []
	for i in range (1, len(card_num), 2):
		double_even = card_num[i]
		even_place.append(double_even)

		for i in range(len(double_even)):
			double_even = (int(double_even[i]))
			double_even = (double_even * 2)
			new_even_place.append(str(double_even))
	return new_even_place

# 1b. If doubling of a digit results in a two-digit number, add up two digits to get single-digit number
def getDigit(number):
	final_sum_double_even_list = []
	for num in number:
		# check if number single digit
		num = str(num)
		# return number if it's single digit
		if (len(num) == 1):
			
			final_sum_double_even_list.append(int(num))
		# return sum of two digits if it's double digit
		else:
			sum_num = 0
			for i in range (len(num)):
				sum_num += int(num[i])
			final_sum_double_even_list.append(sum_num)
	
	# 2. Return all single-digit numbers from Step 1
	return(sum(final_sum_double_even_list))

# Return T if card number valid
def isValid(card_num):
	if (card_num % 10 == 0):
		return True
	else:
		return False

# Return sum of odd place digits from R to L
def sumOfOddPlace(card_num):
	odd_place = []
	for i in range (0, len(card_num), 2):
		odd_place.append(int(card_num[i]))
	return sum(odd_place)

# See if digit id is prefix for card number 
def prefixMatched(card_num, d):
	if (d == 4) or (d == 5) or (d == 6) or (d == 37):
		return True
	else:
		return False

main()
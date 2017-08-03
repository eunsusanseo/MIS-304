# program to check password

 # Susan (Eun) Seo
 # Sheena Wang
 # Joyce (Dong) Huang 

def main():
	checking_password = str(input("Enter password: "))
	
	checkPassword(checking_password)

def checkPassword(password):
	num_digits = 0
	num_upper = 0
	num_lower = 0
	num_special = 0
	# Check if password contains at least 8 characters
	if (len(password) >= 8):
		# If password has at least 8 characters, count number of digits
		for i in range (len(password)):
			if (password[i].isdigit() == True):
				num_digits += 1

		# Check if password contains at least two digits 
		if (num_digits >= 2):
			
			# Check if password contains at least one uppercase letter
			for i in range (len(password)):
				if (password[i].isupper() == True):
					num_upper += 1
			
			# Password contains at least one uppercase letter, then
			if (num_upper >= 1):
				
				# check if password contains at least one lowercase letter
				for i in range (len(password)):
					if (password[i].islower() == True):
						num_lower += 1

				if (num_lower >= 1):

					for i in range (len(password)):
						if ((password[i] == "!") or (password[i] == "@") or (password[i] == "#") or (password[i] == "$") or (password[i] == "%") or (password[i] == "^") or (password[i] == "&") or (password[i] == "*") or (password[i] == ",")):
							num_special += 1

					if (num_special >= 1):
						print("The password you entered is valid")
					else:
						# password does not have at least one special character
						print("The password you entered is invalid")

				# password does not have at least one lowercase letter
				else:
					print("The password you entered is invalid")
			
			# password does not have at least one uppercase letter
			else:
				print("The password you entered is invalid")

		# Password does not have at least two digits
		else:
			print("The password you entered is invalid")

	# Password does not have at least 8 char
	else:
		print("The password you entered is invalid")

main()
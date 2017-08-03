#Program to read get user majors
#Sheena Wang
#Joyce Huang
#Susan Seo

def main ():

	#open file for writing
	out_file = open ('majors.txt', 'w')
	
	#get user input
	string = input ('Enter the major id code and name, seperated by a comma: ')
	string = string.split (', ')
	major_code = int (string[0])
	major_name = string[1]
	done = False
	
	#write to outfile
	while (not done):
		out_write = '%s %s\n' %(major_code, major_name)
		out_file.write (out_write)
		
		string = input ('Enter the major id code and name, seperated by a comma (Enter 0 to stop): ')
		if (string == '0'):
			done = True
		else:
			string = string.split (', ')
			major_code = int (string[0])
			major_name = string[1]

	#close file
	out_file.close ()
	
main ()
#Program to compute student statistics
#Sheena Wang
#Susan Seo
#Joyce Huang
	
def mean (list):
	mean = sum (list)/ len (list)
	return mean
	
def deviation (list, mean):
	sd = (sum ([((x - mean) ** 2) for x in list]) / (len (list) - 1)) ** 0.5
	return sd

def main ():
	
	#open files for reading
	scores_file = open ('scores.txt', 'r')
	majors_file = open ('majors.txt', 'r')
	#open file for writing
	out_file = open ('results.txt', 'w')
	
	#read majors
	major_names_list = [] #store majors and corresponding id
	for line in majors_file:
		line = line.strip () #clean line
		line = line.split ()
		
		id = line[0]
		major = ''
		for string in line[1:]:
			major += string + ' '
		
		major_names_list.append (id)
		major_names_list.append (major)		
	
	#header
	out_file.write ('{0:12}{1:35}{2:15}{3:15}{4:12}{5:15}'.format ('Student', 'Major', 'Minimum Score', 'Maximum Score', 'Mean Score', 'Standard Deviation'))
	
	#read scores
	for line in scores_file:
		line = line.strip () #clean line
		line = line.split () #split line into parts
		
		#get data
		student_id = line[0]
		student_major = line[1]
		student_major_name = major_names_list[major_names_list.index(student_major) + 1]
		student_scores = [float(score) for score in line[2:9]]
		
		#compute stuff
		#minimum
		low = min (student_scores)
		#maximum
		high = max (student_scores)
		#mean
		avg = mean (student_scores)
		#standard deviation
		sd = deviation (student_scores, avg)
		
		#write to out_file
		out_file.write ('\n{0:12}{1:31}{2:15.1f}{3:15.1f}{4:12.4f}{5:15.4f}'.format (student_id, student_major_name, low, high, avg, sd))
		
	
	#close files
	scores_file.close ()
	majors_file.close ()
	out_file.close ()
	
main ()
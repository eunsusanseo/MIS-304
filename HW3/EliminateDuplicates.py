# program to eliminate duplicates

# Susan (Eun) Seo
# Sheena Wang
# Joyce (Dong) Huang 

def main():
	list_a = []
	a = input("Enter your list of numbers, separated by a space: ")
	list_A = a.split()
	list_B = eliminateDuplicates(list_A)

	print("Original List: ", list_A)	
	print("List without duplicates: ", list_B)

def eliminateDuplicates(list_a):
	list_b = []

	for i in list_a:
		if i not in list_b:
			list_b.append(i)
	return list_b

main()
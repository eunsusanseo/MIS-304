 # program to see if two words are anagrams

 # Susan (Eun) Seo
 # Sheena Wang
 # Joyce (Dong) Huang 

def main():
	word1 = str(input("Enter first word: "))
	word2 = str(input("Enter second word: "))

	if (isAnagram(word1, word2) == True):
		print("The words %s and %s are anagrams" %(word1, word2))
	else:
		print("The words %s and %s are not anagrams" %(word1, word2))

def isAnagram(s1, s2):
	s1 = sorted(s1)
	s2 = sorted(s2)

	if (s1 == s2):
		return True
	else:
		return False
main()

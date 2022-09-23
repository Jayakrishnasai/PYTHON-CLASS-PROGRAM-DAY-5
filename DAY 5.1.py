def length(str):
	lis = list(str.split(" "))
	return len(lis[-1])
str = input("enter the word :") 
print("The length of word is",length(str))

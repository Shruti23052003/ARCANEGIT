#Palindrome checker

#input the word to check if it is palindrome or not
a = str(input("Enter a word: "))
#for case sensitive 
a = a.lower()

#convert it into list
b = list(a)

c = " "  #declare empty variable 

c = b[:]
b.reverse()

c = list(c)

if(b == c):
    print(a,"is Palindrome")
else:
    print(a,"is not palindrome")
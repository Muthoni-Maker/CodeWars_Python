#Task One
#Write an application that accepts two parameters as 
#inputs.A sentence and its desired length
#if the length of the sentence is equal to or less than the desired length,the application should output the input sentence if full.


sentence=input("Sentence:")
print(sentence)
x=len(sentence)
print(x)
desiredLength=eval(input("Enter:"))
if x ==desiredLength or x<desiredLength:
	print(sentence)
if  x>desiredLength:
	p=x-desiredLength
	y=sentence[ 0:-1-p]
	t=y[-1]
	if t ==[]:
		print("Alart,white space detected!")
	else:
		print(y)
	
	
	
#If the length of the sentence is greater than the desired length,truncate the sentence to the required length and 
#output the outcome
#All characters in the output should be full words.No half words should output from the application
#The last character should not be a whitespace character

#Task Two
#Write an application that accepts two strings,string 1 and string 2
#If string one and string two are similar,the output string(one ) value = string two value and exit

one=input("Enter string:")
two=input("Enter string two:")
if one ==two:
	print("Similar values")
	




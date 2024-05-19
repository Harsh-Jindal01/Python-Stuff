#Making a program to check palindrome

name = input("Enter Your string : ")

reverse = name[::-1]

if (name == reverse):

	print('Given sting is a palindrome')

else:
	print("Given sting is not a palindrome")

# factorial.py
# A program that computes the factorial of a number
# Illustrates for loop with an accumulator
# Taken from Python Programming an Intro to CS by John Zelle

def main():
	n = input("Please enter a whole number: ")
	fact = 1
	for factor in range (n,1,-1):
		fact = fact * factor
	print "The factorial of", n, "is", fact
		
main()


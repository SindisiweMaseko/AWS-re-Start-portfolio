# Python program to display prime numbers within an interval
# and store them in a results.txt file

# take user input
lower = int(input("Enter lower number: "))
upper = int(input("Enter upper number: "))

# open results file
file = open("results.txt", "w")

file.write("The prime numbers between " + str(lower) + " and " + str(upper) + " are:\n\n")

# find prime numbers
for num in range(lower, upper + 1):

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            file.write(str(num) + "\n")

print("The prime numbers are displayed in the results.txt file.")

# close the file
file.close()

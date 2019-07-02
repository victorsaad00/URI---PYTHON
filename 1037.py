num = float(input())

'''
Timelimit: 1

You must make a program that read a float-point number and print a message saying in which of following 
intervals the number belongs: [0,25] (25,50], (50,75], (75,100]. If the read number is less than zero 
or greather than 100, the program must print the message “Fora de intervalo” that means "Out of Interval".

The symbol '(' represents greather than. For example:
[0,25] indicates numbers between 0 and 25.0000, including both.
(25,50] indicates numbers greather than 25 (25.00001) up to 50.0000000.
'''

if num < 0 or num > 100:
    print("Fora de intervalo")
elif (num >= 0) and (num <= 25):
    print("Intervalo [0,25]")
elif num > 25 and num <= 50:
    print("Intervalo (25,50]")
elif num > 50 and num <= 75:
    print("Intervalo (50,75]")
elif num > 75 and num <= 100:
    print("Intervalo (75,100]")


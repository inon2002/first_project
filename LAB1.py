# Lesson 6 exercise
'''
print:
identify and print every number in an integer. for example
a = 4567
print:
alafim = 4
meot = 5
asarot = 6
ahadot = 7
'''

num = int(input("Enter your number: "))

alafim = num // 1000
meot = num % 1000 // 100
asarot = num % 1000 % 100 // 10
ahadot = num % 1000 % 100 % 10 // 1

print("alafim = " + str(alafim)  + "\nmeot = " + str(meot) + "\nasarot = " + str(asarot) + "\nahadot = " + str(ahadot))

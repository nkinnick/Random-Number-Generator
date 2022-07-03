import random

#Creating a list for the 1000 numbers
numberList = []
#Generates 1000 numbers
for i in range(0, 1000):
  n = random.randint(1, 10)
  numberList.append(n)


#Loop goes through and counts the amount of each number.
#k will represent a different number (1-10) each time
for k in range(1, 11):
  numCount = numberList.count(k)
  print ("Number of times",k,"occurs:", numCount)


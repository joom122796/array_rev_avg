#Write a program to read 6 numbers into an array numbers[0] to numbers[5], ouput them in reverse order and then output the total and average.
import random

arr = []

for i in range(0,6):
  num = random.randint(0,500)
  arr.append(num)
  i = i + 1
else:
  arr.pop(0)
  print(f'Your array is {arr}')
  arr.reverse()
  print(f'Your reversed array is: {arr}')
  arravg = sum(arr)/i
  print(f'The average of the array is: {arravg}')

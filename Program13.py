# N Power of a number
import math

num = int(input("Enter a value:\n"))
expo = int(input("Enter the power value:\n"))

answer = num ^ expo
answer1 = math.pow(num, expo)

print(answer,",", answer1)
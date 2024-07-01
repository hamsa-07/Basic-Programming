# Round off Number
import math
num = float(input("Enter a number:\n"))

c = math.ceil(num)
f = math.floor(num)
r = round(num)

print ("\nCeil:{0}\n Floor:{1}\n Round:{2}\n".format(c,f,r))
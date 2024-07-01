# Greatest of Three Numbers
a = int(input("Enter a value:\n"))
b = int(input("Enter b value:\n"))
c = int(input("Enter c value:\n"))

if a > b and a > c:
    print("A is greatest")
elif b > a and b > c:
    print("B is greatest")
else:
    print("C is greatest")
    
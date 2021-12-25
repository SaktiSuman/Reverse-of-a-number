n = int(input("Enter the number: "))
rev = 0
while(n):
    t = n % 10
    rev = (rev * 10) + t
    n = n // 10
print("The reverse of the number is: ",rev)
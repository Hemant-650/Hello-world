# Practical 5: Check if a number is prime
num = int(input("Enter a number: "))
if num > 1:
 for i in range(2, num):
    if num % i == 0:
      print(num, "is not prime")
    break
 else:
    print(num, "is prime")
else:
 print("Number should be greater than 1")

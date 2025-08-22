# Practical 7: Menu-driven program for area calculations
while True:
 print("\n1. Area of Circle\n2. Triangle\n3. Square\n4. Rectangle\n5. Exit")
 choice = int(input("Enter choice: "))
if choice == 1:
     r = float(input("Enter radius: "))
     print("Area of circle:", 3.14 * r * r)
elif choice == 2:
    b = float(input("Base: "))
    h = float(input("Height: "))
    print("Area of triangle:", 0.5 * b * h)
elif choice == 3:
 s = float(input("Side: "))
 print("Area of square:", s * s)
elif choice == 4:
 l = float(input("Length: "))
 w = float(input("Width: "))
 print("Area of rectangle:", l * w)
else:
 print("Invalid choice!")
#2. Write a program to find whether the given number is even or odd.

a = int(input("Number? "))
if a == 0 :
    print("Even")

elif int(a/2)/(a/2) == 1 :
    print("Even")
else:
    print("Odd")

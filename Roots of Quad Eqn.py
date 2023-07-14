# 1. Write a program to find the roots of a quadratic equations when given the coefficients of the terms.

print("Hello Mathemagician!")
print("Welcome to Root Finder Program!")
print("Let's Get it Started :)")

print()
a = int(input("Enter the coefficient of the two-degree variable: "))
print()
b = int(input("Enter the coefficient of the one-degree variable: "))
print()
c = int(input("Enter the constant: "))
print()

print( "Here!" , ((0 - b) + ((b * b - 4 * a * c)**(1/2)))/(2 * a) , "and" , ((0 - b) - ((b * b - 4 * a * c)**(1/2)))/(2 * a) , "are the roots of the given quadratic equation.")
print("Thanks for Coming ;)")
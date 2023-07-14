name= input("What is your name?")

if len(name) < 3:
    print("Name too short")
else : print("Your name is " + name )

weight = input("What is your weight?" )
unit = input("(L)bs or (K)gs?")

if unit == "K" :
    print(int(weight) * 2.2)
elif unit == "L" :
    print(int(weight) / 2.2)
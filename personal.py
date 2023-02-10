age = eval(input("enter your age"))
if age < 0:
    print("wrong input")
else:
    if age > 50:
        x = age*2
        print (x)
    else:
        print("age is less than 50")
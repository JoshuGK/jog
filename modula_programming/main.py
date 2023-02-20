import operators
import trig
#building a better calc
import others
# x=others.cube(8)
# print(x)
#get numbers
operator=input("enter operator:")
if operator=="cube":
    num=eval(input("enter number:"))
elif operator=="sin":
    angle=eval(input("enter angle in degrees:"))
    sin_of_angle=trig.get_sine(angle)
    print(sin_of_angle)
elif operator=="tan":
    angle=eval(input("enter angle in degrees:"))
    tan_of_angle=trig.get_tan(angle)
    print(tan_of_angle)
elif operator=="cos":
    angle=eval(input("enter angle in degrees:"))
    cos_of_angle=trig.get_cosin(angle)
    print(cos_of_angle)
else:
    num1=eval(input("enter num1:"))
    num2=eval(input("enter num2:"))

    if operator=="+":
        x=operators.add(num1,num2)
        print(x)
    elif operator=="-":
        x=operators.subtract(num1,num2)
        print(x)
    elif operator=="/":
        x=operators.divide(num1,num2)
        print(x)
    elif operator=="*" or "x" or "X":
        x=operators.multiply(num1,num2)
        print(x)

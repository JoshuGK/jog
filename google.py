name=input("enter your name")
print(len(name))
print(name*10)

x=name[0]
print(x)

print(name[0:3])

print(name[::-1])

for name_length in name:
    if name_length>7:
        x=name[7]
        print(x)
    else:
        message=input("leave a message")
        print(message)
    

    


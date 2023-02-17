name=input("enter your name")
#name=name.casefold
vowel="aeiou"
flag=0
for i in vowel:
    if i in name:
        flag=1
        break
if(flag==0):
    print("no vowel:")
else:
    print("vowel present:")
    #create a dictionary
#data ={}.fromkeys(vowel,0)
#form a loop to know whether there is a vowel
#for character in name:
   # if character in vowel:
    #    data[character] +=1
#for vowel in data:
  # print(vowel,"=>",data[vowel])





 




#cars={
    #"model":"ford",
    #"year":1962
   # }
#print(cars["model"])

#books={"name":{"publisher":"longhorn"},
       #"pages":{"number":100}}
#print(books["name"]["publisher"])


#def my_function(first_name):
   # print("hello"+first_name)
#my_function("john")

#def my_function(name):
    #name=input("enter your name")
   # print("hello"+name)

#cars={"model":"ford",
      #"year":1998,
     # "colour":"red",
     # "country":"kenya"
     
    # }
#accessing things
#print(cars["year"])
#print(cars["model"])

#person={"name":"jog",
      #  "age": 83,
        #"pets":["dog","snake","chiwawa",1765,"owl"],
        #"petis":{"dogi":"jof",
           #      "camel":"otis",
      
           #   }
       #  }
#print(person["pets"][3])
#print(person["petis"]["camel"])








               







































#creating a dictionary for a profile of someone
#profile={}
#profile["username"]="user123"
#profile["age"]=23
#profile["repo"]={"name":"python",
    #             "year":1245}
#print(profile)

profiles={}
def register():
    #ask 4 username
    #ask 4 email
    #ask for password

    username=input("enter username:")
    email=input("entrer email:")
    password=input("enter password:")

    #store in a dictionary
    profiles["username"]=username
    profiles["email"]=email
    profiles["password"]=password
    print(profiles)
register()
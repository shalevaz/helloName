name = input("Insert your name ")

age = input("Insert your age ")
age = int(age)
if age > 18:
    print ("Hello "+name+" you are allow to continue")
else:
    print("Hello "+name+" you are too little please try again in a few year")

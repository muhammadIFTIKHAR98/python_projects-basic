#Firstly we need to specify the input required.
# then we need to import datetime as we required the current year.
#we will add the remaining age to reach 100 year age into the current year which we have imported from datetime. 


import datetime
name = str(input("what is your name: "))
age = int(input("what is your age: "))

year = (datetime.date.today().year) + (100-age)
#to mention any reference we need to provide f-string function inside the print function, else it will show an error.
print(f"Hi, {name} you will be 100 years old in year{year}")

#THIS THE CODE FOR CALCULATING THE BODY MASS INDEX

#asking for the input
Height=float(input("Enter your height in centimeters: "))
Weight=float(input("Enter your Weight in Kg: "))

#formula to calculate BMI
Height = Height/100
BMI=Weight/(Height*Height)

print("your Body Mass Index is: ",BMI)

# conditions
if(BMI>0):
	if(BMI<=16):
		print("you are severely underweight")
	elif(BMI<=18.5):
		print("you are underweight")
	elif(BMI<=25):
		print("you are Healthy")
	elif(BMI<=30):
		print("you are overweight")
	else: print("you are severely overweight")
else:("enter valid details")

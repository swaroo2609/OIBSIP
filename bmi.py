print("************BMI CALCULATOR***********")
weight=float(input("Enter your Weight (in kilograms):"))
height=float(input("Enter your Height (in meters):"))
height_in_meters=height/100
bmi=(weight/(height_in_meters*height_in_meters))
if(bmi<18.5):
    print("you are in under weight !")
elif(bmi>=18.5 and bmi<=24.9):
    print("you are Normal in weight !")
elif(bmi>=25.0 and bmi <=29.9):
    print("You are in over weight!")
elif(bmi>=30.0 and bmi<=34.9):
    print("you are in obesity class I !")
elif(bmi>=35.0 and bmi <=39.9):
    print("you are in obesity class II !")
else:
    print("You are in obesity class III !")
print("Your Body Mass Index is :",bmi)
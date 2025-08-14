import time

print("Welcome to the BMI Calculator ")
time.sleep(0.5)

Weight = float(input("Enter your weight (kg): "))
Height = float(input("Enter your height (m): "))

bmi = Weight / Height*2 

if bmi < 18.5:
    category = "Underweight 🥗"
elif bmi < 24.9:
    category = "Normal Weight ✅"
elif bmi < 29.9:
    category = "Overweight ⚠️"
else:
    category = "Obese 🚨"

print("\n Calculating your BMI...\n")
time.sleep(1)
print(f"Your BMI is: {round(bmi,2)}")
print(f"Category: {category}")

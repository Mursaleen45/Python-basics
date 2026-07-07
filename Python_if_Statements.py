#for checking the conditions we use logical operators like and, or, not
age1=15
age2=26

print(age1>=10 or age2<=30)

print(age1>=20 or age1 <=10)

# checking if a user is in a list of names
names=["John","Jane","Jack","Jill","James","Jasmine"]

print("John" in names)

# checking if a user is not in a list of names
banned_users=["John","Jane","Jack"]
user="Jill"
if user not in banned_users:
    print(f"{user} is allowed to access the system.")

# checking condition by .lower function
name= 'mursaleen'
print(name=="MURSALEEN".lower()) 


#checking and testing condition
age=int(input("Enter your age: "))
if age>=18:
    print("You are eligible to vote.")  

# if elif and else statement example

marks=float(input("Enter marks"))
if marks >= 90 and marks <= 100:
    print("Grade A")

elif marks >= 80 and marks < 90:
    print ("Grade B")

elif marks >= 70 and marks < 80:
    print("Grade C")

elif marks >= 60 and marks < 70:
    print("Grade D")

elif marks < 60:
    print("Grade F")

else:
    print("Invalid marks entered. Please enter marks between 0 and 100.")
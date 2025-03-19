num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
if num1 > num2 & num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)
    
    
ch=input("Enter alphabet: ")
if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u":
    print("Vowel")
else:
    print("Consonant")
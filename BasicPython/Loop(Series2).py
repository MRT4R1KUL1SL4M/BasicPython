n=int(input("Enter last digit of the series(2+4+6+...+n): "))
i=2
sum=0
while i<=n:
    sum=sum+i
    i=i+2
    
print("Summation = " , sum)
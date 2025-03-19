n=int(input("Enter last digit of the series(4+8+12+...+n): "))
i=4
sum=0
while i<=n:
    sum=sum+i
    i=i+4
    
print("Summation = " , sum)
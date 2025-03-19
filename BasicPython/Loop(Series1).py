n=int(input("Enter last digit of the series(1+2+3+...+n): "))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1
    
print("Summation = " , sum)
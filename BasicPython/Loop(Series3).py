n=int(input("Enter last digit of the series(1+3+5+...+n): "))
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+2
    
print("Summation = " , sum)
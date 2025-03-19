n=int(input("Enter last digit of the series(1^2 + 2^2 + 3^2 +...+ n^2): "))
i=1
sum=0
while i<=n:
    sum=sum+(i*i)
    i=i+1
    
print("Summation = " , sum)
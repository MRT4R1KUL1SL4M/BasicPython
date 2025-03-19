n=int(input("Enter last digit of the series(2^2 + 4^2 + 6^2 +...+ n^2): "))
i=2
sum=0
while i<=n:
    sum=sum+(i*i)
    i=i+2
    
print("Summation = " , sum)
n=int(input("Enter last digit of the series(1 + 1/2 + 1/3 +...+ 1/n): "))
i=1
sum=0
while i<=n:
    sum=sum+(1/i)
    i=i+1
print(f"Summation = {sum:.2f}")
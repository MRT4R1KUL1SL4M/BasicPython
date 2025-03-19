#xargsLikeTuples
def student(*details):
    print(details)
student(10,"Anis")
student(10,"Anis",5.00)

def add(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print(sum)
add(10,20)

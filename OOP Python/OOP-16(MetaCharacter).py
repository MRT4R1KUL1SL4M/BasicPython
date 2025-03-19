import re
pattern = r"^colo.r$"   #colo diye suru hote hobe, r diye sesh hote hobe. majhe .. er jaygay jekono 2 ta str thaklei match hbe.
if re.match(pattern,"colour"):
    print("matched")
    
    
pattern = r"a*" # 0 or more songkhok a thakleo match hbe
if re.match(pattern,"colour"):
    print("matched")
    
pattern = r"a+" #1 or more songkhok a thakleo match hbe
if re.match(pattern,"colour"):
    print("matched")
else:
    print("Not matched")
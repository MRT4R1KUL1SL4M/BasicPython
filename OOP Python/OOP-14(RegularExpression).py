import re
pattern = r"colour"
text="My favourite colour is Red."
if re.match(pattern,"colour Red is a colour, I love red colour"):
    print("Match")
else:
    print("Not match")

if re.search(pattern,"colour Red is a colour, I love red colour"):
    print("Search found")
else:
    print("Search not found")
    
print(re.findall(pattern,"colour Red is a colour, I love red colour"))

match=re.search(pattern,text)
if match:
    print(match.start())
    print(match.end())
    print(match.span())
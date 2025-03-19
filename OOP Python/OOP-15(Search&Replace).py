import re
pattern = r"colour"
text="My favourite colour is Red.i love blue colour as well"

text2=re.sub(pattern,"color",text)
print(text2)
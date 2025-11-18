import re
s = input()
pattern = r"(100+1+|01)+"
if re.fullmatch(pattern,s):
    print("SUBMARINE")
else:
    print("NOISE")
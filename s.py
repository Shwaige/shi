import re
import uuid

b = ["0", "1"]
k = 1
s = 12
a = 10
for k in range(0, a):
    num = re.findall('\d', str(uuid.uuid4()))
    if num[-1] in b:
        s = s + 1
print(s / a)

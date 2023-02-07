import uuid

k = 0  # 获取多少次 uuid
b = ["0", "1", "2", "3"]
j = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
s = 0  # 符合条件的 uuid 个数

while k < 1000:
    a = str(uuid.uuid4())
    c = -1
    if a[c] in j:
        if a[c] in b:
            k = k + 1
            s = s + 1
        else:
            k = k + 1
    else:
        c = c - 1

        # if a[c] in b:
        #     k = k + 1
        #     s = s + 1
# else:

num = list()
for c in range(0, 5):
    val = int(input(f"Digite o {c+1}° valor: "))
    if c == 0 or val > num[-1]:
        num.append(val)
    else:
        pos = 0
        while pos < len(num):
            if val <= num[pos]:
                num.insert(pos, val)
                break
            pos += 1
print("-"*30)
print(num)

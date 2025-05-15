total = 0
i = 1
while i <= 6:
    j = 1
    while j <= 6:
        if i == 1 or j == 1:
            total += 1
        else:
            total += i + j
        j += 1
    i += 1
print(total / 36)
a=list(bin(int(input())))
counter = 0
for i in a:
    if i == '1':
        counter += 1
print(counter)
with open('day1.txt') as f:
    lst = f.readlines()
    tesf = [x.strip() for x in lst]

data = []
tmp = []

for i,j in zip(tesf[:-1], tesf[0:]):
    if j == '':
        data.append(tmp)
        tmp = []
    else:
        if i != '':
            tmp.append(int(i))
data.append(tmp + [tesf[-1]])

max_count = 0
max_array = []
for i in range(len(data)):
    try:
        max_array.append(sum(data[i]))
    except:
        new = []
        for j in data[i]:
            new.append(int(j))
        max_array.append(sum(new))

x = sorted(max_array)

print('Answer to part 1: ' + str(x[-1]))
y = x[-3:]
print('Answer to part 2: ' + str(sum(y)))

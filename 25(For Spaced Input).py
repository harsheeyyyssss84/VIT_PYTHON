#Example Code
readings = list(map(int, input().split()))          #IMP LINEE WE USE SPLIT() i.e input().split()
avg = sum(readings) / len(readings)

normal = []
abnormal = []

for r in readings:
    if abs(r - avg) > 10:
        abnormal.append(r)
    else:
        normal.append(r)

result = abnormal + normal
print(*(str(x) for x in result))
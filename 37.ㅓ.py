scores = [95, 72, 60, 88, 45, 67]
high = []      #80점 이상
middle = []  #60점 이상
low = []       #나머지
for i in scores:
    if i >= 80:
        high.append(i)
    elif i >= 60:
        middle.append(i)
    else:
        low.append(i)

i = 0
while i < 5:
    i+=1
    print(scores[i],end = " ") 
print(high, middle, low)



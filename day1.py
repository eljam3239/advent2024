#read each column into a list
l1 = []
l2 = []
with open('puzzleinput.txt', 'r') as file:
    for line in file:
        l1.append(int(line.split()[0]))
        l2.append(int(line.split()[1]))
#for i in range(10):
    #print(l1[i], l2[i])

#pair up the smallest numbers in each list, the second smallest, etc
l1.sort()
l2.sort()

pairs = []
while l1:
    pairs.append((l1.pop(0), l2.pop(0)))

#find the distance between the two numbers in each pair and sum all such distances
sum = 0
for pair in pairs:
    sum += abs(pair[0] - pair[1])

#print(sum)
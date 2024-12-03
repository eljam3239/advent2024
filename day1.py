#read each column into a list

def read_file(file):
    l1 = []
    l2 = []
    with open(file, 'r') as file:
        for line in file:
            l1.append(int(line.split()[0]))
            l2.append(int(line.split()[1]))
    return l1, l2

#for i in range(10):
    #print(l1[i], l2[i])
def find_sum_pairs(l1, l2):

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
l1, l2 = read_file('puzzleinput.txt')

similarity_score = 0
for num in l1:
    #print(num)
    count = 0
    for num2 in l2:
        #print(num2)
        if num2 == num:
            count +=1
        #print(count)
    similarity_score += count*num

print(similarity_score)
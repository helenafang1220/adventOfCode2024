f = open("advent_code_ds.txt", "r").read()
f_list = f.replace('\n\n\n', ',').split()

list1 = []
list2 = []
for i in range(len(f_list)):
        if (i % 2 != 0):
            list2.append(int(f_list[i]))

for i in range(len(f_list)):
        if (i % 2 == 0):
            list1.append(int(f_list[i]))

list1 = sorted(list1)
list2 = sorted(list2)


new_list = list(zip(list1, list2))


distance.clear()
distance = []
for a, b in new_list:
    distance.append(abs(b-a))


sum(distance) #answer

#part 2
it_appears = []
for x in range(len(list1)):
    for y in range(len(list2)):
        if list1[x] == list2[y] :
            it_appears.append(list2[y])

get_unique = list(set(it_appears))
print(get_unique)


freq = []
for i in get_unique:
        freq.append(it_appears.count(i))

cal_list = list(zip(freq, get_unique))

#similarity.clear()
similarity = []
for a, b in cal_list:
    similarity.append(abs(a*b))

sum(similarity) #part2 ans


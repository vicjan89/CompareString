import Levenshtein
list1 = []
f = True
both = open('both.txt', 'w', encoding='utf8')
only1 = open('only1.txt', 'w', encoding='utf8')
only2 = open('only2.txt', 'w', encoding='utf8')
with open("Список СРЗАИ.txt", "r", encoding='utf8') as file1:
    for line in file1:
        t = line.find('\t')
        line = line[t+1:]
        list1.append(line)
with open("Список ПТО.txt", "r", encoding='utf8') as file2:
    list2 = file2.readlines()
    c2 = list(range(len(list2)))
for lit1 in list1:
    f = True
    for l2, lit2 in enumerate(list2):
        if Levenshtein.ratio(lit1, lit2)>0.8:
            both.write(lit1+' : '+lit2)
            f = False
            if l2 in c2:
                c2.remove(l2)
    if f:
        only1.write(lit1)
for s in c2:
    only2.write(list2[s])
both.close()
only1.close()
only2.close()
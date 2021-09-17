import Levenshtein
list1 = []
with open("Список СРЗАИ.txt", "r", encoding='utf8') as file1:
    for line in file1:
        t = line.find('\t')
        line = line[t+1:]
        list1.append(line)
with open("Список ПТО.txt", "r", encoding='utf8') as file2:
    list2 = file2.readlines()
for lit1 in list1:
    for lit2 in list2:
        if Levenshtein.ratio(lit1, lit2)>0.8:
            print(lit1[:-1],lit2[:-1])
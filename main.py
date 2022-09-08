import Levenshtein
list1 = []
f = True
both = open('В обоих списках.txt', 'w', encoding='utf8')
only2 = open('Есть во 2 но нет в 1.txt', 'w', encoding='utf8')
with open("Список для сравнения", "r", encoding='utf8') as file1:
    list2 = file1.readlines()
with open("Список СРЗАИ.txt", "r", encoding='utf8') as file2:
    list1 = []
    for row in file2:
        if '#электромонтёр' in row:
            list1.append(row.replace('#электромонтёр', ''))

list1.sort()
for row in list1:
    only2.write(row)

# result_comparison = [[0.0 for i in range(len(list1))] for j in range(len(list2))]
# for i, literature1 in enumerate(list1):
#     for j, literature2 in enumerate(list2):
#         result_comparison[j][i] = Levenshtein.ratio(literature1, literature2)
# for j, result in enumerate(result_comparison):
#     max_result = max(result)
#     if max_result > 0.7:
#         both.write(list2[j] + ' : ' + list1[result.index(max_result)])
#     else:
#         only2.write(list2[j])
both.close()
only2.close()
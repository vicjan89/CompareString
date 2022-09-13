import Levenshtein

class CompareLiterature:

    def __init__(self, list_literature1: str = '', list_literature2: str=''):
        self.list_literature1 = list_literature1
        self.list_literature2 = list_literature2

    @staticmethod
    def load(name_file, filter=''):
        out_list = []
        with open(name_file, "r", encoding='utf8') as file:
            for line in file:
                if filter in line:
                    out_list.append(line.split('#')[0])
        return out_list

    def load_first(self, list_literature: str = '', filter=''):
        if list_literature:
            self.list_literature1 = list_literature
        self.list1 = self.load(self.list_literature1, filter)

    def load_second(self, list_literature: str = '', filter=''):
        if list_literature:
            self.list_literature2 = list_literature
        self.list2 = self.load(self.list_literature2, filter)

    def compare(self):
        self.result_comparison = [[0.0 for i in range(len(self.list1))] for j in range(len(self.list2))]
        for i, literature1 in enumerate(self.list1):
            for j, literature2 in enumerate(self.list2):
                self.result_comparison[j][i] = Levenshtein.ratio(literature1, literature2)

    def separate(self, ratio):
        self.list_both = []
        self.list_only2 = []
        for j, result in enumerate(self.result_comparison):
            max_result = max(result)
            if max_result > ratio:
                self.list_both.append(self.list2[j] + ' : ' + self.list1[result.index(max_result)] + '\n')
            else:
                self.list_only2.append(self.list2[j])

    @staticmethod
    def save(name_file, list_str):
        with open(name_file, 'w', encoding='utf-8') as file:
            for row in list_str:
                file.write(row + '\n')

    def save_both(self, name_file):
        self.save(name_file, self.list_both)

    def save_only2(self, name_file):
        self.save(name_file, self.list_only2)

    def save_first(self, name_file):
        self.save(name_file, sorted(self.list1))




cl = CompareLiterature()
cl.load_first(list_literature="Список СРЗАИ.txt", filter='техник_метролог')
# cl.load_second(list_literature="Список для сравнения")
# cl.compare()
# cl.separate(0.5)
# cl.save_both('В обоих списках.txt')
# cl.save_only2('Есть во 2 но нет в 1.txt')
cl.save_first('В должностную.txt')
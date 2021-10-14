import sys
import csv
import os
import random
class Extract:
    def __init__(self):
        file_url = os.path.split(os.path.realpath(__file__))[0] + '/name.csv'
        self.names = []
        self.chance = []
        self.totalChance = 0
        self.ifAgain = 1 # 决定是否允许重复抽取
        with open(file_url) as csv_file:
            names_csv = csv.reader(csv_file, delimiter = ',')
            for data in names_csv:
                if int(data[1]):
                    self.names.append(data[0])
                    self.chance.append(int(data[1]))
            csv_file.close()
        for c in self.chance:
            self.totalChance += c
            
    def giveOne(self):
        if self.totalChance == 0:
            raise ValueError('所有同学已被抽取，请重启软件')
        num = 0
        rand = random.randint(1, self.totalChance)
        for i in range(len(self.chance)):
            num += self.chance[i]
            if rand <= num:
                res = i
                break
        if not self.ifAgain:
            self.totalChance -= self.chance[res]
            del self.chance[res]
            res = self.names.pop(res)
        else:
            res = self.names[res]
        return res

# test = Extract()
# while 1:
#     print(test.giveOne())

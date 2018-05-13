from HtmlData import *
import os


class Predicate:
    def __init__(self, url):
        self.url = url

    def getPredicate(self):
        a = []
        htmlData = HtmlData(self.url)
        predicateData = htmlData.getPredicate()
        if (predicateData != ''):
            for line in predicateData:
                b = line[0]
                c = b[len(b) - 1]
                if (b[len(b) - 1] == ':'):
                    a.append([b[0:len(b) - 2], line[1], line[2]])
                else:
                    a.append([line[0], line[1], line[2]])
        return a

    def savePredicate(self):
        predicateData = self.getPredicate()
        if (predicateData != []):
            predicateFile = open('/home/thang/Documents/Spider-master/venv/Predicate/data.txt', 'a')
            predicateFile.write('url '+self.url+'\n')
            flag = 1
            for index in predicateData:
                predicateFileTemp = open('/home/thang/Documents/Spider-master/venv/Predicate/data.txt', 'r')
                for line in predicateFileTemp:
                    if ((index[0] + "," + index[1] + "," + index[2]) == line[0:len(line) - 1]):
                        flag = 0
                        break
                predicateFileTemp.close()
                if (flag == 1):
                    predicateFile.write(index[0] + "," + index[1] + "," + index[2] + '\n')
            predicateFile.close()

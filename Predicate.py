from HtmlData import *
import os


class Predicate:
    def __init__(self, url):
        self.url = url

    def getPredicate(self):
        a = []
        htmlData = HtmlData(self.url)
        predicate_data = htmlData.getPredicate()
        if (predicate_data != ''):
            for line in predicate_data:
                b = line[0]
                if (b[len(b) - 1] == ':'):
                    a.append([b[0:len(b) - 2], line[1], line[2]])
                else:
                    a.append([line[0], line[1], line[2]])
        return a

    def savePredicate(self):
        predicate_data = self.getPredicate()
        if (predicate_data != []):
            temp = self.url.split('/')

            file_name = '/home/thang/Documents/Spider-master/venv/Predicate1/'+temp[3]+'__'+temp[4]+'.txt'
            predicate_file = open(file_name, 'w')
            for index in predicate_data:
                    predicate_file.write(index[0] + "||" + index[1] + "||" + index[2] + '\n')
            predicate_file.close()

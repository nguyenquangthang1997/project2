import os

list = os.listdir('/home/thang/Documents/Spider-master/venv/Predicate1')
array = []
for fileName in list:
    file = open('/home/thang/Documents/Spider-master/venv/Predicate1/' + fileName, 'r')
    for line in file:
        line_temp = line.split('||')
        # if ((line_temp[0] == 'Thông tin khác') and (line_temp[2] != 'sub\n') and (([line_temp[0] +' '+ line_temp[2][0:len(line_temp[2]) - 1], line_temp[2]] in array) == False)):
        #     array.append([line_temp[0] +' '+ line_temp[2][0:len(line_temp[2]) - 1], line_temp[2]])
        if (([line_temp[0], line_temp[2]] in array) == False):
            array.append([line_temp[0], line_temp[2]])
predicate_list = open('predicatelist.txt', 'a')
for line in array:
    predicate_list.write(line[0] + '||' + line[1])
predicate_list.close()

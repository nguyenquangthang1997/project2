import os

listValue = os.listdir('/home/thang/Documents/Spider-master/venv/Predicate1')
rdfFile = open('Rdf.rdf', 'w')
rdfFile.write('<rdf:RDF\n')
rdfFile.write('xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"\n')
rdfFile.write('xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#"\n')
rdfFile.write('xmlns:phone="http://localhost/onto/proj/Phone/"\n')
rdfFile.write('xmlns:pre="http://localhost/onto/proj/">\n')
for fileName in listValue:
    rdfFile.write('<rdf:Description rdf:about="http://localhost/onto/proj/Phone/'+fileName[12:len(fileName)-4].replace('?','').replace('#','').replace('=', '')+'">')
    file = open('/home/thang/Documents/Spider-master/venv/Predicate1/' + fileName, 'r')
    for line in file:
        predicate = ''
        lineTemp = line.split('||')
        if (lineTemp[2] != 'sub\n'):
            if(lineTemp[0] == 'Thông tin khác' ):
                predicate = lineTemp[0].replace(' ', '').replace('&', '').replace('(', '').replace(')', '').replace('/','')+lineTemp[2][0:len(lineTemp[2])-1].replace(' ', '').replace('&', '').replace('(', '').replace(')', '').replace('/', '')
            else:
                predicate = lineTemp[0].replace(' ', '').replace('&', '').replace('(', '').replace(')', '').replace('/', '')
            rdfFile.write('\t<pre:'+predicate + '>')
            rdfFile.write(lineTemp[1].replace('&', ','))
            rdfFile.write('</pre:'+predicate + '>\n')

    rdfFile.write('</rdf:Description>')
rdfFile.write('</rdf:RDF>')
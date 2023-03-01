# This program is to find exon records and to find -mRNA- then replace exon nunber by appending E
# Author	Sangeetha Vijaya
# Date		2/26/202

import fileinput
input_file = "wyeomyia.genes.gff"

oldCompList = list()
newCompList = list()

with fileinput.FileInput(input_file, inplace=True) as file_object:
    for line in file_object:
        components = line.strip().split()
        if len(components) > 2 and components[2].strip() == 'exon':
            oldCompList.append(components[8])
            index = components[8].find('-RA:')
            newComponent = components[8][0: index+3] + '-E' + components[8][index+4:len(components[8])] 
            newCompList.append(newComponent)
            print(line.replace(components[8],newComponent), end ='')
        else:
            print(line, end ='')
file_object.close()   

fout = open("exonList.txt", "wt")

for i in range(0, len(oldCompList)):
    fout.write(oldCompList[i] + "\t\t" + newCompList[i]+"\n")
    
fout.close()
for i in range(0, len(oldCompList)):
    print(oldCompList[i] + "\t\t" + newCompList[i])
    print()

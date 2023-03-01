# This program is to find exon records and to find -mRNA- then replace with RA
# Author	Sangeetha Vijaya
# Date		2/26/202

import fileinput
input_file = "wyeomyia.genes.gff"

oldCompList = list()
newCompList = list()

with fileinput.FileInput(input_file, inplace=True) as file_object:
    for line in file_object:
        components = line.strip().split()
        if len(components) > 2 and ( components[2].strip() == 'mRNA' or components[2].strip() == 'exon' or components[2].strip() == 'CDS'):
            if components[2].strip() == 'mRNA':
                oldCompList.append(components[8])
            index = components[8].find('-mRNA-')                
            #print(components[8])
            #print(components[8][0:index+1])
            #print(components[8][index+7:len(components[8])])
            newComponent = components[8][0:index+1] + 'RA' + components[8][index+7:len(components[8])]
            #print(newComponent)
            index = newComponent.find('-mRNA-')
            newComponent = newComponent[0:index+1] + 'RA' + newComponent[index+7:len(newComponent)]
            #print(newComponent)
            print(line.replace(components[8],newComponent), end ='')
            if components[2].strip() == 'mRNA':
                newCompList.append(newComponent)
        else:
            print(line, end ='')
file_object.close()   

fout = open("mRNAList.txt", "wt")

for i in range(0, len(oldCompList)):
    fout.write(oldCompList[i] + "\t\t" + newCompList[i]+"\n")
    
fout.close()
for i in range(0, len(oldCompList)):
    print(oldCompList[i] + "\t\t" + newCompList[i])
    print()

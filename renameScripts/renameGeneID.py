seqNumber = 0

import fileinput

input_file = "wyeomyia.genes.gff"

inputVal = list()

with open("original-geneID-list.txt") as fileHeader:    
    for l in fileHeader:
        #print(l)
        inputVal.append(str(l).strip())
        
#inputVal.append('maker-tig00034405|arrow-exonerate_est2genome-gene-0.0')

for i in range(0, len(inputVal)):
    
    seqNumber = seqNumber + 1
    strSeqNumber = str(seqNumber)
    
    while len(strSeqNumber) < 6:
        strSeqNumber = "0" + strSeqNumber                            
        nextID = "WYSM" + str(strSeqNumber)
        
    print()
    print("inputVal" + ":\t" + inputVal[i] + " nextID : " + nextID + ":\t" + str(type(inputVal[i])))

    orgText = inputVal[i]
    
    with fileinput.FileInput(input_file, inplace=True) as file_object:
        for line in file_object:
            print(line.replace(orgText, nextID), end='')
            #print(line.replace('maker-tig00034405|arrow-exonerate_est2genome-gene-0.1', nextID), end='')
    file_object.close()
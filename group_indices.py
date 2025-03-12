inputList = [[1,2,3], [4,5,6], [7,8,9]]
outputList = []

#we will choose an index from 0
index = 0

# for i in range(len(inputList[0])):
#     outputList.append([inputList[j][i] for j in range(len(inputList))])

for i in range(len(inputList[0])):
    outputList.append(inputList)

    for j in range(len(inputList)):
        outputList.append(inputList[j][index])
    index = index + 1

a,b,c = outputList[0], outputList[1], outputList[2]

print(a,b,c)
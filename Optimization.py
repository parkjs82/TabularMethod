def makeTable(pi,minterm):
    table = []
    subTable = []
    key = list(pi.keys())
    for i in range(0, len(minterm)): #minterm의 길이와 같은 배열 0으로 초기화
        subTable.append(0)
    for i in range(0, len(pi)): # pi갯수*minterm갯수 2차원 배열 생성
        table.append(subTable[:])
        for j in range(0, len(minterm)):
            if key[i].find(' '+str(minterm[j])+' ') == -1:
                table[i][j] = 0
            else:
                table[i][j] = 1
    return table
def printTable(arr,minterm):
    print(minterm)
    for i in range(0,len(arr)):
        print(arr[i])
def showStep(pi,minterm,EPIArray):
    if minterm != []:
        table = makeTable(pi, minterm)
        printTable(table, minterm)
        print("PI : ", pi)
    else:
        print("End")
    print("EPI : ", EPIArray)
    print()
def findEPI(table,minterm):
    EPIindex = []
    row = len(table)
    col = len(minterm)
    for i in range(0, col):
        count = 0
        p = 0
        for j in range(0, row):
            if table[j][i] == 1:
                count += 1
                p = j
        if count == 1:
            EPIindex.append(p)
    return EPIindex
def delDontCareMinterm(table,EPIindex,minterm): #ex) pi_1이 minterm 0,1을 커버할때 minterm에서 제거
    removeIndex = []
    for i in range(0,len(minterm)):
        removeIndex.append(0)

    for i in range(0,len(EPIindex)):
        for j in range(0,len(table[EPIindex[i]])):
            if table[EPIindex[i]][j] == 1:
                removeIndex[j] += 1

    for i in range(len(removeIndex)-1, -1, -1):
        if removeIndex[i]>0:
            minterm.pop(i)
    return minterm
def findNEPI(pi, minterm, EPIArray):
    counter = 0
    key = list(pi.keys())
    while(counter != len(pi)):
        counter = len(pi)
        table = makeTable(pi, minterm)
        EPIindex = findEPI(table,minterm)
        minterm = delDontCareMinterm(table, EPIindex, minterm)

        EPIindex = list(set(EPIindex))
        EPIindex.reverse()
        for i in EPIindex:
            EPIArray[key[i]] = pi[key[i]]
            del pi[key[i]]
        key = list(pi.keys())
        if EPIindex != []:
            print("simplify table")
            showStep(pi, minterm, EPIArray)
    changeAblePI(pi,minterm,EPIArray)
    return EPIArray
def changeAblePI(pi,minterm,EPIArray):
    table = makeTable(pi, minterm)
    key = list(pi.keys())
    pi1 = 0
    pi2 = 0
    for i in range(0, len(pi)):
        for j in range(0, len(pi)):
            if i == j:
                continue
            if table[i] == table[j]:
                pi1 = i
                pi2 = j
                break
    if pi1!=0:
        if len(key[pi1]) >= len(key[pi2]):
            del pi[key[pi2]]
        else:
            del pi[key[pi1]]
        print("changeable pi removed")
        showStep(pi, minterm, EPIArray)
def rowDominance(pi, minterm, EPIArray):
    counter = 0
    while(counter != len(pi)):
        removeindex = []
        counter = len(pi)
        key = list(pi.keys())
        table = makeTable(pi,minterm)
        row = len(table)
        column = len(table[0])
        for i in range(0,row):
            for j in range(0,row):
                for k in range(0,column):
                    if i == j:
                        break
                    if table[i][k] < table[j][k]:
                        break
                    else:
                        if k == column-1:
                            removeindex.append(j)
        removeindex.reverse()
        for i in removeindex:
            del pi[key[i]]
        if removeindex != []:
            print("row dominance operated")
            showStep(pi, minterm, EPIArray)
    changeAblePI(pi,minterm,EPIArray)
def columnDominance(pi,minterm, EPIArray):
    counter = 0
    while(counter != len(minterm)):
        removeindex = []
        counter = len(minterm)
        table = makeTable(pi,minterm)
        row = len(table)
        column = len(table[0])
        for i in range(0,column):
            for j in range(0,column):
                for k in range(0,row):
                    if i == j:
                        break
                    if table[k][i] < table[k][j]:
                        break
                    else:
                        if k == row-1:
                            removeindex.append(j)
        removeindex.reverse()
        for i in removeindex:
            minterm.pop(i)
        if removeindex != []:
            print("column dominance operated")
            showStep(pi, minterm, EPIArray)
    changeAblePI(pi,minterm,EPIArray)
def petricksMethod():
    print()
# if __name__ == "__main__":

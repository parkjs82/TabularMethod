def combineCheck(str1, str2):
    counter = 0
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            counter += 1
    if counter == 1:
        return 1
    return 0


def combineStr(str1, str2):
    returnStr = ''
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            returnStr += '-'
        else:
            returnStr += str1[i]
    return returnStr


def combine(pi, key):
    returnPI = {}
    counter = []
    for i in range(0, len(pi)):
        counter.append(0)
    for i in range(0, len(pi)):
        for j in range(i+1, len(pi)):
            if combineCheck(pi[key[i]], pi[key[j]]) == 1:
                sumKey = key[i].split()
                sumKey += key[j].split()
                for k in range(0,len(sumKey)):
                    sumKey[k] = int(sumKey[k])
                sumKey.sort()
                sumKey = list(map(str, sumKey))
                num = ' '+' '.join(sumKey)+' '

                returnPI[num] = combineStr(pi[key[i]], pi[key[j]])
                counter[i] += 1
                counter[j] += 1
    for i in range(0,len(pi)):
        if counter[i] == 0:
            returnPI[key[i]] = pi[key[i]]
    return returnPI


def sort(arr):
    returnArr = []
    ar = []
    for i in range(0, len(arr)):
        str = ''
        for j in range(0, len(arr[i])):
            if arr[i][j] == '-':
                str += '2'
            else:
                str += arr[i][j]
        ar.append(str)
    ar.sort()
    for i in range(0, len(ar)):
        str = ''
        for j in range(0, len(ar[i])):
            if ar[i][j] == '2':
                str += '-'
            else:
                str += ar[i][j]
        returnArr.append(str)
    return returnArr


def translate(pi, demension, minterm):
    key = []
    for i in range(0, len(minterm)):
        st = ""
        num = minterm[i]
        for j in range(demension-1, -1, -1):
            if num >= (2**j):
                st += '1'
                num -= 2**j
            else:
                st += '0'
        pi[str(minterm[i])] = st
        key.append(str(minterm[i]))
    return key


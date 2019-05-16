# 연속수 목록 검색 기능
#
# @param		inputData		입력데이터(숫자열 목록)
# @return						연속수 목록
def getSequenceList(inputData) :
    sequenceList = []
    ########################여기부터 구현 (1) ---------------->
    for str in inputData:
        tmp = int(str[0])
        check = True
        for i in range(1, len(str)):
            intCh = int(str[i])
            if tmp == intCh - 1:
                tmp = intCh
            else:
                check = False
                break
        if check:
            sequenceList.append(str)
    ############################# <-------------- 여기까지 구현 (1)
    return sequenceList

# 가장 큰 수 생성 기능
#
# @param		sequenceList	연속수 목록
# @return						가장 큰 수
def getMaxNum(sequenceList) :
    maxNum = 0
    ########################여기부터 구현 (2) ---------------->
    tmpSequenceList = []
    for strValue in sequenceList:
        tmpSequenceList.append(int(strValue))
    tmpSequenceList.sort()
    minStr = str(tmpSequenceList[0])
    tmpSequenceList.reverse()
    maxStr = str(tmpSequenceList[0])
    firstNum = int(minStr + maxStr)
    secondNum = int(maxStr + minStr)

    if firstNum > secondNum:
        maxNum = firstNum
    else:
        maxNum = secondNum
    ############################# <-------------- 여기까지 구현 (2)
    return maxNum

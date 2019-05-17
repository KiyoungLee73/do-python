# 연속수 목록 검색 기능
#
# @param		inputData		입력데이터(숫자열 목록)
# @return						연속수 목록
def getSequenceList(inputData) :
    sequenceList = []
    ########################여기부터 구현 (1) ---------------->
    sampleStr = '123456789'
    returnList = list()

    for i in inputData:
        if sampleStr.find(i) >= 0:
            returnList.append(i)

    sequenceList = returnList
    ############################# <-------------- 여기까지 구현 (1)
    return sequenceList

# 가장 큰 수 생성 기능
#
# @param		sequenceList	연속수 목록
# @return						가장 큰 수
def getMaxNum(sequenceList) :
    maxNum = 0
    ########################여기부터 구현 (2) ---------------->
    maxVal = 0
    minVal = 999999999

    for i in sequenceList:
        chkVal = int(i)
        if chkVal > maxVal:
            maxVal = chkVal
        
        if chkVal < minVal:
            minVal = chkVal

    maxValStr = str(maxVal)
    minValStr = str(minVal)

    if int(maxValStr + minValStr) > int(minValStr + maxValStr):
        maxNum =  int(maxValStr + minValStr)
    else:
        maxNum =  int(minValStr + maxValStr)
    ############################# <-------------- 여기까지 구현 (2)
    return maxNum

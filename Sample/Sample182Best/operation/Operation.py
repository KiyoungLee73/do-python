# 문자열 분리 기능
#
# @param		inputData			입력데이터(문자열)
# @return							[0]: 문자로 구성된 문자열, [1]: 숫자로 구성된 문자열
def getStrList(inputData):
    strList = []
    ######################여기부터 구현 (1) ---------------->
    str = ""
    numStr = ""
    for c in inputData:
        if isNum(c):
            numStr += c
        else:
            str += c
    strList.append(str)
    strList.append(numStr)
    ############################# <-------------- 여기까지 구현 (1)
    return strList

# 새로운 문자열을 생성하는 기능
#
# @param		strList			[0]: 문자로 구성된 문자열, [1]: 숫자로 구성된 문자열
# @return						새로운 문자열
def getNewStr(strList):
    newStr = ""
    ######################여기부터 구현 (2) ---------------->
    strL = strList[0]
    numStr = strList[1]
    for i in range(len(strL)):
        if i == len(strL) - 1:
            newStr += strL[i]
        else:
            newStr += strL[i] + numStr[i]
    ############################# <-------------- 여기까지 구현 (2)
    return newStr

# 숫자를 확인하는 기능(솔루션용 기능, 제공파일에 없음)
#
# @param		s			문자열
# @return					숫자여부
def isNum(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


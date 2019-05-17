# 문자열 분리 기능
#
# @param		inputData			입력데이터(문자열)
# @return							[0]: 문자로 구성된 문자열, [1]: 숫자로 구성된 문자열
def getStrList(inputData):
    strList = []
    ######################여기부터 구현 (1) ---------------->
    tempStrList = ''
    tempNumList = ''
    for i in inputData:
        if i.isdigit():
            tempNumList += i
        else:
            tempStrList += i
    strList.append(tempStrList)
    strList.append(tempNumList)
    ############################# <-------------- 여기까지 구현 (1)
    return strList

# 새로운 문자열을 생성하는 기능
#
# @param		strList			[0]: 문자로 구성된 문자열, [1]: 숫자로 구성된 문자열
# @return						새로운 문자열
def getNewStr(strList):
    newStr = ""
    ######################여기부터 구현 (2) ---------------->
    for i in range(len(strList[1])):
        newStr += strList[0][i]
        newStr += strList[1][i]
    newStr += strList[0][len(strList[0])-1]
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


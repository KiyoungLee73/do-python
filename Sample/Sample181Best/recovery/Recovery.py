# 데이터 1차 복원 기능
#
# @param		inputData			입력데이터(원본 데이터)
# @param		backup				입력데이터(백업 데이터)
# @return							1차 복원된 데이터
def getFirstRecovery(inputData, backup) :
    firstRecovery = ""
    for i in range(len(inputData)):
        currentCh = inputData[i]
        backupCh = backup[i]
        if str(currentCh).isdigit():
            if not str(backupCh).isdigit(): # 결함 발생
                currentCh = backupCh
        firstRecovery += currentCh
    return firstRecovery


# 데이터 2차 복원 기능
#
# @param		firstRecovery		1차 복원된 데이터
# @param		netWork				입력데이터(네트워크에 저장된 데이터)
# @return							2차 복원된 데이터
def getSecondRecovery(firstRecovery, netWork) :
    netWorkStr = ""
    for i in range(len(netWork)):
        netWorkStr += netWork[i] # 결함 발생
    secondRecovery = getFirstRecovery(firstRecovery, netWorkStr)
    return secondRecovery

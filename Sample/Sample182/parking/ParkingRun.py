#-----------------------------------------------
# 이 파일은 수정하면 안되며, 제공된 Parking.py 파일의
# 함수를 수정해서 프로그램을 완성해야 합니다.
#-----------------------------------------------
from Parking import *

def main():
    # 제공 데이터 세트2를 실행하려면 loadData에서 제공 데이터 세트1을 주석 처리하고제공 데이터 세트2를 주석 해제하여 실행
    inputData = loadData()
    printInput(inputData)

    # 차종별 주차대수 계산 기능
    numberOfCars = getNumberOfCars(inputData)
    printNumberOfCars(numberOfCars)

    # 주차요금 합계 계산 기능
    parkingfee = getParkingFee(inputData)
    printParkingfee(parkingfee)

def loadData():
    ######################
    # 제공 데이터 세트 1
    ######################
    inputData = [
        {"carNumber": "11가1234", "parkingTime": 10},
        {"carNumber": "34오6789", "parkingTime": 20},
        {"carNumber": "76나2323", "parkingTime": 45},
        {"carNumber": "33노8989", "parkingTime": 120},
        {"carNumber": "99이3810", "parkingTime": 35},
        {"carNumber": "46거6677", "parkingTime": 20},
        {"carNumber": "47마9087", "parkingTime": 60},
        {"carNumber": "90오2345", "parkingTime": 70},
        {"carNumber": "90우9999", "parkingTime": 80},
        {"carNumber": "45소1122", "parkingTime": 10},
        {"carNumber": "23노8888", "parkingTime": 35},
        {"carNumber": "78이2345", "parkingTime": 44},
        {"carNumber": "88구1212", "parkingTime": 20}
    ]



    ######################
    # 제공 데이터 세트 2
    ######################

    # inputData = [
    #     {"carNumber": "11너5687", "parkingTime": 10},
    #     {"carNumber": "21구7894", "parkingTime": 100},
    #     {"carNumber": "68고4567", "parkingTime": 35},
    #     {"carNumber": "92가1234", "parkingTime": 30},
    #     {"carNumber": "98거5698", "parkingTime": 90},
    #     {"carNumber": "72아1234", "parkingTime": 60},
    #     {"carNumber": "81사6543", "parkingTime": 20}
    # ]

    return inputData

def printInput(inputData):
    printLineInitial()
    print("차량번호\t주차시간(분)")
    for parkingInfo in inputData:
        print("{}\t{}".format(parkingInfo.get("carNumber"), parkingInfo.get("parkingTime")))
    printLine()

def printNumberOfCars(numberOfCars) :
    print("[차종별 주차대수]")
    if len(numberOfCars) == 0:
        print("결과값이 없습니다.")
    else:
        keyList = list(numberOfCars.keys())
        keyList.sort()
        for key in keyList:
            if key == 0:
                print("승용차: ", end="")
            elif key == 1:
                print("승합차: ", end="")
            elif key == 2:
                print("화물차: ", end="")
            else:
                print("특수차: ", end="")
            print("{}대".format(numberOfCars.get(key)))
    printLine()

def printParkingfee(parkingfee) :
    print("[주차요금 합계]: ", end="")
    if parkingfee == 0:
        print("결과값이 없습니다.")
    else:
        print("{}원".format(parkingfee))
    printLine()

def printLineInitial():
    print("[초기 입력 데이터]")

def printLine():
    print("--------------------------------------------------------------------------")


## 메인 코드 부분 ##
if __name__ == "__main__" :
    main()
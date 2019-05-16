# 차종별 주차대수 계산 기능
#
# @param		inputData		입력데이터(주차한 차량 정보)
# @return						차종별 주차대수 (key->"0" : value->"승용차 주차대수", key->"1" : value->"승합차 주차대수", key->"2" : value->"화물차 주차대수", key->"3" : value->"특수차 주차대수")
def getNumberOfCars(inputData):
    numberOfCars = {}

    for parking in inputData:
        carTypeStr = parking.get("carNumber")[0:2]
        key = -1
        carType = int(carTypeStr)
        if carType >= 11 and carType <= 69:
            key = 0
        elif carType >= 70 and carType <= 79:
            key = 1
        elif carType >= 80 and carType <= 97:
            key = 2
        elif carType >= 98 and carType <= 99:
            key = 3

        cnt = 0
        if key in numberOfCars.keys():
            cnt = numberOfCars.get(key) + 1 # 결함 발생
        else:
            cnt += 1

        numberOfCars[key] = cnt
    return numberOfCars

# 주차요금 합계 계산 기능
#
# @param		inputData		입력데이터(주차한 차량 정보)
# @return						주차요금 합계
def getParkingFee(inputData):
    parkingfee = 0
    fee = [1000, 1000, 2000, 3000]  # [0]:승용차, [1]:승합차, [2]:화물차, [3]:특수차의 추차요금
    for parking in inputData:
        time = parking.get("parkingTime")
        price = 0
        if time >= 30:
            carTypeStr = parking.get("carNumber")[0:2]
            carType = int(carTypeStr)
            index = 0
            if carType >= 11 and carType <= 69:
                index = 0
            elif carType >= 70 and carType <= 79:
                index = 1
            elif carType >= 80 and carType <= 97:
                index = 2
            elif carType >= 98 and carType <= 99:
                index = 3
            price = fee[index]
        parkingfee += price # 결함 발생
    return parkingfee

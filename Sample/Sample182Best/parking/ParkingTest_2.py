import unittest
from parking.Parking import *

class ParkingTest_2(unittest.TestCase):
    inputData = [
        [
            {"carNumber": "25너5687", "parkingTime": 100},
            {"carNumber": "69구7894", "parkingTime": 100},
            {"carNumber": "72고4567", "parkingTime": 35},
            {"carNumber": "88가1234", "parkingTime": 32},
            {"carNumber": "98거5698", "parkingTime": 65},
            {"carNumber": "72아1234", "parkingTime": 70},
            {"carNumber": "92사6543", "parkingTime": 80}
        ],
        [
            {"carNumber": "67너5687", "parkingTime": 90},
            {"carNumber": "81구7894", "parkingTime": 100},
            {"carNumber": "98고4567", "parkingTime": 35},
            {"carNumber": "99가1234", "parkingTime": 40},
            {"carNumber": "75거5698", "parkingTime": 90},
            {"carNumber": "64아1234", "parkingTime": 60},
            {"carNumber": "12사6543", "parkingTime": 20}
        ],
        [
            {"carNumber": "98너5687", "parkingTime": 10},
            {"carNumber": "91구7894", "parkingTime": 10},
            {"carNumber": "68고4567", "parkingTime": 35},
            {"carNumber": "65가1234", "parkingTime": 30},
            {"carNumber": "84거5698", "parkingTime": 25},
            {"carNumber": "72아1234", "parkingTime": 60},
            {"carNumber": "51사6543", "parkingTime": 20}
        ]
    ]

    inputData2 = [
        [
            {"carNumber": "25너5687", "parkingTime": 100},
            {"carNumber": "69구7894", "parkingTime": 100},
            {"carNumber": "72고4567", "parkingTime": 35},
            {"carNumber": "88가1234", "parkingTime": 32},
            {"carNumber": "98거5698", "parkingTime": 65},
            {"carNumber": "72아1234", "parkingTime": 70},
            {"carNumber": "92사6543", "parkingTime": 80}
        ],
        [
            {"carNumber": "67너5687", "parkingTime": 90},
            {"carNumber": "81구7894", "parkingTime": 100},
            {"carNumber": "98고4567", "parkingTime": 35},
            {"carNumber": "99가1234", "parkingTime": 40},
            {"carNumber": "75거5698", "parkingTime": 90},
            {"carNumber": "64아1234", "parkingTime": 60},
            {"carNumber": "12사6543", "parkingTime": 20}
        ],
        [
            {"carNumber": "98너5687", "parkingTime": 10},
            {"carNumber": "91구7894", "parkingTime": 10},
            {"carNumber": "68고4567", "parkingTime": 35},
            {"carNumber": "65가1234", "parkingTime": 30},
            {"carNumber": "84거5698", "parkingTime": 25},
            {"carNumber": "72아1234", "parkingTime": 60},
            {"carNumber": "51사6543", "parkingTime": 20}
        ]
    ]

    compareNumberOfCars = [
        {0: 2, 1: 2, 2: 2, 3: 1},
        {0: 3, 1: 1, 2: 1, 3: 2},
        {0: 3, 1: 1, 2: 2, 3: 1}
    ]

    compareParkingfee = [
        11000, 11000, 3000
    ]

    def test1__차종별_주차대수_계산__차종별_주차대수_계산_기능__5(self):
        for i in range(len(self.inputData)):
            numberOfCars = getNumberOfCars(self.inputData[i])
            if len(numberOfCars) == len(self.compareNumberOfCars[i]):
                for key in self.compareNumberOfCars[i].keys():
                    self.assertEqual(int(self.compareNumberOfCars[i].get(key)), int(numberOfCars.get(key)))
            else:
                self.assertEqual(True, False)

    def test2__주차요금_합계_계산__주차요금_합계_계산_기능__5(self):
        for i in range(len(self.inputData2)):
            parkingfee = getParkingFee(self.inputData2[i])
            self.assertEqual(int(self.compareParkingfee[i]), int(parkingfee))

if __name__ == '__main__' :
    unittest.main()
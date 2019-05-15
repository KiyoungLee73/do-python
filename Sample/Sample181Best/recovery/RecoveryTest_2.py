import unittest
from recovery.Recovery import *

class RecoveryTest_2(unittest.TestCase):


    inputData = [
        "uie1had23jkh67adsk9hu8adf", "e2ruih1jdch32alihh12twa1d", "lkaj2sdfu3haes1lkjr4rgj89bha"
    ]

    backup = [
        "uie1hadt3jkhj7adskkhu8adf", "eoruih1jdch3lalihh12twa1d", "lkajusdfu3haes1lkjr4rgj8tbha"
    ]

    netWork = [
        [
            "uiet", "hadt", "kjkh", "jead", "skkh", "ucad", "f   "
        ],
        [
            "eoru", "ihtj", "dchp", "lali", "hhop", "twap", "d   "
        ],
        [
            "lkaj", "usdf", "ucha", "estl", "kjrs", "rgje", "tbha"
        ]
    ]
    compareFirstRecovery = [
        "uie1hadt3jkhj7adskkhu8adf", "eoruih1jdch3lalihh12twa1d", "lkajusdfu3haes1lkjr4rgj8tbha"
    ]

    compareFirstRecovery2 = [
        "uie1hadt3jkhj7adskkhu8adf", "eoruih1jdch3lalihh12twa1d", "lkajusdfu3haes1lkjr4rgj8tbha"
    ]

    compareSecondRecovery = [
        "uiethadtkjkhjeadskkhucadf", "eoruihtjdchplalihhoptwapd", "lkajusdfuchaestlkjrsrgjetbha"
    ]


    def test1__데이터_1차_복원__데이터_1차_복원_기능__5(self):
        for i in range(len(self.inputData)):
            firstRecovery = getFirstRecovery(self.inputData[i], self.backup[i])
            self.assertEqual(self.compareFirstRecovery[i], firstRecovery)

    def test2__데이터_2차_복원__데이터_2차_복원_기능__5(self):
        for i in range(len(self.compareFirstRecovery2)):
            secondRecovery = getSecondRecovery(self.compareFirstRecovery2[i], self.netWork[i])
            self.assertEqual(self.compareSecondRecovery[i], secondRecovery)

if __name__ == '__main__' :
    unittest.main()
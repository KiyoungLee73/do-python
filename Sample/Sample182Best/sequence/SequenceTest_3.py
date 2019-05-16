import unittest
from sequence.Sequence import *

class SequenceTest_3(unittest.TestCase):


    inputData = [
        [
            "3421", "5671", "6598", "1234", "7756", "6789", "123", "345"
        ],
        [
            "6598", "12", "5678", "3256", "6658", "6789", "1156", "678"
        ],
        [
            "2569", "6598", "7589", "2365", "4567", "2345", "655", "789"
        ]
    ]

    compareSequenceList = [
        [
            "123", "345", "1234", "6789"
        ],
        [
            "12", "678", "5678", "6789"
        ],
        [
            "789", "2345", "4567"
        ]
    ]

    compareSequenceList2 = [
        [
            "123", "345", "1234", "6789"
        ],
        [
            "12", "678", "5678", "6789"
        ],
        [
            "789", "2345", "4567"
        ]
    ]

    compareMaxNum = [
        6789123, 678912, 7894567
    ]
    def test1__연속수_목록_검색__연속수_목록_검색_기능__10(self):
        for i in range(len(self.inputData)):
            sequenceList = getSequenceList(self.inputData[i])
            if len(sequenceList) == len(self.compareSequenceList[i]):
                sequenceList.sort()
                self.compareSequenceList[i].sort()
                for j in range(len(self.compareSequenceList[i])):
                    self.assertEqual(int(self.compareSequenceList[i][j]), int(sequenceList[j]))
            else:
                self.assertEqual(True, False)

    def test2__가장_큰_수_생성__가장_큰_수_생성_기능__10(self):
        for i in range(len(self.compareSequenceList2)):
            maxNum = getMaxNum(self.compareSequenceList2[i])
            self.assertEqual(int(self.compareMaxNum[i]), int(maxNum))

if __name__ == '__main__' :
    unittest.main()
import unittest
from sum.Sum import *

class SumTest_4(unittest.TestCase):


    inputData = [
        [
            [71, 12, 7, 45],
            [33, 36, 43, 93],
            [25, 42, 63, 84],
            [12, 54, 74, 45]
        ],
        [
            [66, 31, 12, 85, 56, 17],
            [42, 77, 24, 61, 45, 36],
            [65, 94, 61, 42, 36, 48],
            [15, 64, 58, 47, 9, 58],
            [2, 41, 45, 38, 57, 69],
            [24, 37, 49, 37, 41, 72]
        ],
        [
            [15, 46, 1, 22, 92, 46, 57, 22],
            [32, 42, 53, 67, 73, 81, 95, 6],
            [52, 95, 88, 74, 61, 52, 46, 33],
            [33, 31, 31, 21, 31, 47, 59, 68],
            [46, 52, 71, 24, 32, 38, 47, 79],
            [55, 44, 37, 52, 79, 42, 21, 32],
            [51, 32, 43, 64, 87, 8, 39, 24],
            [32, 23, 36, 73, 67, 58, 49, 31]
        ]
    ]

    compareSortedArray = [
        [
            [1, 2, 3, 5],
            [2, 3, 4, 5],
            [2, 3, 4, 6],
            [3, 4, 5, 7]
        ],
        [
            [1, 2, 4, 5, 6, 7],
            [1, 2, 4, 5, 6, 7],
            [1, 2, 4, 6, 6, 8],
            [1, 2, 5, 7, 7, 9],
            [1, 2, 5, 7, 8, 9],
            [4, 5, 7, 8, 8, 9]
        ],
        [
            [1, 1, 1, 1, 3, 5, 6, 7],
            [1, 2, 2, 2, 3, 5, 6, 7],
            [1, 2, 2, 2, 4, 5, 6, 8],
            [1, 2, 2, 3, 4, 6, 7, 9],
            [1, 2, 2, 3, 4, 7, 8, 9],
            [1, 2, 2, 3, 5, 7, 8, 9],
            [1, 2, 3, 4, 6, 7, 8, 9],
            [1, 2, 3, 4, 6, 7, 8, 9]
        ]
    ]

    compareSortedArray2 = [
        [
            [1, 2, 3, 5],
            [2, 3, 4, 5],
            [2, 3, 4, 6],
            [3, 4, 5, 7]
        ],
        [
            [1, 2, 4, 5, 6, 7],
            [1, 2, 4, 5, 6, 7],
            [1, 2, 4, 6, 6, 8],
            [1, 2, 5, 7, 7, 9],
            [1, 2, 5, 7, 8, 9],
            [4, 5, 7, 8, 8, 9]
        ],
        [
            [1, 1, 1, 1, 3, 5, 6, 7],
            [1, 2, 2, 2, 3, 5, 6, 7],
            [1, 2, 2, 2, 4, 5, 6, 8],
            [1, 2, 2, 3, 4, 6, 7, 9],
            [1, 2, 2, 3, 4, 7, 8, 9],
            [1, 2, 2, 3, 5, 7, 8, 9],
            [1, 2, 3, 4, 6, 7, 8, 9],
            [1, 2, 3, 4, 6, 7, 8, 9]
        ]
    ]

    compareArrSum = [
        31, 24, 26
    ]
    def test1__배열_정렬__배열을_정렬한_결과__10(self):
        for i in range(len(self.inputData)):
            sortedArray = getSortedArray(self.inputData[i])
            if len(sortedArray) == len(self.compareSortedArray[i]):
                for j in range(len(self.compareSortedArray[i])):
                    for k in range(len(self.compareSortedArray[i][j])):
                        self.assertEqual(int(self.compareSortedArray[i][j][k]), int(sortedArray[j][k]))
            else:
                self.assertEqual(True, False)

    def test2__배열합_계산__배열합을_계산한_결과__10(self):
        for i in range(len(self.compareSortedArray2)):
            arrSum = getArrSum(self.compareSortedArray2[i])
            self.assertEqual(int(self.compareArrSum[i]), int(arrSum))

if __name__ == '__main__' :
    unittest.main()
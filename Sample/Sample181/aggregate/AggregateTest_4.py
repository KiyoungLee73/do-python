import unittest
from Aggregate import *

class AggregateTest_4(unittest.TestCase):
    inputData = [
        [
            [-1, 9, 3],
            [9, -9, 9],
            [1, 2, 3]
        ],
        [
            [7, 1, 3, 6, -2],
            [-3, -2, 0, 1, 2],
            [0, 1, 2, 3, 4],
            [0, 8, -3, 9, -5],
            [9, 6, -6, 7, 0]
        ],
        [
            [-1, -2, -3, 1, 2, 3],
            [8, 7, -2, -1, -5, 8],
            [9, -4, 5, 2, 7, -1],
            [0, 2, 3, -2, 0, 9],
            [1, 7, -8, 3, 2, 3],
            [3, 4, -4, 5, 8, 6]
        ]
    ]

    inputData2 = [
        [
            [-1, 9, 3],
            [9, -9, 9],
            [1, 2, 3]
        ],
        [
            [7, 1, 3, 6, -2],
            [-3, -2, 0, 1, 2],
            [0, 1, 2, 3, 4],
            [0, 8, -3, 9, -5],
            [9, 6, -6, 7, 0]
        ],
        [
            [-1, -2, -3, 1, 2, 3],
            [8, 7, -2, -1, -5, 8],
            [9, -4, 5, 2, 7, -1],
            [0, 2, 3, -2, 0, 9],
            [1, 7, -8, 3, 2, 3],
            [3, 4, -4, 5, 8, 6]
        ]
    ]

    compareNumberOfSubArrays = [
        14, 55, 91
    ]

    compareMaximumValue = [
        26, 48, 75
    ]

    def test1__부분_배열_개수_구하기__부분_배열_개수를_구한_결과__5(self):
        for i in range(len(self.inputData)):
            numberOfSubArrays = getNumberOfSubArrays(len(self.inputData[i]))
            self.assertEqual(int(self.compareNumberOfSubArrays[i]), int(numberOfSubArrays))

    def test2__부분_배열_내의_최대_합_구하기__부분_배열_내의_최대_합을_구한_결과__15(self):
        for i in range(len(self.inputData2)):
            maximumValue = getMaximumValue(self.inputData2[i])
            self.assertEqual(int(self.compareMaximumValue[i]), int(maximumValue))

if __name__ == '__main__' :
    unittest.main()
import unittest
from stick.Stick import *

class StickTest_1(unittest.TestCase):


    inputData = [
        5, 7, 9
    ]

    numberOfLayers = [
        10, 6, 12
    ]

    compareNumberOfStickForTriangle = [
        11, 15, 19
    ]

    compareNumberOfStickForPyramid = [
        165, 63, 234
    ]


    def test1__N개의_삼각형_만들기_막대_개수__N개의_삼각형_만들기_막대_개수를_구하는_기능__5(self):
        for i in range(len(self.inputData)):
            numberOfStickForTriangle = getNumberOfStickForTriangle(self.inputData[i])
            self.assertEqual(int(self.compareNumberOfStickForTriangle[i]), int(numberOfStickForTriangle))

    def test2__N층의_피라미드_만들기_막대_개수__N층의_피라미드_만들기_막대_개수를_구하는_기능__5(self):
        for i in range(len(self.numberOfLayers)):
            numberOfStickForPyramid = getNumberOfStickForPyramid(self.numberOfLayers[i])
            self.assertEqual(int(self.compareNumberOfStickForPyramid[i]), int(numberOfStickForPyramid))

if __name__ == '__main__' :
    unittest.main()
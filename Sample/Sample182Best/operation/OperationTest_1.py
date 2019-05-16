import unittest
from operation.Operation import *

class OperationTest_1(unittest.TestCase):


    inputData = [
        "Q8T47S3D1LA", "184BS3DQ9SD", "Z4AD9K6W5D2"
    ]

    compareStrList = [
        ["QTSDLA", "84731"],
        ["BSDQSD", "18439"],
        ["ZADKWD", "49652"]
    ]

    compareStrList2 = [
        ["QTSDLA", "84731"],
        ["BSDQSD", "18439"],
        ["ZADKWD", "49652"]
    ]

    compareNewStr = [
        "Q8T4S7D3L1A", "B1S8D4Q3S9D", "Z4A9D6K5W2D"
    ]


    def test1__문자열과_숫자열로_입력_문자열_분리__문자열과_숫자열로_입력_문자열을_분리한_결과__5(self):
        for i in range(len(self.inputData)):
            strList = getStrList(self.inputData[i])
            if len(strList) == len(self.compareStrList[i]):
                for j in range(len(self.compareStrList[i])):
                    self.assertEqual(self.compareStrList[i][j],strList[j])
            else:
                self.assertEqual(True, False)



    def test2__문자열과_숫자열_결합__문자열과_숫자열을_결합한_결과__5(self):
        for i in range(len(self.compareStrList2)):
            newStr = getNewStr(self.compareStrList2[i])
            self.assertEqual(self.compareNewStr[i], newStr)

if __name__ == '__main__' :
    unittest.main()
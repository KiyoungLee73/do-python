import unittest
from Gene import *

class GeneTest_5(unittest.TestCase):
    inputData = [
        "AGGCTTC,TTAGGA", "CTAGAAT,GGA", "GTTCTAG,GTTTCA"
    ]

    inputData2 = [
        "AGGCTTC,TTAGGA", "CTAGAAT,GGA", "GTTCTAG,GTTTCA"
    ]

    similarityMatrix = [
        [5, -1, -2, -1, -3],
        [-1, 6, -3, -2, -4],
        [-2, -3, 7, -1, -2],
        [-1, -2, -1, 8, -1],
        [-3, -4, -2, -1, 0]
    ]

    compareSimilarity = [
        3, 2, 4
    ]

    compareMaxSimilarity = [
        10, 1, 22
    ]

    def test1__단순비교_방식의_유사도_측정__단순비교_방식의_유사도를_측정한_결과__15(self):
        for i in range(len(self.inputData)):
            similarity = measureSimpleComparison(self.inputData[i])
            self.assertEqual(int(self.compareSimilarity[i]), int(similarity))

    def test2__행렬비교_방식의_유사도_측정__행렬비교_방식의_유사도를_측정한_결과__15(self):
        for i in range(len(self.inputData2)):
            maxSimilarity = measureSortComparison(self.inputData2[i], self.similarityMatrix)
            self.assertEqual(int(self.compareMaxSimilarity[i]), int(maxSimilarity))

if __name__ == '__main__' :
    unittest.main()
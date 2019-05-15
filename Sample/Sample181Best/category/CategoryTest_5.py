import unittest
from category.Category import *

class CategoryTest_5(unittest.TestCase):
    inputData =[
        [
            ["U", "R"],
            ["U", "C"],
            ["U", "D"],
            ["R", "E"],
            ["R", "F"],
            ["C", "G"],
            ["D", "H"],
            ["D", "I"],
            ["D", "J"],
            ["E", "K"],
            ["E", "L"],
            ["F", "M"],
            ["G", "N"],
            ["I", "O"],
            ["I", "P"],
            ["J", "Q"]
        ],
        [
            ["W", "B"],
            ["W", "Z"],
            ["W", "D"],
            ["B", "E"],
            ["B", "F"],
            ["B", "G"],
            ["B", "H"],
            ["Z", "I"],
            ["D", "J"],
            ["E", "K"],
            ["E", "L"],
            ["E", "M"],
            ["H", "N"],
            ["H", "O"],
            ["I", "P"],
            ["J", "Q"]
        ],
        [
            ["Z", "B"],
            ["Z", "C"],
            ["Z", "V"],
            ["B", "E"],
            ["C", "F"],
            ["C", "G"],
            ["C", "H"],
            ["V", "I"],
            ["V", "J"],
            ["E", "K"],
            ["E", "L"],
            ["E", "M"],
            ["F", "N"],
            ["H", "O"],
            ["I", "P"],
            ["I", "Q"]
        ]
    ]

    inputData2 = [
        [
            ["U", "R"],
            ["U", "C"],
            ["U", "D"],
            ["R", "E"],
            ["R", "F"],
            ["C", "G"],
            ["D", "H"],
            ["D", "I"],
            ["D", "J"],
            ["E", "K"],
            ["E", "L"],
            ["F", "M"],
            ["G", "N"],
            ["I", "O"],
            ["I", "P"],
            ["J", "Q"]
        ],
        [
            ["W", "B"],
            ["W", "Z"],
            ["W", "D"],
            ["B", "E"],
            ["B", "F"],
            ["B", "G"],
            ["B", "H"],
            ["Z", "I"],
            ["D", "J"],
            ["E", "K"],
            ["E", "L"],
            ["E", "M"],
            ["H", "N"],
            ["H", "O"],
            ["I", "P"],
            ["J", "Q"]
        ],
        [
            ["Z", "B"],
            ["Z", "C"],
            ["Z", "V"],
            ["B", "E"],
            ["C", "F"],
            ["C", "G"],
            ["C", "H"],
            ["V", "I"],
            ["V", "J"],
            ["E", "K"],
            ["E", "L"],
            ["E", "M"],
            ["F", "N"],
            ["H", "O"],
            ["I", "P"],
            ["I", "Q"]
        ]
    ]

    categories = [
        [
            "F", "I"
        ],
        [
            "M", "N"
        ],
        [
            "K", "M"
        ]
    ]

    categoryStr= [
        "H", "E", "C"
    ]

    compareTopCategory = [
        "U", "B", "E"
    ]

    compareNumberOfSubcategories = [
        6, 9, 16
    ]




    def test1__상위_카테고리_검색__상위_카테고리를_검색한_결과__15(self):
        for i in range(len(self.inputData)):
            topCategory = getTopCategory(self.inputData[i], self.categories[i])
            self.assertEqual(topCategory, self.compareTopCategory[i])

    def test2__하위_카테고리_개수_계산__하위_카테고리의_개수를_계산한_결과__15(self):
        for i in range(len(self.inputData2)):
            numberOfSubcategories = getNumberOfSubcategories(self.inputData2[i], self.categoryStr[i])
            self.assertEqual(int(numberOfSubcategories), int(self.compareNumberOfSubcategories[i]))


if __name__ == '__main__' :
    unittest.main()
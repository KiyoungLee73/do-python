# 상위 카테고리를 검색하는 기능
#
# @param		inputData		입력데이터(카테고리 정보)
# @param		categories		입력데이터(inputCategories[0]: 카테고리1, inputCategories[1]: 카테고리2)
# @return						상위 카테고리
def getTopCategory(inputData, categories):
    topCategory = ""
    ########################여기부터 구현 (1) ---------------->





    ############################# <-------------- 여기까지 구현 (1)
    return topCategory

# 하위 카테고리의 개수를 계산하는 기능
#
# @param		inputData		입력데이터(카테고리 정보)
# @param		categoryStr		입력데이터(카테고리)
# @return						하위 카테고리의 개수
def getNumberOfSubcategories(inputData, categoryStr) :
    numberOfSubcategories = 0
    ########################여기부터 구현 (2) ---------------->



    ############################# <-------------- 여기까지 구현 (2)
    return numberOfSubcategories

# 트리를 만드는 기능(솔루션용 기능, 제공파일에 없음)
#
# @param		inputData		입력데이터(카테고리 정보)
# @return						트리 경로
def makeTreePath(inputData):
    mindMapPath = []
    parentToChildMindMap = {}
    allNodeList = []
    for strArr in inputData:
        key = strArr[0]
        value = strArr[1]
        if key not in allNodeList:
            allNodeList.append(key)
        if value not in allNodeList:
            allNodeList.append(value)
        lowerPath = []
        if key in parentToChildMindMap.keys():
            lowerPath = parentToChildMindMap.get(key)
            lowerPath.append(value)
        else:
            lowerPath.append(value)
        parentToChildMindMap[key] = lowerPath

    childToParentMindMap = {}
    for strArr in inputData:
        key = strArr[1]
        value = strArr[0]
        childToParentMindMap[key] = value

    rootNode = ""
    for node in allNodeList:
        if node not in childToParentMindMap.keys():
            rootNode = node
    allNodeList.append(rootNode)

    leafNode = []
    for node in allNodeList:
        if node not in parentToChildMindMap.keys():
            leafNode.append(node)

    for key in leafNode:
        tmpKey = key
        path = []
        while (True):
            path.append(tmpKey)
            tmpKey = childToParentMindMap.get(tmpKey)
            if tmpKey == rootNode:
                path.append(rootNode)
                path.reverse()
                mindMapPath.append(path)
                break
    return mindMapPath
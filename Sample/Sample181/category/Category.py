# 상위 카테고리를 검색하는 기능
#
# @param		inputData		입력데이터(카테고리 정보)
# @param		categories		입력데이터(inputCategories[0]: 카테고리1, inputCategories[1]: 카테고리2)
# @return						상위 카테고리
def getTopCategory(inputData, categories):
    topCategory = ""
    ########################여기부터 구현 (1) ---------------->

    foundedHighCategoryList = list()
    foundedHighCategory = ''
    for i in categories:
        inputCategory = i
        tempHighCategory = ''
        while True:
            foundedFlag = 'N'
            for searchHiarachy in inputData:
                if searchHiarachy[1] == inputCategory:
                    foundedHighCategory = searchHiarachy[0]
                    inputCategory = foundedHighCategory
                    tempHighCategory = tempHighCategory + foundedHighCategory
                    foundedFlag = 'Y'
                
                if foundedFlag == 'Y':
                    break
            if foundedFlag == 'N':
                break
        foundedHighCategoryList.append(tempHighCategory)
    #print(foundedHighCategoryList)

    minLen = 9999
    inputSize = len(foundedHighCategoryList)
    for j in range(len(foundedHighCategoryList)):
        foundedHighCategoryList[j] = foundedHighCategoryList[j][::-1] #순서 뒤집기 중요
        if len(foundedHighCategoryList[j]) < minLen:
            minLen = len(foundedHighCategoryList[j])
    #print(foundedHighCategoryList)

    for k in range(minLen):
        if foundedHighCategoryList[0][k] == foundedHighCategoryList[1][k]:
            topCategory = foundedHighCategoryList[0][k]

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

    #상위카테고리 찾기
    highCategory = ''
    for a in inputData:
        if categoryStr == a[1]:
            highCategory = a[0]

    foundedCategory = list()
    count = 0
    findCategory = [['1', highCategory]]
    tempFindCategory = list()
    targetCategory = inputData

    import copy

    while True:
        foundedFlag = 'N'
        jCount = 0
        for j in findCategory:
            foundedFlag = 'N'
            for i in targetCategory:
                if j[1] == i[0]:
                    foundedCategory.append(i)
                    tempFindCategory.append(i)
                    count += 1
                    foundedFlag = 'Y'
            jCount += 1
        if len(tempFindCategory) > 0:
            findCategory.clear()
            findCategory = copy.deepcopy(tempFindCategory)
            tempFindCategory.clear()

        #print(findCategory)

        if foundedFlag == 'N':
            break
    #print(foundedCategory)  
    numberOfSubcategories = len(foundedCategory)

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
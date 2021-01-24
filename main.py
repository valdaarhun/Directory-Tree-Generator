import os


tabSegment1 = ['\u251c', '\u2500', '\u2500']
tabSegment2 = ['\u2514', '\u2500', '\u2500']
tabSegment3 = [' ' for _ in range(3)]
tabSegment4 = ['\u2502', ' ', ' ']


def index(levels):
    count = 0
    dict = {}
    for level in levels:
        dict[level[0]] = count
        count += 1
        fileList = level[2]
        for file in fileList:
            dict[level[0] + '/' + file] = -count
            count += 1
    return dict


def constructAdjList(adjList, levels, indexedDict):
    for level in levels:
        parent = indexedDict[level[0]]
        adjList[parent] = []
        dirList = level[1]
        fileList = level[2]
        for dir in dirList:
            path = level[0] + '/' + dir
            if path in indexedDict:
                adjList[parent].append(indexedDict[path])
        for file in fileList:
            path = level[0] + '/' + file
            if path in indexedDict:
                adjList[parent].append(indexedDict[path])


def dfs(reverseIndexedDict, adjList, parent, node, tabs):
    path = reverseIndexedDict[node].replace(reverseIndexedDict[parent], '')
    path = '.' if path is '' else path.replace('/', '')
    if node is not 0:
        if adjList[parent][-1] is not node:
            print(tabs + ''.join(tabSegment1), end='')
            tabs += ''.join(tabSegment4)
        else:
            print(tabs + ''.join(tabSegment2), end='')
            tabs += ''.join(tabSegment3)
    if node >= 0:
        print(f'\033[1;34;40m{path}\033[0m')
    else:
        print(f'\033[1;31;40m{path}\033[0m')
    if node >= 0:

        for child in adjList[node]:
            dfs(reverseIndexedDict, adjList, node, child, tabs)


def main():
    rootPath = os.getcwd()
    levels = []
    for path, dirList, fileList in os.walk(rootPath):
        levels.append((path, dirList, fileList))
    indexedDict = index(levels)
    adjList = {}
    constructAdjList(adjList, levels, indexedDict)
    reverseIndexedDict = {indexedDict[key]: key for key in indexedDict}
    rootTree = 0
    tabs = ''
    dfs(reverseIndexedDict, adjList, rootTree, rootTree, tabs)


if __name__ == '__main__':
    exit(main())

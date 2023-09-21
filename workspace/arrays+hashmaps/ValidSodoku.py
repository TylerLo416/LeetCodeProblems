class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #iterate through row
        for i in board:
            alreadyFound = {}
            for j in i:
                if(j != '.'):
                    if(int(alreadyFound.get(j, 0)) == 1):
                        return False
                    else:
                        alreadyFound[j] = 1

        #iterate through column
        for i in range(len(board)):
            alreadyFound = {}
            for j in board:
                if(j[i] != '.'):
                    if(int(alreadyFound.get(j[i],0)) == 1):
                        return False
                    else:
                        alreadyFound[j[i]] = 1

        #iterate through 9 3x3 boxes
            count = 0
            for i in board:
                modCounter = 0
                if count == 3:
                    alreadyFound = {}
                    alreadyFound1 = {}
                    alreadyFound2 = {}
                    count = 0
                else:
                    count += 1
                for j in i:
                    if j != '.':
                        if j % 3 == 0:
                            mapPointer = alreadyFound
                        elif j % 3 == 1:
                            mapPointer = alreadyFound1
                        else:
                            mapPointer = alreadyFound2
                        if(int(mapPointer.get(j, 0)) == 1):
                            return False
                        else:
                            mapPointer[j] = 1



        #all succeeded
        return True
def schedule(groupNum):
    courtNum = getCourtNum()
    createGames(groupNum, courtNum)
    print("Scheduler finished")

def getCourtNum():
    courtNum = input("Enter the number of courts: ")
    return courtNum

def createGames(groupNum, courtNum):
    arr = [[0]*2]*int(((groupNum*(groupNum-1))/2))
    print(len(arr))

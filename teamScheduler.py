def schedule(groupNum):
    courtNum = getCourtNum()
    createGames(groupNum, courtNum)
    print("Scheduler finished")


# Requests the number of courts the round robin will occur on
def getCourtNum():
    courtNum = input("Enter the number of courts: ")
    return courtNum


# Creates an array of games between teams
def createGames(groupNum, courtNum):
    arr = [[0] * 2] * int(((groupNum * (groupNum - 1)) / 2))
    print(len(arr))

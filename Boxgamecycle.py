import random

#tab combos for all possible rolls
lookup = {
    1: [[1]],
    2: [[2]],
    3: [[3],[1,2]],
    4: [[4],[1,3]],
    5: [[5],[1,4],[2,3]],
    6: [[6],[1,5],[2,4],[1,2,3]],
    7: [[7],[1,6],[2,5],[3,4],[1,2,4]],
    8: [[8],[1,7],[2,6],[3,5],[1,2,5],[1,3,4]],
    9: [[9],[1,8],[2,7],[3,6],[4,5],[1,2,6],[1,3,5],[2,3,4]],
    10: [[1,9],[2,8],[3,7],[4,6],[1,2,7],[1,3,6],[1,4,5],[2,3,5],[1,2,3,4]],
    11: [[2,9],[3,8],[4,7],[5,6],[1,2,8],[1,3,7],[1,4,6],[2,3,6],[2,4,5],[1,2,3,5]],
    12: [[3,9],[4,8],[5,7],[1,2,9],[1,3,8],[1,4,7],[1,5,6],[2,3,7],[2,4,6],[3,4,5],[1,2,3,6],[1,2,4,5]]}

def movesAvailable(Board, roll):
    if (Board == []):
        return False
    combos = lookup[roll]
    alive = True

    i = 0

    while(alive):
        a = set(combos[i]).issubset(Board)
        if a:
            return True
        else:
            i=i+1
            if(i==len(combos)):
                return False

def gameLoop(Board):
    print("\n" + str(Board))
    if(sum(Board) <= 6):
        roll = random.randint(1,6)
    else:
        roll = random.randint(1,6) + random.randint(1,6)

    #is roll in board?
    check = movesAvailable(Board, roll)
    if (check == True):
        print("\nYOU ROLLED: " + str(roll))
    else:
        score = "".join(map(str, Board))
        if (score == ""):
            print("Congratulations! You shut the box! :)")
        else:
            print("\nYOU ROLLED: " + str(roll))
            print("No moves! Your score is " + score)
        return(False)
    print("")

    #humanPlay(roll,Board)
    aiPlay(roll, Board)

    return(True)

def humanPlay(roll, Board):
    sum1 = 0
    selected = []
    while (sum1 != roll):
        num = int(input("Select a Value: "))
        if num in Board:
            Board.remove(num)
            selected.append(num)
            selected.sort()

        elif num in selected:
            selected.remove(num)
            Board.append(num)
            Board.sort()

        print(selected)
        sum1 = sum(selected)

def aiPlay(roll, Board):
    combos = lookup[roll]
    set1 = []

    #find "precarious numbers" (numbers that only have 1 remaining combo left) and preserve them if possible
    preserve = findPrecariousNums(Board)

    for i in range(len(combos)):
        any_in = lambda a, b: any(i in b for i in a) #are any combo numbers in preserve?
        if(any_in(combos[i], preserve) == False):
            if(set(combos[i]).issubset(Board)):
                set1 = combos[i]
                break
        
    if (set1==[]):
        for i in range(len(combos)):
            if(set(combos[i]).issubset(Board)):
                set1 = combos[i]
                break

    for j in range(len(set1)):
        Board.remove(set1[j])

def findPrecariousNums(Board):
    preserve = []
    combo = []
    for k in range(2,13):
        numCombos = 0
        #check if lookup[num] has more than 1 viable combo
        for v in range(len(lookup[k])):
            if (set(lookup[k][v]).issubset(Board)):
                numCombos += 1
                combo = lookup[k][v]
            if (numCombos > 1):
                break
        if numCombos == 1:
            preserve.append(combo)

    flat_preserve = [item for sublist in preserve for item in sublist]
    flat_preserve = list(set(sorted(flat_preserve)))
    return(flat_preserve)
        

def main():
    Board = [1,2,3,4,5,6,7,8,9]
    playing = True

    while playing:
        playing = gameLoop(Board)
        if playing == False:
            again = str(input("Play again? yes/no\n\n"))
            if (again == "yes" or again=="y"):
                Board = [1,2,3,4,5,6,7,8,9]
                playing = True

main()


        
        





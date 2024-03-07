firstGame = list(map(int, input().split(":")))
secondGame = list(map(int, input().split(":")))
location = int(input())


sumGoalsFirstTeam = firstGame[0] + secondGame[0]
sumGoalsSecondTeam = firstGame[1] + secondGame[1]
if location == 1:
    houseGoalsFirstTeam, guestGoalsFirstTeam, guestGoalsSecondTeam, houseGoalsSecondTeam = (
        firstGame[0], secondGame[0], firstGame[1], secondGame[1]
    )
else:
    houseGoalsFirstTeam, guestGoalsFirstTeam, guestGoalsSecondTeam, houseGoalsSecondTeam = (
        secondGame[0], firstGame[0], secondGame[1], firstGame[1]
    )
    
    
if sumGoalsFirstTeam > sumGoalsSecondTeam:
    print(0)
elif sumGoalsFirstTeam == sumGoalsSecondTeam == 0:
    print(1)
else:
    if sumGoalsFirstTeam == sumGoalsSecondTeam:
        if guestGoalsFirstTeam > guestGoalsSecondTeam:
            print(0)
        else:
            print(1)
    else:
        if location == 1:
            if guestGoalsFirstTeam + (sumGoalsSecondTeam - sumGoalsFirstTeam) > guestGoalsSecondTeam:
                print(abs(sumGoalsSecondTeam - sumGoalsFirstTeam))
            else:
                print(abs(sumGoalsSecondTeam - sumGoalsFirstTeam + 1))
        else:
            if guestGoalsSecondTeam >= guestGoalsFirstTeam:
                print(abs(sumGoalsSecondTeam - sumGoalsFirstTeam + 1))
            else:
                print(abs(sumGoalsSecondTeam - sumGoalsFirstTeam))
# code for part 1
with open('rock_paper_scissor.txt', 'r') as fh:
    # set up
    # partner A= stone  B=paper  C=scissor
    # myself X=stone  Y=paper Z=scissor
    # result counting win=6 draw=3 lose=0
    # weighting Rock=1, Paper=2, Scissor=3
    tournement_list = fh.read()
    tournement_list = tournement_list.split()
    result = 0
    for i in range(0, len(tournement_list), 2):
        partner = tournement_list[i]
        myself = tournement_list[i+1]
        # result is the item I use plus win/draw/lose
        if partner == 'A' and myself == 'X':
            result = result + 1 + 3
        elif partner == 'A' and myself == 'Y':
            result = result + 2 + 6
        elif partner == 'A' and myself == 'Z':
            result = result + 3 + 0
        elif partner == 'B' and myself == 'X':
            result = result + 1 + 0
        elif partner == 'B' and myself == 'Y':
            result = result + 2 + 3
        elif partner == 'B' and myself == 'Z':
            result = result + 3 + 6
        elif partner == 'C' and myself == 'X':
            result = result + 1 + 6
        elif partner == 'C' and myself == 'Y':
            result = result + 2 + 0
        elif partner == 'C' and myself == 'Z':
            result = result + 3 + 3
        else:
            pass
print(result)


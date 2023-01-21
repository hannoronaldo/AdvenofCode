# code for part 2
with open('rock_paper_scissor.txt', 'r') as fh:
    # set up
    # partner A= stone  B=paper  C=scissor
    # result of round X=lose  Y=draw Z=win
    # result counting win=6 draw=3 lose=0
    # weighting Rock=1, Paper=2, Scissor=3
    tournement_list = fh.read()
    tournement_list = tournement_list.split()
    result = 0
    for i in range(0, len(tournement_list), 2):
        partner = tournement_list[i]
        result_of_round = tournement_list[i+1]
        # calculation is given by the use
        if partner == 'A' and result_of_round == 'X':
            result = result + 3 + 0
        elif partner == 'A' and result_of_round == 'Y':
            result = result + 1 + 3
        elif partner == 'A' and result_of_round == 'Z':
            result = result + 2 + 6
        elif partner == 'B' and result_of_round == 'X':
            result = result + 1 + 0
        elif partner == 'B' and result_of_round == 'Y':
            result = result + 2 + 3
        elif partner == 'B' and result_of_round == 'Z':
            result = result + 3 + 6
        elif partner == 'C' and result_of_round == 'X':
            result = result + 2 + 0
        elif partner == 'C' and result_of_round == 'Y':
            result = result + 3 + 3
        elif partner == 'C' and result_of_round == 'Z':
            result = result + 1 + 6
        else:
            pass
print(result)


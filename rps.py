# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(G):
    maximum_score = total_points = 0
    for francos_turn in ['R','P','S']:
        for giovannis_turn in G:
            total_points += rps(francos_turn, giovannis_turn)
        maximum_score=max(maximum_score, total_points)
        total_points=0
    return maximum_score
        


def rps(franco, giovanni):
    if(franco == 'R'):
        if(giovanni == 'R'):
            return 1
        if(giovanni == 'S'):
            return 2
        if(giovanni == 'P'):
            return 0
    if(franco == 'S'):
        if(giovanni == 'R'):
            return 0
        if(giovanni == 'S'):
            return 1
        if(giovanni == 'P'):
            return 2
    if(franco == 'P'):
        if(giovanni == 'R'):
            return 2
        if(giovanni == 'S'):
            return 0
        if(giovanni == 'P'):
            return 1

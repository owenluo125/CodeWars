# https://www.codewars.com/kata/57d29ccda56edb4187000052/python

def rpsls(pl1, pl2):
    funnydic = {"scissors" : ("paper", "lizard"),
               "paper" : ("rock", "spock"),
               "rock" : ("lizard", "scissors"),
               "lizard" : ("spock", "paper"),
               "spock" : ("scissors", "rock")}
    if pl1 == pl2:
        return "Draw!"
    elif pl2 in funnydic[pl1]:
        return "Player 1 Won!"
    else:
        return "Player 2 Won!"

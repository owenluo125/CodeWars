# https://www.codewars.com/kata/5270d0d18625160ada0000e4/python

def score(dice):
    score = 0
    count = 0
    for x in range(1,7):
        if x == 1 or x == 5:
            if (dice.count(x) // 3) < 3 and x == 1:
                score += 100 * (dice.count(x) % 3)
            elif (dice.count(x) // 3) < 3 and x == 5:
                score += 50 * (dice.count(x) % 3)
        if dice.count(x) >= 3 and x != 1:
            score += (dice.count(x) // 3) * 100 * x
        elif x == 1:
            score += (dice.count(x) // 3) * 1000
    return score
        
            

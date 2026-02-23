"""
Domain: Gaming Domain player performace ranking System

Problem statement: Design "gaming leader system:

Should includes:
1. Accept Scores from multiple matches
2.Calcaulte total Score
3. Determine player rank
4. Flag proffesional players

Rules:-
=> Total Score >= 1000 => pro players
Rank assignment:-
>= 1200 - Diamond
>= 900 - Gold
>= 600 => Sliver
else - Bronze


"""

# Gaming leaderBoard System

def analyze_player(scores):
    total = 0

    for score in scores:
        total = total + score
    
    # determine ranks
    if total >= 1200:
        rank = "Diamoun"
    elif total >= 900:
        rank = "Gold"
    elif total>= 600:
        rank = "Sliver"
    else:
        rank = "Bronze"

    # Professional tag
    if total >= 1000:
        status = "Pro player"
    else:
        status = "Noraml Player"
    
    return total,rank,status

# User input
scores = []
matches = int(input("Enter number of matches playes:"))
for i in range(matches):
    s = int(input(f"Enter score for match{i+1}:"))
    scores.append(s)

# Function Call
total , rank,status = analyze_player(scores)
#Output
print("Total Score:",total)
print("Rank:",rank)
print("Status:",status)







user_choice=(input('''
Hy welcome to score pridiction...
please select format of game....
    1: t20
    2: one day
'''))
if user_choice=="1" or user_choice=="t20":
    overs=20
    current_over=(int(input("plz enter current over of game ;")))
    current_score=int(input("plz enter current score of a team ;"))
    wickets=int(input("how many wickets or in hand ;"))
    for i in range(current_over,overs):
        if wickets>=10 and current_over<=5:
            current_score=current_score+12
        elif wickets>=7 and current_over<=10:
            current_score=current_score+9
        elif wickets>=5 and current_over<=15:
            current_score=current_score+7
        elif wickets>=1 and current_over<=20:
            current_score=current_score+3
    print("your predictor score is :", current_score)
    exit()
if user_choice=="2" or user_choice=="one day":
    overs=50
    current_over=(int(input("plz enter current over of game ;")))
    current_score=int(input("plz enter current score of a team ;"))
    wickets=int(input("how many wickets or in hand ;"))
    for i in range(current_over,overs):
        if wickets>=10 and current_over<=10:
            current_score=current_score+9
        elif wickets>=8 and current_over<=20:
            current_score=current_score+7
        elif wickets>=6 and current_over<=30:
            current_score=current_score+6
        elif wickets>=3 and current_over<=40:
            current_score=current_score+5
        elif wickets>=1 and current_over<=50:
            current_score=current_score+4
print("your predicted  score according to currint run rate  is :", current_score)









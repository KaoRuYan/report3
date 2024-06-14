#average = 成绩均值
#count = 及格人数

scores  = [int(to_score) for to_score in input().split()]
#符合if>60的to_score都會進入to_scoure
count = len([to_score for to_score in scores if(int(to_score) >= 60)])
        
average = sum(scores) /len(scores)

print("及格人數:",count)
print("輸入的成績是:" , average)

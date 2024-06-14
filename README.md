# Python期末報告
11124110 高儒彥 11124136 王何儀
# 期末報告第2題
統計學生平均成績與及格人數
# 程式碼
將輸入的成績以空格分割
並將值給予scores
```
scores  = [int(to_score) for to_score in input().split()]
```
符合成績大於60的to_score都會進入to_score
```
count = len([to_score for to_score in scores if(int(to_score) > 60)])
```
計算總平均
```
average = sum(scores) /len(scores)
```
輸出及格人數與總平均
```
print("及格人數:",count)
print("總平均為:" , average)
```
# 實作截演示
![image](https://github.com/OHIMEOPP/FinalHwPy/blob/main/FinalHwpy.png)

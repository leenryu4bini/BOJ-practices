#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2108                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: leenryu4 <boj.kr/u/leenryu4>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2108                           #+#        #+#      #+#     #
#    Solved: 2025/09/11 11:46:54 by leenryu4      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
#import numpy as np
#from scipy import stats

N= int(input())

nmlst= []
for _ in range(N):
    a= int(input())
    nmlst.append(a)

#print(nmlst)
'''
print(round(np.mean(nmlst))) #산술평균
print(int(np.median(nmlst))) #중앙값
values, counts = np.unique(nmlst, return_counts=True)
#print(values)
#print(counts)
maxc = counts.max()
cands = values[counts == maxc]
mode = cands[0] if len(cands) == 1 else sorted(cands)[1]
#stats.mode 해보았지만 tie-break 방법이 부재

print(mode) #최빈값

print(max(nmlst)-min(nmlst)) #범위'''

### numpy 안 쓰고 살아남기

from collections import Counter

#________평균 구하기________
s= sum(nmlst)
mean= round(s/N) # 0을 하면 0.0 이렇게 나온다 왤까..
print(mean)

#________중앙값 구하기________

nmlst_sort= sorted(nmlst)

if N%2==0:
    i = N // 2 - 1
    j = N // 2

    median = (nmlst_sort[i] + nmlst_sort[j]) / 2
else: 
    med= N//2
    median = nmlst_sort[med]

print(median)

#________최빈값 구하기________
counts= Counter(nmlst)
#print(counts)
maxc = max(counts.values())
#cands = i if counts[i] == maxc [오답]

#print(counts.items())

cands = [x for x, c in counts.items() if c == maxc] 
    #items로 뽑아서 count 값이 max와 같은 애들만 list로

mode = cands[0] if len(cands) == 1 else sorted(cands)[1]
print(mode) #최빈값

#________범위 구하기________
print(max(nmlst)-min(nmlst)) #범위
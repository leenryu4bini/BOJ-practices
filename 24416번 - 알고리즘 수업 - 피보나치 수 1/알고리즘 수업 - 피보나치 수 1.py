#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 24416                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: leenryu4 <boj.kr/u/leenryu4>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/24416                          #+#        #+#      #+#     #
#    Solved: 2025/09/18 18:31:06 by leenryu4      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #


# [입력 받기]

n= int(input())



# ---- 재귀 호출

'''def fib(n):
    cnt1=0
    if n==1 or n==2:
        return 1
    else: 
        cnt1+=1
        ans= fib(n-1)[0] + fib(n-2)[0] #이게 인덱싱이 안 됐음
        return ans, cnt1
    '''
#cnt return 하라고 하려고 했는데 그러면 호출할 때 오류나니까
# 못하고 있음 

# ---- 동적 프로그래밍

def fibonacci(n):
    cnt2=0

    dp= [1]*n

    for i in range(2, n):
        cnt2+=1
        dp[i]= dp[i-1] + dp[i-2]
    
    return dp[i], cnt2

#print(fib(n))
lst= list(fibonacci(n))
print(*lst)


# === 사라지지 않는 궁금증 1 ===
'''
그렇다면 dp[i]가 피보나치를 재귀함수로 돌렸을 때의
시행횟수와 같다는 것인가?

왤까?????



'''


# === 사라지지 않는 궁금증 2 ===

'''def fib(n):
    cnt1=0
    if n==1 or n==2:
        return 1
    else: 
        cnt1+=1
        ans= fib(n-1)[0] + fib(n-2)[0] #이게 인덱싱이 안 됐음
        return ans, cnt1
    '''

# -> 인덱싱이 왜 안 됐을까? 반환을 튜플로 하는데?
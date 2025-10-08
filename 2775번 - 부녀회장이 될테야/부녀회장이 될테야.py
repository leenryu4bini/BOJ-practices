#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2775                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: leenryu4 <boj.kr/u/leenryu4>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2775                           #+#        #+#      #+#     #
#    Solved: 2025/09/10 21:55:15 by leenryu4      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
 
T= int(input())

def people(mat, i, j):
    mat[i][j]= mat[i][j-1]+ mat[i+1][j]
    return mat[i][j]

for _ in range(T):
    k= int(input()) 
    n= int(input())
    
    aptmat= [[0]*n for _ in range(k+1)] #층이 k+1 층이니까.
    #열: n, 행: k+1

    #print(aptmat)

    row0 = [i+1 for i in range(n)]
    aptmat[-1] = row0[:] # 참조 공유 방지를 위해 복사본으로 넣어야 한다고 함!

    for r in range(k):      # 모든 행에 대해
        aptmat[r][0] = 1        # 첫 열을 1로 설정

    #print(aptmat)

    for i in range(k-1,-1, -1): #k-1 부터 0까지
        for j in range(1,n): #1부터 n-1까지
            aptmat[i][j]= people(aptmat, i, j)
    #print(aptmat)

    print(aptmat[0][n-1])
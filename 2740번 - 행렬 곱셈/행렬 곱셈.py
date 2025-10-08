#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2740                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: leenryu4 <boj.kr/u/leenryu4>                +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2740                           #+#        #+#      #+#     #
#    Solved: 2025/09/25 18:33:08 by leenryu4      ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

'''r1, c1= map(int, input().split())

mat_a= []

for _ in range(r1):
    mat_a.append(list(map(int, input().split())))

#print(mat_a)

r2, c2= map(int, input().split())

mat_b= []

for _ in range(r2):
    mat_b.append(list(map(int, input().split())))

#print(mat_b)

# 구현 레츠기릿 --- 1. 정석대로 해 보기

# mat_c= [] #계산 결과 담을 matrix 
# [처음에는 그냥 이와 같이 빈 리스트만 만들었움] => out of range 오류?가 났었음. indexing 오류
mat_c= [[0]*c2 for _ in range(r1)] 
# 자리를 먼저 만들어볼까 함.. 행렬의 크기는 정해져 있으니까!

#print(mat_c)


for i in range(1, r1+1): # m*n 행렬 곱하기 n*p 행렬은 m*p 행렬이니까! m에 해당하는 r1으로
    #print(i)
    for j in range(1, c2+1):
        #print(j)
        sum=0 # 시그마 구현 위해 초기화

        for k in range (1, c1+1): #어차피 c1=r2일 거임
            #print(k)
            sum += mat_a[i-1][k-1]*mat_b[k-1][j-1]
        #print(sum)
        mat_c[i-1][j-1]= sum
        #print(mat_c[i-1][j-1])

#print(mat_c)

for l in mat_c:
    print(*l)'''

#====== 분할 정복 도전!

r1, c1= map(int, input().split())

mat_a= [] #mat_a는 그대로 받기

for _ in range(r1):
    mat_a.append(list(map(int, input().split())))

print(mat_a)

r2, c2= map(int, input().split())

mat_b= []

for _ in range(r2):
    mat_b.append(list(map(int, input().split())))

print(mat_b)

#전치해보기

mat_b_t= [[0]*r2 for _ in range(c2)] 

for i in range(r2):
    for j in range(c2):
        mat_b_t[j][i] = mat_b[i][j]

print(mat_b_t)

#전치한 거 갖고 놀기!

#(근데 이게 분할 정복이 맞나?)

def mtrx_prdct(mat_unit1, mat_unit2):
    for i in range(len(mat_unit1)):
        prdct= mat_unit1[i]*mat_unit2[i]
        return prdct
    
#print(mtrx_prdct(mat_a[0], mat_b_t[0])) # 잘 작동된다

mat_c= [[0]*c2 for _ in range(r1)] #행렬곱 결과 담을 matrix


for i in range(r1): 
    for j in range(c2):
        mat_c[i][j]= mtrx_prdct(mat_a[i], mat_b_t[j])

print(mat_c)
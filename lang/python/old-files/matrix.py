A = [[1,2,3],
     [4,5,6],
     [7 ,8,9],
     [1,1,1]]

B = [[9,8,7],
     [6,5,4],
     [3,2,1],
     [1,1,1]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0],
          [0,0,0]]

# iterate through rows 
for i in range(len(A)):
# iterate through columns 
    for j in range(len(A[0])):
        result[i][j] = A[i][j] * B[i][j]

for x in result:
    print(x)

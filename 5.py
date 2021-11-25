import math 
import numpy as np 

A = np.matrix('1 1 -1; 3 -1 2; 4 4 -3')
B = np.matrix('-2; 9; -5')

print ('Check ', np.linalg.solve(A, B))
print ('Jordan-Gaus method', np.linalg.inv(A)*B)
def Jordan(a,b):
  k=1
  while k <= n-1:
    k+=1
    i=k+1
    if i<=n:
      I+=1
    j=k
    a[i][j] = a[i][j]-(a[i][k]/a[k][k])*a[k][j]
    if j<=n:
      j+=1
      a[i][j] = a[i][j]-(a[i][k]/a[k][k])*a[k][j]
    b[i] = b[i]-(a[i][k]/a[k][k]*b[k])
  else:
    print(np.linalg.solve(A,B))
    
    
print(Jordan(A,B))
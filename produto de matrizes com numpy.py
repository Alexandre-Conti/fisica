from numpy import array,dot

a=array([[1,3],[2,4]],int)
b=array([[4,-2],[-3,1]],int)
c=array([[1,2],[2,1]],int)

print(dot(a,b)+2*c)
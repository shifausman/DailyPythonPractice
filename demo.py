#repace
"""s=input("enter the main sentence")
old=input("enter the word to be replace")
new=input("enter the word to be replaced")

if old in s:
    news=s.replace(old,new)
    print(news)"""

#matrix
def matrix(mat,r,c):
    for i in range (r):
        row=[]
        for j in range (c):
            x=int(input("Enter the element:"))
            row.append(x)
        mat.append(row)

def display(mat):
   for i in mat:
       print(i)

r=int(input("enter the no. of rows"))
c=int(input("enter the no. of cols"))

mat1=[]
mat2=[]
sum=[]

matrix(mat1,r,c)
print("The matrix 1 is")
display(mat1)

matrix(mat2,r,c)
print("The matrix 2 is")
display(mat2)

for i in range (r):
        row=[]
        for j in range (c):
            row.append(0)
        sum.append(row)

for i in range (r):
    for j in range (c):
        sum[i][j]=mat1[i][j]+mat2[i][j]
print("The sum is")
display(sum)



def matrix(m,n):
    out = []
    for i in range(m):
        row =[]
        for j in range(n):
            inp = int(input(f"Enter O[{i}][{j}]: "))
            row.append(inp)
        out.append(row)
    return out

def sum(A,B):
    output=[]
    for i in range(len(A)): #number of rows
        row =[]
        for j in range(len(A[0])): # number of columns
            row.append(A[i][j]+B[i][j])
        output.append(row)
    return output

m = int(input("Enter the value of m: "))
n = int(input("Enter the value of n: "))

print("Enter the matrix A")
A = matrix(m,n)
print(A)

print("Enter the matrix B")
B = matrix(m,n)
print(B)

s = sum(A,B)
print(s)

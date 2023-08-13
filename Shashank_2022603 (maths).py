import sympy
file=open("math.txt","r")
x=file.readline().split(":")
p=int(x[1])
y=file.readline().split(":")
q=int(y[1])
matrx=[]
for _ in range (p):
    o=file.readline().split()
    matrx.append(o)
m = sympy.Matrix(matrx)
r = m.rref()[0]
#print(r)
l=list(r)
#print(l)
t=list()
a=0
b=int(len(l)/p)
h=b
for i in range(int(len(l)/q)):
    x=l[a:h]
    t.append(x)
    a=h
    h+=b
#print(t)
print("\n"+"*"*45+" RREF OF MATRIX " +"*"*45)
c=len(t[0])
for i in t:
    print(*i)

print("*"*40+" GENERAL EQUATIONS "+"*"*40)
pivot=[]
for k in range (len(t)):
    w=str()
    for l in range (c):
        if t[k][l]==0.0 or t[k][l]==-0.0:
            continue
        w+=("("+str(round(t[k][l],3))+")")+"*"+('x_'+str(l+1) +str(" + "))
    if w[:-3]=="":
        break
    print(w[:-3]," = "+"0")
for k in range (1,len(t)+1):
    for l in range (1,len(t[0])+1):
        if t[k-1][l-1]==1.0:
            pivot.append(tuple((k,l)))
            break
print("*"*100)
print("PIVOT POSITIONS :",pivot)

non_piv=[]
col=[]
for i in pivot:
    a=i[1]
    col.append(a)
for j in range (1,len(matrx[0])+1):
    if j not in col:
        non_piv.append(j-1)
#print("non piv ",non_piv)
#print("col",col)

piv_col=m.rref()[1]
#print("pivots",piv_col)
vectors = []
for b in non_piv:
    vec = [0]*q
    vec[b] = 1
    for i, pivot in enumerate(piv_col):
        vec[pivot] = -r[i, b]
    vectors.append(vec)
#print(vectors)
sol=str(str([0]*q) + " + ")
print("*"*45 + " EQUATIONS IN PARAMETRIC VECTOR FORM " + "*"*45)
for i in range (len(vectors)):
    sol+=str(f"X_{non_piv[i]+1}*{vectors[i]} + ")
print(sol[:-2])


def mean(z):
    return sum(z)/len(z)            # val returns

def mean_diff(z):
    md=[]
    mean_z=mean(z)
    for i in z:
        md.append((i-mean_z))
    return md                       # list returns

def square(z):
    md_z=[]
    md_z=mean_diff(z)
    sqrlist=[]
    for i in md_z:
        sqrlist.append(i**2)
    return sqrlist                  # list returns


def listvalmult(z1,z2):
    md_x=[]
    md_y=[]
    md_x=mean_diff(z1)
    md_y=mean_diff(z2)
    listmult=[]
    for i,j in zip(md_x,md_y):
        listmult.append(i*j)      
    return listmult                      # list returns

def variance(z):
    sqr=[]
    sqr=square(z)
    return sum(sqr)/len(z)         # val returns



def covariance(z1,z2):
    lvm=[]
    lvm=listvalmult(z1,z2)
    return sum(lvm)/len(z1)         # val returns

def linear_regression(x,y):
    var_x=variance(x)
    covar=covariance(x,y)
    mean_x=mean(x)
    mean_y=mean(y)
    m=covar/var_x
    c=mean_y-m*mean_x
    
    return m,c                     # val returns

x=[2,4,6,8]
y=[3,7,5,10]

m,c=linear_regression(x,y)
x1=int(input("Enter value to predict: \n"))
y1=m*x1+c

print("Predicted Value: ",y1)
print("slope: ",m,"Intercept: ",c)
 







def dycf(f,g):#带余除法
    q=[]
    r=[]
    if len(f)<len(g):
        return[[0],f]
    else:
        for i in range(len(f)-len(g)+1):
            c=f[i]/g[0]
            q+=[c]
            for j in range(len(g)):
                f[i+j]=f[i+j]-c*g[j]
        for i in range(len(f)):
            if f[i]!=0.0:
                for j in range(len(f)-i):
                    r+=[f[i]]
                    i+=1
                break
        if r==[]:
            r=[0]
        return [q,r]
def zdgys(f,g):#最大公因式
    if g==[0]:
        return [0]
    elif dycf(f,g)[1]==[0]:
        return g
    else:
        r=[dycf(f,g)[1]]
        _=0
        while abs(r[_][0])>10**(-13)or len(r[_])!=1:#浮点数不精确修复
            r+=[dycf(g,r[_])[1]]
            g=r[_]
            _+=1
        return r[_-1]
def cf(f,g):#多项式乘法
    ans=[0]*(len(f)+len(g)-1)
    for i in range(len(f)):
        for j in range(len(g)):
            ans[i+j]=ans[i+j]+f[i]*g[j]
    return ans
def sc(n,f):#类似向量（数组）乘数
    t=[]
    for _ in f:
        t+=[n*_]
    return t
def D(f):
    d=[]
    for i in range(len(f)-1):
        d+=[(len(f)-1-i)*f[i]]
    return d
def m(f,n):
    F=f
    for _ in range(n-1):
        F=cf(f,F)
    return F
def cys(f):
    return zdgys(f,D(f))
def s1(f):#首1多项式
    t=f[0]
    for i in range(len(f)):
        f[i]=f[i]/t
    return f
def zxgbs(f,g):#最小公倍式
    return(dycf(cf(f,g),zdgys(f,g))[0])
def ysfj(n):
    n=int(abs(n))
    q=[]
    for i in range(n):
        if n%(i+1)==0:
            q+=[i+1]
    return q+sc(-1,q)
def dxs_funiction(f,x):
    s=0
    for i in range(len(f)):
        s+=f[i]*((x)**(len(f)-i-1))
    return s


def ylg(f):#有里根
    f=by(f)#有理数域因式分解
    p=ysfj(f[0])
    q=ysfj(f[len(f)-1])
    ans=[]
    for i in p:
        for j in q:
            if abs(dxs_funiction(f,j/i))<10**-13:
                ans+=[[j,i]]
    Q=[]
    res=[]
    for _ in range(len(ans)):
        if ans[_][0]/ans[_][1] not in Q:
            Q+=[ans[_][0]/ans[_][1]]
            res+=[ans[_]]
        else:
            ans[_]=None
    
    return [res,Q]
def gys(f):
    ans=[]
    for i in range(int(max(f))):
        l=0
        for j in f:
            if j%(i+1)==0:
                l+=1
        if l==len(f):
            ans+=[i+1]
    return ans

def by(f):#本源多项式
    return sc(int(1/max(gys(f))),f)
def nxs(f):
    if len(list(set(f)))==max(f)and min(f)==1:
        s=0
        for i in range(len(f)):
            for j in range(i):
                if f[j]>f[i]:
                    s+=1
        return s
    else:
        return 'NaN,因为你的输入不是排列'
print(nxs([10,8,8,7,6,5,4,3,2,1]))


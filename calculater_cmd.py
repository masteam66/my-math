'''
\begin{array}{l}
诺把多项式f(x)=\sum_{i=0}^{n}a_ix^i记为n维向量(数组)\\
f=[a_n,a_{n-1},...,a_1,a_0]\\
是否有简便算法计算带余除法和最大公因式
\end{array}
'''
import time
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
        while abs(r[_][0])>10**(-13)and len(r[_])!=1:#浮点数不精确修复
            r+=[dycf(g,r[_])[1]]
            g=r[_]
            _+=1
        return r[_-1]
def dxs(f):#将输入的数组（向量）转换为多项式
    if len(f)==1:
        return [str(f[0]),[f[0]]]
    elif len(f)==2:
        if str(f[1])[0]!='-':
            return [f'{f[0]}x+{f[1]}',[f'{f[0]}x',f'{f[1]}']]
        else:
            return [f'{f[0]}x{f[1]}',[f'{f[0]}x',f'{f[1]}']]
    else:
        x=[]
        for i in range(len(f)-2):
            x+=[f'{f[i]}x^{len(f)-i-1}']
        x+=[f'{f[len(f)-2]}x',str(f[len(f)-1])]
        s=str(x[0])
        for _ in range(1,len(x)):
            if str(f[_])[0]!='-':
                s+='+'+x[_]
            else:
                s+=x[_]
        return [s,x]
def dycf_proof(f,g):#带余除法证明
    q=[]
    r=[]
    F=[f.copy()]
    print('计算f(x)/g(x)='+dxs(f)[0]+'/'+dxs(g)[0]+'的带余除法')
    if len(f)<len(g):
        return[[0],f]
    else:
        for i in range(len(f)-len(g)+1):
            c=f[i]/g[0]
            q+=[c]
            for j in range(len(g)):
                f[i+j]=f[i+j]-c*g[j]
            F+=[f.copy()]
        for i in range(len(f)):
            if f[i]!=0.0:
                for j in range(len(f)-i):
                    r+=[f[i]]
                    i+=1
                break
        if r==[]:
            r=[0]
        print(dxs(g)[0]+'|'+dxs(F[0])[0]+'|'+dxs(q)[0])
        
        for i in range(len(q)):
            t=[0]*len(q)
            t[i]=q[i]
            print(' '*len(dxs(g)[0])+'|'+dxs(cf(g,t))[0]+'|')
            print(' '*len(dxs(g)[0])+'|'+'-----'*len(f)+'|')
            print(' '*len(dxs(g)[0])+'|'+dxs(F[i+1])[0]+'|')
    print('f(x)=('+dxs(q)[0]+')*g(x)+'+dxs(r)[0])
    print(f'\n')
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
def dxs_preview(f):#多项式预览
    if len(f)==1:
        return str(f[0])
    elif len(f)==2:
        x=[]
        if f[0]!=0:
            if f[0]==1:
                x+=[f'x']
            elif f[0]==-1:
                x+=[f'-x']
            else:
                x+=[f'{f[0]}x']
        if f[len(f)-1]!=0:
            x+=[f'{f[1]}']
        s=str(x[0])
        for _ in range(1,len(x)):
            if str(x[_])[0]!='-':
                s+='+'+x[_]
            else:
                s+=x[_]
        return s
    else:
        x=[]
        for i in range(len(f)-2):
            if f[i]!=0:
                if f[i]==1:
                    x+=[f'x^{len(f)-i-1}']
                elif f[i]==-1:
                    x+=[f'-x^{len(f)-i-1}']
                else:
                    x+=[f'{f[i]}x^{len(f)-i-1}']
        if f[len(f)-2]!=0:
            if f[len(f)-2]==1:
                x+=[f'x']
            elif f[len(f)-2]==-1:
                x+=[f'-x']
            else:
                x+=[f'{f[i]}x']
        if f[len(f)-1]!=0:
            x+=[f'{f[i]}']
        s=str(x[0])
        for _ in range(1,len(x)):
            if str(x[_])[0]!='-':
                s+='+'+x[_]
            else:
                s+=x[_]
        return s
def input_list(t):#输出为列表
    tem=''
    l=[]
    for i in t:
        if i !=',':
            tem=tem+str(i)
        else:
            if float(tem)%1==0:
                l+=[int(tem)]
            else:
                l+=[float(tem)]
            tem=''
    if tem!='':
        if float(tem)%1==0:
            l+=[int(tem)]
        else:
            l+=[float(tem)]
    return l
def s1(f):#首1多项式
    t=f[0]
    for i in range(len(f)):
        f[i]=f[i]/t
    return f

print(f'多项式计算器命令行版v1.0by masteam66，\n,使用说明：依次输入多项式系数如x^2-2则输入“1,0,-2”')
while True:
    mode=input(f'请选择模式，计算带余除法f(x)/g(x)请输入1，\n导数f‘（x）输入2，\n[f(x)]^n输入3，\n首1最大公因式(f,g)输入4,\n乘法f(x)*g(x)输入5，\nk-1重因式(f(x),f’(x))输入6\n')
    if mode =='1':
        f=input_list(input('请输入f(x):例如x^2-2则输入“1,0,-2”\n'))
        g=input_list(input('请输入g(x):例如x^2-2则输入“1,0,-2”\n'))
        dycf_proof(f,g)
        time.sleep(1)
    elif mode =='2':
        f=input_list(input('请输入f(x):例如x^2-2则输入“1,0,-2”\n'))
        print('f(x)='+dxs_preview(f)+','+'f’(x)='+dxs_preview(D(f))+f'\n')
        time.sleep(1)
    elif mode =='3':
        f=input_list(input('请输入f(x):例如x^2-2则输入“1,0,-2”\n'))
        n=int(input('输入指数n'))
        print('('+dxs_preview(f)+')^'+str(n)+'='+dxs_preview(m(f,n))+f'\n')
        time.sleep(1)
    elif mode =='4':
        f=input_list(input('请输入f(x):例如x^2-2则输入“1,0,-2”\n'))
        g=input_list(input('请输入g(x):例如x^2-2则输入“1,0,-2”\n'))
        print('f(x)='+dxs_preview(f)+'与g(x)='+dxs_preview(g)+'的首1最大公因式为'+dxs_preview(s1(zdgys(f,g)))+f'\n')
        time.sleep(1)
    elif mode =='5':
        f=input_list(input('请输入f(x):例如x^2-2则输入“1,0,-2”\n'))
        g=input_list(input('请输入g(x):例如x^2-2则输入“1,0,-2”\n'))
        print('f(x)='+dxs_preview(f)+'与g(x)='+dxs_preview(g)+'的乘积f(x)*g(x)为'+dxs_preview(cf(f,g))+f'\n')
        time.sleep(1)
    elif mode =='6':
        f=input_list(input('请输入f(x):例如x^2-2则输入“1,0,-2”\n'))
        print('f(x)='+dxs_preview(f)+'与f‘(x)='+dxs_preview(D(f))+'的最大公因式(k-1重因式)为'+dxs_preview(s1(zdgys(f,D(f))))+f'\n')
        time.sleep(1)
    else:
        print(f'错误\n')

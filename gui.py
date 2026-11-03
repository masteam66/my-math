import calculate
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
            print(' '*len(dxs(g)[0])+'|'+dxs(calculate.cf(g,t))[0]+'|')
            print(' '*len(dxs(g)[0])+'|'+'-----'*len(f)+'|')
            print(' '*len(dxs(g)[0])+'|'+dxs(F[i+1])[0]+'|')
    print('f(x)=('+dxs(q)[0]+')*g(x)+'+dxs(r)[0])
    print(f'\n')

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
                x+=[f'{f[len(f)-2]}x']
        if f[len(f)-1]!=0:
            x+=[f'{f[len(f)-1]}']
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
def ysfj_Q(f):
    Q=calculate.ylg(f)
    if Q==[[],[]]:
        return dxs_preview(f)
    else:
        s1=str(f[0])
        s2=str(f[0])
        for i in range(len(Q[1])):
            if Q[1][i]>0:
                s1+='(x-'+str(Q[1][i])+')'
                s2+='[x-('+str(abs(Q[0][i][0]))+'/'+str(abs(Q[0][i][1]))+')]'
            elif Q[1][i]==0:
                s1+='x'
                s2+='x'
            else:
                s1+='(x+'+str(-Q[1][i])+')'
                s2+='[x+('+str(abs(Q[0][i][0]))+'/'+str(abs(Q[0][i][1]))+')]'
            m=0
            while abs(calculate.dxs_funiction(f,Q[1][i]))<10**-13:
                f=calculate.dycf(f,[1,-Q[1][i]])[0]
                m+=1
            if m>1:
                s1+=f'^{m}'
                s2+=f'^{m}'
        if calculate.s1(f)!=[1.0]:
            s1+='('+dxs_preview(f)+')'
            s2+='('+dxs_preview(f)+')'
        return s1+'='+s2



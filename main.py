
import time
import calculate
import gui

print(f'多项式计算器命令行版v1.1bymasteam66，\n,使用说明：依次输入多项式系数如x^2-2则输入“1,0,-2”')
while True:
    mode=input(f'请选择模式，计算带余除法f(x)/g(x)请输入1，\n导数f‘（x）输入2，\n[f(x)]^n输入3，\n首1最大公因式(f,g)输入4,\n乘法f(x)*g(x)输入5，\nk-1重因式(f(x),f’(x))输入6\n首1最小公倍式[f(x),g(x)]输入7\n整系数多项式的有理数域因式分解输入8\n逆序数输入9\n')
    if mode =='1':
        f=gui.input_list(input('请输入f(x):例如x^2-2则输入“1,0,-2”\n'))
        g=gui.input_list(input('请输入g(x):例如x^2-2则输入“1,0,-2”\n'))
        calculate.dycf_proof(f,g)
        time.sleep(1)
    elif mode =='2':
        f=gui.input_list(input('请输入f(x):例如x^2-2则输入“1,0,-2”\n'))
        print('f(x)='+gui.dxs_preview(f)+','+'f’(x)='+gui.dxs_preview(calculate.D(f))+f'\n')
        time.sleep(1)
    elif mode =='3':
        f=gui.input_list(input('请输入f(x):例如x^2-2则输入“1,0,-2”\n'))
        n=int(input('输入指数n'))
        print('('+gui.dxs_preview(f)+')^'+str(n)+'='+gui.dxs_preview(calculate.m(f,n))+f'\n')
        time.sleep(1)
    elif mode =='4':
        f=gui.input_list(input('请输入f(x):例如x^2-2则输入“1,0,-2”\n'))
        g=gui.input_list(input('请输入g(x):例如x^2-2则输入“1,0,-2”\n'))
        print('f(x)='+gui.dxs_preview(f)+'与g(x)='+gui.dxs_preview(g)+'的首1最大公因式为'+gui.dxs_preview(calculate.s1(calculate.zdgys(f,g)))+f'\n')
        time.sleep(1)
    elif mode =='5':
        f=gui.input_list(input('请输入f(x):例如x^2-2则输入“1,0,-2”\n'))
        g=gui.input_list(input('请输入g(x):例如x^2-2则输入“1,0,-2”\n'))
        print('f(x)='+gui.dxs_preview(f)+'与g(x)='+gui.dxs_preview(g)+'的乘积f(x)*g(x)为'+gui.dxs_preview(calculate.cf(f,g))+f'\n')
        time.sleep(1)
    elif mode =='6':
        f=gui.input_list(input('请输入f(x):例如x^2-2则输入“1,0,-2”\n'))
        print('f(x)='+gui.dxs_preview(f)+'与f‘(x)='+gui.dxs_preview(calculate.D(f))+'的最大公因式(k-1重因式)为'+gui.dxs_preview(calculate.s1(calculate.zdgys(f,calculate.D(f))))+f'\n')
        time.sleep(1)
    elif mode =='7':
        f=gui.input_list(input('请输入f(x):例如x^2-2则输入“1,0,-2”\n'))
        g=gui.input_list(input('请输入g(x):例如x^2-2则输入“1,0,-2”\n'))
        print('f(x)='+gui.dxs_preview(f)+'与g(x)='+gui.dxs_preview(g)+'的首1最小公倍式为'+gui.dxs_preview(calculate.s1(calculate.zxgbs(f,g)))+f'\n')
    elif mode =='8':
        f=gui.input_list(input('请输入整系数f(x):例如x^2-2则输入“1,0,-2”\n'))
        print('f(x)='+gui.dxs_preview(f)+','+'f(x)='+gui.ysfj_Q(f)+f'\n')
        time.sleep(1)
    elif mode =='9':
        f=gui.input_list(input('请输入逆序数:例如231则输入“2,3,1”\n'))
        print('改排列的逆序数为'+str(calculate.nxs(f))+f'\n')
        time.sleep(1)
    else:
        print(f'错误\n')


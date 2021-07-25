# -*- coding: utf-8 -*-
import sympy
import sys

max_prime=pow(10,20)
min_prime=pow(10,19)
p=sympy.randprime(min_prime,max_prime)
q=sympy.randprime(min_prime,max_prime)
while(p==q):
    q=sympy.randprime(min_prime,max_prime)
n=p*q
L=sympy.lcm(p-1,q-1)
MAX=max(p,q)
e=sympy.randprime(MAX+1,L)
print("大文字のみは進数＝26,引く数＝65 全文字使う場合は進数＝95,引く数＝32")
sin=(input("進数="))
k=(input("引く数="))
k=int(k)
sin=int(sin)

while True:

    print("Select mode.")
    try:
        mode=int(input("Encryption - 1 , Decryption - 2 , Quit - 3\n"))
    except:
        sys.exit()

    if mode==1:

        Plain=(input("Insert plain text="))
        plist=list(Plain)
        keta=len(plist)
        Pn=0
        
        for i in range(keta):
            Pa=(ord(plist[i]))-k
            Pa=Pa*(pow(sin,keta-(i+1)))
            Pn=Pn+Pa
        
        C=pow(Pn,e,n)
        
        nketa=0
        for i in range(10**9):
            if C<sin**i:
                nketa=nketa+i
                break
        ans=[0]*nketa
        check=0
        for i in range(1,nketa+1):
            j=C//(sin**(nketa-i))
            ans[check]=j
            check=check+1
            C=C-(j)*(sin**(nketa-i))
        
        nlen=len(ans)
        clist=[]
        for i in range(nlen):
            X=ans[i]+k
            X=chr(X)
            clist.append(X)
        
        ctxt=(''.join(clist))

        print()
        print(ctxt)
        print()
        
    elif mode==2:
    
        d=sympy.gcdex(e,L)
        d=(d[0])%L
        d=int(d)
        Crypt=(input("Insert crypt text="))
        clist=list(Crypt)
        keta=len(clist)
        Cn=0
    
        for i in range(keta):
            Ca=(ord(clist[i]))-k
            Ca=Ca*(pow(sin,keta-(i+1)))
            Cn=Cn+Ca
            
        P=pow(Cn,d,n)
        
        nketa=0
        for i in range(10**9):
            if P<sin**i:
                nketa=nketa+i
                break
        ans=[0]*nketa
        check=0
        for i in range(1,nketa+1):
            j=P//(sin**(nketa-i))
            ans[check]=j
            check=check+1
            P=P-(j)*(sin**(nketa-i))
        
        nlen=len(ans)
        pplist=[]
        for i in range(nlen):
            X=ans[i]+k
            X=chr(X)
            pplist.append(X)
        
        ptxt=(''.join(pplist))
        
        print()
        print(ptxt)
        print()
        
    else:
        print("End of program.")
        break
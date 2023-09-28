import math
class D:
    def end(asd):
        print("magical prime")
    def csd(asd):
        print("neon number")
class M(D):
    def mp(asd,n):
        
        m=n
        c=0
        for i in range(1,n+1):
            if(n%i==0):
                c=c+1
        if(c==2):
            
            r=0
            s=0
            while(n>0):
                r = n % 10 
                n = n // 10
                s = (s*10)+r
           
            d=0
            for i in range(1,s+1):
                if(s%i==0):
                    d=d+1
            if(d==2):
                return [m,s]
        return []
            
        
class P(D):
    def nn(asd, a):  
        s = 0
        g = int(math.pow(a, 2))
        while g > 0:
            r = g % 10
            g = int(g / 10)  
            s = s + r
        if(s==a):
            print(s)
        
a=int(input("Enter 1 for magical number or it will be neon number:"))
if(a==1):
    s=set()
    for n in range(0,100):
        c=M()
        for i in c.mp(n):
            s.add(i)
    print(s)
else:
    for n in range(0,100):
        c=P()
        c.nn(n)
    
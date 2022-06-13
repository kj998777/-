import turtle
import math
t=turtle. Turtle()
t1=turtle.Turtle()
t.speed(100)
t1.speed(100)
f=True
#좌표축 그리기
t1.hideturtle()
t.hideturtle()
t1.pu()
t1.goto(0,0)
t1.pd()
t1.forward(800)
t1.backward(1600)
t1.forward(800)  
t1.left(90)
t1.forward(400)
t1.backward(800)
t1.forward(400)
t1.right (90)
t1.goto(-800,0)
for i in range(-20,21):
    if i!=0:
        t1.left(90)
        t1.forward(10)
        t1.backward(20)
        t1.pu()
        t1.backward(10)
        t1.write(i)
        t1.forward(10)
        t1.pd()
        t1.forward(10)
        t1.right(90)
        t1.forward(40)
    else:
        t1.forward(40)
t1.goto(0,0)
t1.goto(0,-400)
t1.left(90)
for i in range(-10,11):
    t1.left(90)
    t1.forward(10)
    t1.backward(20)
    t1.pu()
    t1.backward(3)
    t1.write(i)
    t1.forward(3)
    t1.pd()
    t1.forward(10)
    t1.right(90)
    t1.forward(40)
t1.goto(0,0)
t1.right(90)
    #함수 그리기

while 0==0:
    print("그릴 함수(방정식)를 선택해 주세요.")
    h=int(input("1.삼각함수 2.다항함수 3.로그함수 4.지수함수 5.원(방정식)(번호를 선택해주세요):"))
    if h==1:
        print("삼각함수를 선택하세요.")
        j=int(input("1.sin함수 2.cos함수 3.tan함수 (번호를 선택해주세요):"))
        if j==1:
            print("y=a*sin(b(x-m))+n")
            b1=float(input("a값을 입력해주세요:"))
            a1=float(input("b값을 입력해주세요:"))
            c1=float(input("x축으로 몇만큼 평행이동 하겠습니까?(m값)"))
            d1=float(input("y축으로 몇만큼 평행이동 하겠습니까?(n값)"))
            ab=input("절댓값을 씌우겠습니까?(y/n)")
            def s(x):
                a=math.sin(x)
                return a
            if ab=="n":
                t.pu()
                t.goto(-800,s(-800))
                t.pd()
                k=-20
                while k<=20:
                    k=k+0.05
                    t.goto(40*k,40*(b1*s(a1*(k-c1))+d1))
            elif ab=="y":
                if s(-800)>=0:
                    t.pu()
                    t.goto(-800,s(-800))
                    t.pd()
                    k=-20
                elif s(-800)<0:
                    t.pu()
                    t.goto(-800,-s(-800))
                    t.pd()
                    k=-20
                while k<=20:
                    k=k+0.05
                    if 40*(b1*s(a1*(k-c1))+d1)>=0:
                        t.goto(40*k,40*(b1*s(a1*(k-c1))+d1))
                    elif 40*(b1*s(a1*(k-c1))+d1)<0:
                        t.goto(40*k,-40*(b1*s(a1*(k-c1))+d1))
                    
        elif j==2:
            print("y=a*cos(b(x-m))+n")
            b1=float(input("a값을 입력해주세요:"))
            a1=float(input("b값을 입력해주세요:"))
            c1=float(input("x축으로 몇만큼 평행이동 하겠습니까?(m값)"))
            d1=float(input("y축으로 몇만큼 평행이동 하겠습니까?(n값)"))
            ab=input("절댓값을 씌우겠습니까?(y/n)")
            def s(x):
                a=math.cos(x)
                return a
            t.pu()
            t.goto(-800,s(-800))
            t.pd()
            k=-20
            if ab=="n":
                t.pu()
                t.goto(-800,s(-800))
                t.pd()
                k=-20
                while k<=20:
                    k=k+0.05
                    t.goto(40*k,40*(b1*s(a1*(k-c1))+d1))
            elif ab=="y":
                if s(-800)>=0:
                    t.pu()
                    t.goto(-800,s(-800))
                    t.pd()
                    k=-20
                elif s(-800)<0:
                    t.pu()
                    t.goto(-800,-s(-800))
                    t.pd()
                    k=-20
                while k<=20:
                    k=k+0.05
                    if 40*(b1*s(a1*(k-c1))+d1)>=0:
                        t.goto(40*k,40*(b1*s(a1*(k-c1))+d1))
                    elif 40*(b1*s(a1*(k-c1))+d1)<0:
                        t.goto(40*k,-40*(b1*s(a1*(k-c1))+d1))
        elif j==3:
            print("y=a*tan(b(x-m))+n")
            b1=float(input("a값을 입력해주세요:"))
            a1=float(input("b값을 입력해주세요:"))
            c1=float(input("x축으로 몇만큼 평행이동 하겠습니까?(m값)"))
            d1=float(input("y축으로 몇만큼 평행이동 하겠습니까?(n값)"))
            ab=input("절댓값을 씌우겠습니까?(y/n)")
            def s(x):
                a=math.tan(x)
                return a
            t.pu()
            t.goto(-800,s(-800))
            t.pd()
            k=-20
            if ab=="n":
                t.pu()
                t.goto(-800,s(-800))
                t.pd()
                k=-20
                while k<=20:
                    k=k+0.05
                    t.goto(40*k,40*(b1*s(a1*(k-c1))+d1))
            elif ab=="y":
                if s(-800)>=0:
                    t.pu()
                    t.goto(-800,s(-800))
                    t.pd()
                    k=-20
                elif s(-800)<0:
                    t.pu()
                    t.goto(-800,-s(-800))
                    t.pd()
                    k=-20
                while k<=20:
                    k=k+0.05
                    if 40*(b1*s(a1*(k-c1))+d1)>=0:
                        t.goto(40*k,40*(b1*s(a1*(k-c1))+d1))
                    elif 40*(b1*s(a1*(k-c1))+d1)<0:
                        t.goto(40*k,-40*(b1*s(a1*(k-c1))+d1))
        while 0==0:
            print(" ")
            e=input("함수를 초기화 하겠습니까? (y/n)")
            if e=="y":
                t.clear()
                f=False
                break
            elif e=="n":
                g=input("함수를 추가 하시겠습니까? (y/n)")
                if g=="y":
                    break
                elif g!="y" and g!="n":
                    print("잘못입력하였습니다.")
            else:
                print("잘못입력하였습니다.")
    elif h==2:
        d=[]
        def f(a,x,n):
            return a*(x**n)
        a=int(input("최고차항의 차수를 입력하세요:"))
        for i in range(a+1):
            print(a-i,end="")
            c=float(input("차항의 계수를 입력하세요:"))
            d.append(c)
        ab=input("절댓값을 씌우겠습니까?(y/n)")
        if ab=="n":
        #입력된 함수 문자로 출력하기
            print("y=",end="")
            if a==1:
                if d[0]==1:
                    print("x",end="")
                elif d[0]==0:
                    print(end="")
                elif d[0]==-1:
                    print("-x",end="")
                else:
                    print(d[0],end="")
                    print("x",end="")
            elif a==0:
                if d[0]==1:
                    print("1",end="")
                elif d[0]==0:
                    print(end="")
                else:
                    print(d[0],end="")
            else:
                if d[0]==1:
                    print("x^",end="")
                    print(a,end="")
                elif d[0]==0:
                    print(0,end="")
                elif d[0]==-1:
                    print("-x^",end="")
                    print(a,end="")
                else:
                    print(d[0],end="")
                    print("x^",end="")
                    print(a,end="")
            for i in range(1,a+1):
                if a-i==1:
                    if d[i]>=0:
                        if d[i]==1:
                            print("+x",end="")
                        elif d[i]==0:
                            print(end="")
                        else:
                            print("+",end="")
                            print(d[i],end="")
                            print("x",end="")
                    else:
                        if d[i]==-1:
                            print("-x",end="")
                        else:
                            print(d[i],end="")
                            print("x",end="")
                elif a-i==0:
                    if d[i]>=0:
                        if d[i]==1:
                            print("+1",end="")
                        elif d[i]==0:
                            print(end="")
                        else:
                            print("+",end="")
                            print(d[i],end="")
                    else:
                        if d[i]==-1:
                            print("-1",end="")
                        else:
                            print(d[i],end="")
                else:
                    if d[i]>=0:
                        if d[i]==1:
                            print("+x^",end="")
                            print(a-i,end="")
                        elif d[i]==0:
                            print(end="")
                        else:
                            print("+",end="")
                            print(d[i],end="")
                            print("x^",end="")
                            print(a-i,end="")
                    else:
                        if d[i]==-1:
                            print("-x^",end="")
                            print(a-i,end="")
                        else:
                            print(d[i],end="")
                            print("x^",end="")
                            print(a-i,end="")
            def g(n):
                b=[]
                for i in range(a+1):
                    b.append(f(d[i],n,a-i))
                return sum(b)
            t.pu()
            t.goto(-800,40*g(-20))
            t.pd()
            k=-20
            while k<=20:
                k=k+0.05
                t.goto(40*k,40*g(k))
                    

        if ab=="y":
            print("y=|",end="")
            if a==1:
                if d[0]==1:
                    print("x",end="")
                elif d[0]==0:
                    print(end="")
                elif d[0]==-1:
                    print("-x",end="")
                else:
                    print(d[0],end="")
                    print("x",end="")
            elif a==0:
                if d[0]==1:
                    print("1",end="")
                elif d[0]==0:
                    print(end="")
                else:
                    print(d[0],end="")
            else:
                if d[0]==1:
                    print("x^",end="")
                    print(a,end="")
                elif d[0]==0:
                    print(0,end="")
                elif d[0]==-1:
                    print("-x^",end="")
                    print(a,end="")
                else:
                    print(d[0],end="")
                    print("x^",end="")
                    print(a,end="")
            for i in range(1,a+1):
                if a-i==1:
                    if d[i]>=0:
                        if d[i]==1:
                            print("+x",end="")
                        elif d[i]==0:
                            print(end="")
                        else:
                            print("+",end="")
                            print(d[i],end="")
                            print("x",end="")
                    else:
                        if d[i]==-1:
                            print("-x",end="")
                        else:
                            print(d[i],end="")
                            print("x",end="")
                elif a-i==0:
                    if d[i]>=0:
                        if d[i]==1:
                            print("+1",end="")
                        elif d[i]==0:
                            print(end="")
                        else:
                            print("+",end="")
                            print(d[i],end="")
                    else:
                        if d[i]==-1:
                            print("-1",end="")
                        else:
                            print(d[i],end="")
                else:
                    if d[i]>=0:
                        if d[i]==1:
                            print("+x^",end="")
                            print(a-i,end="")
                        elif d[i]==0:
                            print(end="")
                        else:
                            print("+",end="")
                            print(d[i],end="")
                            print("x^",end="")
                            print(a-i,end="")
                    else:
                        if d[i]==-1:
                            print("-x^",end="")
                            print(a-i,end="")
                        else:
                            print(d[i],end="")
                            print("x^",end="")
                            print(a-i,end="")
            print("|",end="")
            def g(n):
                b=[]
                for i in range(a+1):
                    b.append(f(d[i],n,a-i))
                return sum(b)
            if 40*g(-20)>=0:
                t.pu()
                t.goto(-800,40*g(-20))
                t.pd()
                k=-20
                while k<=20:
                    if 40*g(k)>=0:
                        k=k+0.05
                        t.goto(40*k,40*g(k))
                    elif 40*g(k)<0:
                        k=k+0.05
                        t.goto(40*k,-40*g(k))
            elif 40*g(-20)<0:
                t.pu()
                t.goto(-800,-40*g(-20))
                t.pd()
                k=-20
                while k<=20:
                    if 40*g(k)>=0:
                        k=k+0.05
                        t.goto(40*k,40*g(k))
                    elif 40*g(k)<0:
                        k=k+0.05
                        t.goto(40*k,-40*g(k))
                    
            #함수 초기화 혹은 추가하기
        while 0==0:
            print(" ")
            e=input("함수를 초기화 하겠습니까? (y/n)")
            if e=="y":
                t.clear()
                break
            elif e=="n":
                g=input("함수를 추가 하시겠습니까? (y/n)")
                if g=="y":
                    break
                elif g!="y" and g!="n":
                    print("잘못입력하였습니다.")
            else:
                print("잘못입력하였습니다.")
    elif h==3:
        print("y=a*log_b c(x-m)+n")
        b1=float(input("a값을 입력해주세요:"))
        a1=float(input("b값을 입력해주세요:"))
        e1=float(input("c값을 입력해주세요:"))
        c1=float(input("x축으로 몇만큼 평행이동 하겠습니까?(m값)"))
        d1=float(input("y축으로 몇만큼 평행이동 하겠습니까?(n값)"))
        ab=input("절댓값을 씌우겠습니까?(y/n)")
        if a1<=0 or a1==1:
            print("잘못입력하였습니다.")
        elif e1<=0:
            print("잘못입력하였습니다.")
        else:
            k=c1
            if ab=="n":
                while k<=20+c1:
                    if k==c1:
                        k=k+0.00000001
                        t.pu()
                        f1=40*(b1*(math.log(e1*(k-c1),a1))+d1)
                        t.goto(40*k,f1)
                        t.pd()
                    else:
                        k=k+0.05
                        f1=40*(b1*(math.log(e1*(k-c1),a1))+d1)
                        t.goto(40*k,f1)
            elif ab=="y":
                while k<=20+c1:
                    if k==c1:
                        k=k+0.00000001
                        if 40*(b1*(math.log(e1*(k-c1),a1))+d1)>=0:
                            f1=40*(b1*(math.log(e1*(k-c1),a1))+d1)
                            t.pu()
                            t.goto(40*k,f1)
                            t.pd()
                        elif 40*(b1*(math.log(e1*(k-c1),a1))+d1)<0:
                            f1=40*(b1*(math.log(e1*(k-c1),a1))+d1)
                            t.pu()
                            t.goto(40*k,-f1)
                            t.pd()
                    else:
                        if 40*(b1*(math.log(e1*(k-c1),a1))+d1)>=0:
                            k=k+0.05
                            f1=40*(b1*(math.log(e1*(k-c1),a1))+d1)
                            t.goto(40*k,f1)
                        elif 40*(b1*(math.log(e1*(k-c1),a1))+d1)<0:
                            k=k+0.05
                            f1=40*(b1*(math.log(e1*(k-c1),a1))+d1)
                            t.goto(40*k,-f1)
                   
            while 0==0:
                print(" ")
                e=input("함수를 초기화 하겠습니까? (y/n)")
                if e=="y":
                    t.clear()
                    f=False
                    break
                elif e=="n":
                    g=input("함수를 추가 하시겠습니까? (y/n)")
                    if g=="y":
                        break
                    elif g!="y" and g!="n":
                        print("잘못입력하였습니다.")
                else:
                    print("잘못입력하였습니다.")
    elif h==4:
        print("y=a*b^c(x-m)+n")
        b1=float(input("a값을 입력해주세요:"))
        a1=float(input("b값을 입력해주세요:"))
        e1=float(input("c값을 입력해주세요:"))
        c1=float(input("x축으로 몇만큼 평행이동 하겠습니까?(m값)"))
        d1=float(input("y축으로 몇만큼 평행이동 하겠습니까?(n값)"))
        ab=input("절댓값을 씌우겠습니까?(y/n)")
        if a1<=0:
            print("잘못입력하였습니다.")
        else:
            if ab=="n":
                t.pu()
                t.goto(-800,40*(b1*(a1**(e1*(-20-c1)))+d1))
                t.pd()
                k=-20
                while k<=20:
                    k=k+0.05
                    t.goto(40*k,40*(b1*(a1**(e1*(k-c1)))+d1))
            elif ab=="y":
                if 40*(b1*(a1**(e1*(-20-c1)))+d1)>=0:
                    t.pu()
                    t.goto(-800,40*(b1*(a1**(e1*(-20-c1)))+d1))
                    t.pd()
                    k=-20
                    while k<=20:
                        if 40*(b1*(a1**(e1*(k-c1)))+d1)>=0:
                            k=k+0.05
                            t.goto(40*k,40*(b1*(a1**(e1*(k-c1)))+d1))
                        elif 40*(b1*(a1**(e1*(k-c1)))+d1)<0:
                            k=k+0.05
                            t.goto(40*k,-40*(b1*(a1**(e1*(k-c1)))+d1))
                elif 40*(b1*(a1**(e1*(-20-c1)))+d1)<0:
                    t.pu()
                    t.goto(-800,-40*(b1*(a1**(e1*(-20-c1)))+d1))
                    t.pd()
                    k=-20
                    while k<=20:
                        if 40*(b1*(a1**(e1*(k-c1)))+d1)>=0:
                            k=k+0.05
                            t.goto(40*k,40*(b1*(a1**(e1*(k-c1)))+d1))
                        elif 40*(b1*(a1**(e1*(k-c1)))+d1)<0:
                            k=k+0.05
                            t.goto(40*k,-40*(b1*(a1**(e1*(k-c1)))+d1))
            while 0==0:
                    print(" ")
                    e=input("함수를 초기화 하겠습니까? (y/n)")
                    if e=="y":
                        t.clear()
                        f=False
                        break
                    elif e=="n":
                        g=input("함수를 추가 하시겠습니까? (y/n)")
                        if g=="y":
                            break
                        elif g!="y" and g!="n":
                            print("잘못입력하였습니다.")
                    else:
                        print("잘못입력하였습니다.")
            
    if h==5:
        a1=float(input("원의 반지름을 입력하세요:"))
        b1=float(input("x축으로 몇만큼 평행이동 하겠습니까?"))
        c1=float(input("y축으로 몇만큼 평행이동 하겠습니까?"))
        t.pu()
        t.goto(40*b1,40*c1)
        t.dot(5)
        t.goto(40*b1,40*(c1-a1))
        t.pd()
        t.circle(40*a1)
        while 0==0:
                    print(" ")
                    e=input("방정식을 초기화 하겠습니까? (y/n)")
                    if e=="y":
                        t.clear()
                        f=False
                        break
                    elif e=="n":
                        g=input("방정식 추가 하시겠습니까? (y/n)")
                        if g=="y":
                            break
                        elif g!="y" and g!="n":
                            print("잘못입력하였습니다.")
                    else:
                        print("잘못입력하였습니다.")
    


q = int(input())
b = int(input())
p = 1
while b + q > 0:
    if q > 0:
        if p < 3:
            p += 1
        elif p == 3:
            p = 1
        if q > 3:
            q -= p
        elif q == 3:
            p = 3
            q -= p
        elif q == 2:
            p = 2
            q -= p
        elif q == 1:
            p = 1
            q -= p
        print("Ծրագիրը առաջին կույտից վերցրեց՝", p, "քար, մնաց՝", q)
    elif q == 0 and b > 0:
        if p < 3:
            p += 1
        elif p == 3:
            p = 1
        if b > 3:
            b -= p
        elif b == 3:
            p = 3
            b -= p
        elif b == 2:
            p = 2
            b -= p
        elif b == 1:
            p = 1
            b -= p
        print("Ծրագիրը երկրորդ կույտից վերցրեց՝", p, "քար, մնաց՝", b)
        if b == 0:
            print("Խաղն ավարտվեց հաղթեց (ԱԻ)ն։")
    if q > 0:
        n = int(input())
        if q >= 3:
            while n < 1 or n > 3:
                n = int(input())
        elif q == 2:
            while n < 1 or n > 2:
                n = int(input())
        elif q == 1:
            while n != 1:
                n = int(input())
        q = q - n
        print("Դուք առաջին կույտից վերցրեցիք", n, "քար մնաց՝", q)
    elif q == 0 and b > 0:
        n = int(input())
        if b >= 3:
            while n < 1 or n > 3:
                n = int(input())
        elif b == 2:
            while n < 1 or n > 2:
                n = int(input())
        elif b == 1:
            while n != 1:
                n = int(input())
        b = b - n
        print("Դուք երկրորդ կույտից վերցրեցիք՝", n, "մնաց՝", b)
        if b == 0:
            print("Շնորհավորում եմ դուք հաղթեցիք (ԱԻ) ին։")
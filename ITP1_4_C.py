while True:
    a,b,c=input().split()
    a = int(a)
    c = int(c)
    if b == "?":
        break
    if b == "+":
        print(a+c)
    if b == "-":
        print(a-c)
    if b == "*":
        print(a*c)
    if b == "/":
        print(a//c)
# 演算子が"?"になるまで繰り返し処理をします。条件分岐は問題通りです。
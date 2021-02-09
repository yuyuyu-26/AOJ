while True:
    a,b = list(map(int,input().split()))
    if a == 0 and b == 0:
        break
    if a > b:
        print(b,a)
    else:
        print(a,b)
# while文で入力が0になるまで繰り返し処理します。if文でaとbの大小を反転します。
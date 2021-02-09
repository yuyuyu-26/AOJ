while True:
    x,y=map(int,input().split())
    if x == 0 and y == 0:
        break
    for i in range(x):
        print("#"*y)
    print()
# 「文字列*数値」で繰り返しになる。最後のprint()で長方形の間に空白を入れ忘れないように。
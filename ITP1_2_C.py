x=list(map(int,input().split()))
x.sort()
print(*x)
# listで複数の要素を格納して、"list名".sort()かsorted("list名")でソートできる。
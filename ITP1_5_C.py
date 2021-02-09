while True:
    x,y=map(int,input().split())
    if x == 0 and y == 0:
        break
    for i in range(x):
        for j in range(y):
            if (i+j)%2==0:
                print("#",end="")
            else:
                print(".",end="")
        print()
    print()
# 行数と列数を足した値が偶数のときには"#"で奇数のときには"."が出力されると正解の出力となっています。print()では改行されてしまうため、引数にend=""とすることで改行しないようにします。
while True:
    H,W= map(int,input().split())
    if H==0 and W==0:
        break
    print("#"*W)
    for i in range(H-2):
        print("#"+"."*(W-2)+"#")
    print("#"*W)
    print()
# 理論としては一行目と最終行目とその間の行を分けて出力する。
# また中間層の出力では一列目と最後の列は"#"で中間の列は"."が出力されるようにする。
W,H,x,y,r = map(int,input().split())
if x - r >= 0 and x + r <= W:
    if y - r >= 0 and y + r <= H:
        print("Yes")
    else:
        print("No")
else:
    print("No")
# 円の中心のx,y座標が半径rとの加算によりエリア内に収まるかを条件分岐する
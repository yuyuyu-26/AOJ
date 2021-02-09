a,b=map(int,input().split())
print(a*b,2*(a+b))
# 一行/複数行の入力はinput().split()で取得可能。ただ、文字列として受け取るのでmapとintで数値にしてから処理する。
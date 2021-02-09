count = 0
a,b,c = map(int,input().split())
for i in range(a,b+1):
    if c % i == 0:
        count += 1
print(count)
# aからbまでの各値がcの約数かどうかを判別します。約数であった場合はcountで計測されます。rangeの範囲がaからb+1になっているのに注意(0からスタートのため)。
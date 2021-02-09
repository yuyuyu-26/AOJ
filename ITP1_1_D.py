x = int(input())
a = x % 3600
b = a % 60
print(x//3600,a//60,b,sep=":")
# sep=""で出力の区切り文字を指定する
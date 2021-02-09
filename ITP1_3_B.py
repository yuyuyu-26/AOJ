a = 0
while True:
    x = int(input())
    a += 1
    if x == 0:
        break
    print("Case {}: {}".format(a,x))
# while文で入力が0になるまで実行する。入力はwhile文の中に書かないと一度のみの取得になってしまうので注意。
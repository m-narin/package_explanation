# packageファイルの中のaverage2関数を取り込む
from package import average2

# average2関数を利用し平均値を求める

# 値を入力
array = list(map(int, input("複数の数値を,区切りで入力 => ").split(","))) 

# 入力された値で平均値を計算
ave2 = average2(*array)

# 結果の出力
print("平均値 =", ave2)



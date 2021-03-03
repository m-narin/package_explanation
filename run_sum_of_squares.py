# packageファイルの中のsum_of_squares関数を取り込む
from package import sum_of_squares

# sum_of squares関数を利用し2乗和を求める

# 値を入力
array = list(map(int, input("複数の数値を,区切りで入力 => ").split(","))) 

# 入力された値で2乗わを計算
squares = sum_of_squares(*array)

# 結果を出力
print("2乗和 =", squares)
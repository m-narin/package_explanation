# 任意の引数に対して, 平均を返す関数
def average2(*args):
    ave = sum(args)/len(args)
    return ave

# 2乗和を求める
def sum_of_squares(*args):

    total = 0

    # 受け取った値のそれぞれを2乗して足していく
    for i in args:
        total += i**2
    
    return total


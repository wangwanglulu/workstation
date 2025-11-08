def total_cola(n):
    """
    参数 n：初始可乐瓶数
    返回值：总共能喝到的可乐数量
    """
    total = n         # 喝掉的总数
    bottles = n       # 当前拥有的空瓶数

    # 只要空瓶数 >= 3，就可以继续兑换
    while bottles >= 3:
        new = bottles // 3          # 换得的新可乐数
        bottles = new + bottles % 3 # 更新空瓶（新瓶+剩余）
        total += new                # 累加喝掉的新瓶数

    return total
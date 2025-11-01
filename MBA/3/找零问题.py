#找零问题

coins = [25, 10, 5, 1]   # 面额从大到小
amount = 68              # 要找的金额
i = 0                    # 当前硬币索引
used = []                # 记录已使用的硬币

while amount > 0:
    if amount >= coins[i]:
        amount -= coins[i]
        used.append(coins[i])
    else:
        i += 1

print("使用的硬币列表：", used)
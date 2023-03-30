import tkinter as tk
import random

# 定义常量
ROWS = 40
COLS = 40
CELL_SIZE = 10
INTERVAL = 100

# 创建一个二维列表来表示网格，初始时随机设置一些单元格为活着的状态
grid = [[random.randint(0, 1) for j in range(COLS)] for i in range(ROWS)]

# 创建主窗口
root = tk.Tk()
root.title('生命演化游戏')

# 创建Canvas组件
canvas = tk.Canvas(root, width=CELL_SIZE*COLS, height=CELL_SIZE*ROWS, borderwidth=0, highlightthickness=0, bg='white')
canvas.pack()

# 定义函数来绘制网格
def draw_grid():
    canvas.delete('all')
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 1:
                canvas.create_rectangle(j*CELL_SIZE, i*CELL_SIZE, (j+1)*CELL_SIZE, (i+1)*CELL_SIZE, fill='black')
            else:
                canvas.create_rectangle(j*CELL_SIZE, i*CELL_SIZE, (j+1)*CELL_SIZE, (i+1)*CELL_SIZE, fill='white')

# 定义函数来计算下一代单元格状态
def next_generation():
    global grid
    # 创建一个二维列表来存储下一代单元格状态
    next_grid = [[0 for j in range(COLS)] for i in range(ROWS)]
    # 遍历每个单元格，计算它周围的活着的邻居数量
    for i in range(ROWS):
        for j in range(COLS):
            count = 0
            for m in range(-1, 2):
                for n in range(-1, 2):
                    row = i + m
                    col = j + n
                    if (m == 0 and n == 0) or row < 0 or row >= ROWS or col < 0 or col >= COLS:
                        continue
                    if grid[row][col] == 1:
                        count += 1
            # 根据邻居数量和当前单元格状态来计算下一代单元格状态
            if count == 3 or (count == 2 and grid[i][j] == 1):
                next_grid[i][j] = 1
    # 将下一代单元格状态赋值给当前网格
    grid = next_grid
    draw_grid()
    # 定时器，每隔一段时间调用一次next_generation函数
    root.after(INTERVAL, next_generation)

# 启动游戏
next_generation()

# 进入主循环
root.mainloop()

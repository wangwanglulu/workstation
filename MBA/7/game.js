// 定义网格大小
var ROWS = 50;
var COLS = 50;

// 创建二维数组，表示生命演化游戏的网格
var grid = new Array(ROWS);
for (var i = 0; i < ROWS; i++) {
    grid[i] = new Array(COLS);
}

// 初始化网格，随机设置一些单元格为活着的状态
for (var row = 0; row < ROWS; row++) {
    for (var col = 0; col < COLS; col++) {
        grid[row][col] = Math.random() < 0.2 ? 1 : 0;
    }
}

// 创建游戏板，将网格中的单元格转化为 DOM 元素并显示在页面上
var board = document.getElementById("board");
for (var row = 0; row < ROWS; row++) {
    for (var col = 0; col < COLS; col++) {
        var cell = document.createElement("div");
        cell.className = "cell";
        if (grid[row][col] === 1) {
            cell.classList.add("alive");
        }
        board.appendChild(cell);
    }
    var clear = document.createElement("div");
    clear.className = "clear";
    board.appendChild(clear);
}

// 定义计算下一代单元格状态的函数
function nextGeneration() {
    var nextGrid = new Array(ROWS);
    for (var i = 0; i < ROWS; i++) {
        nextGrid[i] = new Array(COLS);
    }

    // 根据生命游戏的规则计算下一代单元格的状态
    for (var row = 0; row < ROWS; row++) {
        for (var col = 0; col < COLS; col++) {
            var neighbors = countNeighbors(row, col);
            if (grid[row][col] === 1) {
                if (neighbors < 2 || neighbors > 3) {
                    nextGrid[row][col] = 0;
                } else {
                    nextGrid[row][col] = 1;
                }
            } else {
                if (neighbors === 3) {
                    nextGrid[row][col] = 1;
                } else {
                    nextGrid[row][col] = 0;
                }
            }
        }
    }

    // 将下一代单元格状态应用到网格上，并更新页面上网格中单元格的样式
    for (var row = 0; row < ROWS; row++) {
        for (var col = 0; col < COLS; col++) {
            var cell = board.children[row * (COLS + 1) + col];
            if (nextGrid[row][col] === 1) {
                cell.classList.add("alive");
            } else {
                cell.classList.remove("alive");
            }
        }
    }

    // 将下一代网格作为当前网格
    grid = nextGrid;
}

// 定义计算一个单元格周围的活着的邻居数量的函数
function countNeighbors(row, col) {
    var count = 0;
    for (var i = -1; i <= 1; i++) {
        for (var j = -1; j <= 1; j++) {
            var r = row + i;
            var c = col + j;
            if (i === 0 && j === 0) {
                // 跳过当前单元格
            } else if (r < 0 || r >= ROWS || c < 0 || c >= COLS) {
                // 超出网格边界的单元格视为死亡状态
            } else if (grid[r][c] === 1) {
                count++;
            }
        }
    }
    return count;
}

// 定时计算下一代单元格状态，并更新页面上的网格
setInterval(function() {
    nextGeneration();
}, 100);
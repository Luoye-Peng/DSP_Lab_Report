import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# ===== 全局绘图与字体设置 =====
rcParams.update({
    'font.sans-serif': ['PingFang SC', 'STHeiti', 'SimHei'],  # 中文字体（macOS）
    'axes.unicode_minus': False,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'lines.linewidth': 1.5,
    'lines.markersize': 6
})

# ===== 定义分段信号函数 =====
def x_func(n):
    """分段定义的 x(n)"""
    if -4 <= n <= -1:
        return 2 * n + 5
    elif 0 <= n <= 4:
        return 6
    else:
        return 0

# ===== 生成信号 =====
n = np.arange(-5, 6)
x = np.array([x_func(k) for k in n])

# ===== 绘制原始信号 =====
plt.figure(figsize=(6, 4))
plt.stem(n, x, basefmt=" ")
plt.title("原始信号 $x(n)$", fontsize=13)
plt.xlabel("n"); plt.ylabel("$x(n)$")
plt.grid(True); plt.tight_layout(); plt.show()

# ===== 输出 δ 加权形式 =====
print("x(n) 可表示为：")
expr = "  ".join([f"{x[i]}·δ(n-{k})" for i, k in enumerate(n) if x[i] != 0])
print(expr + "\n")

# ===== 定义三个变换信号 =====
def x1(n): return 2 * x_func(n - 2)   # x₁(n) = 2x(n−2)
def x2(n): return 2 * x_func(n + 2)   # x₂(n) = 2x(n+2)
def x3(n): return x_func(2 - n)       # x₃(n) = x(2−n)

n2 = np.arange(-8, 9)
signals = {
    "$x_1(n) = 2x(n-2)$": [x1(k) for k in n2],
    "$x_2(n) = 2x(n+2)$": [x2(k) for k in n2],
    "$x_3(n) = x(2-n)$":  [x3(k) for k in n2]
}

# ===== 循环绘图 =====
for title, seq in signals.items():
    plt.figure(figsize=(6, 4))
    plt.stem(n2, seq, basefmt=" ")
    plt.title(title, fontsize=13)
    plt.xlabel("n"); plt.ylabel("幅度")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
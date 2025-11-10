import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# ===== 全局绘图设置 =====
rcParams.update({
    'font.sans-serif': ['PingFang SC', 'STHeiti', 'SimHei'],  # 中文字体
    'axes.unicode_minus': False,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'lines.linewidth': 1.5,
    'lines.markersize': 6
})

# ===== 定义信号 =====
n = np.arange(-5, 6)
x = np.array([1, 2, 3, 4, 3, 2, 1, 0, -1, -2, -3])
y = np.array([2, 1, 0, -1, -2, -1, 0, 1, 2, 3, 4])

# ===== 各种信号运算 =====
n0 = 2
x_shift = np.array([x[i - n0] if 0 <= i - n0 < len(x) else 0 for i in range(len(x))])
x_add = x + y
x_mul = x * y
x_rev = x[::-1]
energy = np.abs(x)**2

# 打印求和、求积、能量
print(f"信号和 Σx(n) = {np.sum(x)}")
print(f"信号积 Πx(n) = {np.prod(x)}")
print(f"信号能量 Σ|x(n)|² = {np.sum(energy)}")

# ===== 信号字典化：统一绘图 =====
signals = {
    "原始信号 $x(n)$": x,
    "原始信号 $y(n)$": y,
    f"信号移位 $x(n-{n0})$": x_shift,
    "信号相加 $x(n)+y(n)$": x_add,
    "信号相乘 $x(n)\\cdot y(n)$": x_mul,
    "信号翻转 $x(-n)$": x_rev,
    "信号能量分布 $|x(n)|^2$": energy
}

# ===== 自动绘制所有图 =====
for title, seq in signals.items():
    plt.figure(figsize=(6, 4))
    plt.stem(n, seq, basefmt=" ")
    plt.title(title, fontsize=13)
    plt.xlabel("n"); plt.ylabel("幅度")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
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

# ===== 序列定义函数 =====
n = np.arange(-10, 11)

signals = {
    "单位采样序列 $\\delta(n)$": np.where(n == 0, 1, 0),
    "单位阶跃序列 $u(n)$": np.where(n >= 0, 1, 0),
    "正弦序列 $\\sin(\\omega n)$": np.sin(np.pi / 5 * n),
    "实指数序列 $a^n$": 0.8 ** n,
    "随机序列 $x(n)$": np.random.rand(len(n))
}

# ===== 绘制所有信号 =====
for title, seq in signals.items():
    plt.figure(figsize=(6, 4))
    plt.stem(n, seq, basefmt=" ")
    plt.title(title, fontsize=13)
    plt.xlabel("n"); plt.ylabel("幅度")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
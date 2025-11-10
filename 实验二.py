import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from matplotlib import rcParams

# ===== 全局绘图设置 =====
rcParams.update({
    'font.sans-serif': ['PingFang SC', 'STHeiti', 'SimHei'],  # 中文字体（macOS 常用）
    'axes.unicode_minus': False,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'lines.linewidth': 1.5,
    'lines.markersize': 6
})

# ===== 统一参数 =====
N = 40
n = np.arange(N)
imp = np.eye(1, N, 0).flatten()   # 单位脉冲 δ(n)
ustep = np.ones(N)                # 单位阶跃 u(n)

# ===== 定义系统A与系统B =====
systems = {
    "系统A（差分方程）": {
        "b": [0.866],
        "a": [1, -0.8, 0.64],
        "label": r"系统A：$H_A(z)=\frac{0.866}{1-0.8z^{-1}+0.64z^{-2}}$"
    },
    "系统B（系统函数）": {
        "b": [1, -0.5],
        "a": [1, -1, 1],
        "label": r"系统B：$H_B(z)=\frac{1-0.5z^{-1}}{1-z^{-1}+z^{-2}}$"
    }
}

# ===== 绘图函数 =====
def plot_signal(n, seq, title, ylabel="幅度"):
    plt.figure(figsize=(6, 4))
    plt.stem(n, seq, basefmt=" ")
    plt.title(title, fontsize=13)
    plt.xlabel("n"); plt.ylabel(ylabel)
    plt.grid(True); plt.tight_layout(); plt.show()

# ===== (1) 各系统的脉冲与阶跃响应 =====
for sys_name, sys in systems.items():
    b, a, label = sys["b"], sys["a"], sys["label"]

    h = signal.lfilter(b, a, imp)
    s = signal.lfilter(b, a, ustep)

    plot_signal(n, h, f"{sys_name}的脉冲响应 $h(n)$")
    plot_signal(n, s, f"{sys_name}的阶跃响应 $s(n)$")

# ===== (2) 输入信号 x(n)=u(n−3) =====
x = np.zeros(N)
x[3:] = 1.0
plot_signal(n, x, "输入信号 $x(n)=u(n-3)$")

# ===== (3) 利用卷积法求各系统输出响应 =====
for sys_name, sys in systems.items():
    b, a = sys["b"], sys["a"]
    h = signal.lfilter(b, a, imp)

    y_conv = np.convolve(x, h, mode='full')
    n_conv = np.arange(len(y_conv))

    plot_signal(n_conv, y_conv, f"{sys_name}卷积法输出 $y(n)=x(n)*h(n)$")
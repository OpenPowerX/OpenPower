# 单样本均值等效性检验

样本均值用 $\hat{\mu}$ 表示，总体均值用 $\mu$ 表示。

样本标准差用 $s$ 表示，总体标准差用 $\sigma$ 表示。

下等效界值用 $\delta_1$ 表示，上等效界值用 $\delta_2$ 表示，$\delta_1 < 0$，$\delta_2 > 0$。

$$
\begin{align*}
H_{01} &: \mu - \mu_0 \leqslant \delta_1 \;\text{或}\; H_{02}: \mu - \mu_0 \geqslant \delta_2 \\
H_1 \  &: \delta_1 < \mu - \mu_0 < \delta_2
\end{align*}
$$

以下推导过程在边界条件 $\mu - \mu_0 = \delta_1$ 和 $\mu - \mu_0 = \delta_2$ 下进行。

## _z_ 检验 {#z-test}

当总体方差 $\sigma^2$ 已知时，可使用 $z$ 检验进行推导。

在 $H_{01}$ 成立时，可构建 $z_1$ 统计量：

$$
z_1 = \frac{\hat{\mu} - \mu_0 - \delta_1}{\sigma/\sqrt{n}} \sim N(0, 1)
$$

在 $H_{02}$ 成立时，可构建 $z_2$ 统计量：

$$
z_2 = \frac{\hat{\mu} - \mu_0 - \delta_2}{\sigma/\sqrt{n}} \sim N(0, 1)
$$

在 $H_1$ 成立时，可构建 $z'_1$ 和 $z'_2$ 统计量：

$$
z'_1 = \frac{\hat{\mu} - \mu_0 - \delta_1}{\sigma/\sqrt{n}} \sim N\left(\frac{\mu - \mu_0 - \delta_1}{\sigma/\sqrt{n}}, 1\right)
$$

$$
z'_2 = \frac{\hat{\mu} - \mu_0 - \delta_2}{\sigma/\sqrt{n}} \sim N\left(\frac{\mu - \mu_0 - \delta_2}{\sigma/\sqrt{n}}, 1\right)
$$

计算检验效能：

$$
\begin{align*}
    \text{Power}
& = P(z'_1 > z_{1-\alpha} \ \cap \ z'_2 < z_{\alpha}) \\
& = P(z'_1 > z_{1-\alpha}) + P(z'_2 < z_{\alpha}) - P(z'_1 > z_{1-\alpha} \ \cup \ z'_2 < z_{\alpha}) \\
& \approx P(z'_1 > z_{1-\alpha}) + P(z'_2 < z_{\alpha}) - 1 \\
& = 1 - \Phi\left(z_{1-\alpha} - \frac{\mu - \mu_0 - \delta_1}{\sigma/\sqrt{n}}\right)
      + \Phi\left(z_{\alpha} - \frac{\mu - \mu_0 - \delta_2}{\sigma/\sqrt{n}}\right) - 1 \\
& = \Phi\left(z_{\alpha} - \frac{\mu - \mu_0 - \delta_2}{\sigma/\sqrt{n}}\right) - \Phi\left(z_{1-\alpha} - \frac{\mu - \mu_0 - \delta_1}{\sigma/\sqrt{n}}\right)
\end{align*}
$$

## _t_ 检验 {#t-test}

当总体方差 $\sigma^2$ 未知时，可使用 $t$ 检验进行推导。

在 $H_{01}$ 成立时，可构建 $t_1$ 统计量：

$$
t_1 = \frac{\hat{\mu} - \mu_0 - \delta_1}{s/\sqrt{n}} \sim t(n - 1)
$$

在 $H_{02}$ 成立时，可构建 $t_2$ 统计量：

$$
t_2 = \frac{\hat{\mu} - \mu_0 - \delta_2}{s/\sqrt{n}} \sim t(n - 1)
$$

在 $H_1$ 成立时，可构建 $t'_1$ 和 $t'_2$ 统计量：

$$
t'_1 = \frac{\hat{\mu} - \mu_0 - \delta_1}{s/\sqrt{n}} \sim t\left(n - 1, \frac{\mu - \mu_0 - \delta_1}{\sigma/\sqrt{n}}\right)
$$

$$
t'_2 = \frac{\hat{\mu} - \mu_0 - \delta_2}{s/\sqrt{n}} \sim t\left(n - 1, \frac{\mu - \mu_0 - \delta_2}{\sigma/\sqrt{n}}\right)
$$

令 $T(x;v,\lambda)$ 为自由度为 $v$，非中心参数为 $\lambda$ 的非中心 $t$ 分布的累积分布函数。

计算检验效能：

$$
\begin{align*}
    \text{Power}
& = P(t'_1 > t_{1-\alpha, n-1} \ \cap \ t'_2 < t_{\alpha, n-1}) \\
& = Q_1\left(\nu, \ t_{\alpha, n-1}, \ \frac{\mu - \mu_0 - \delta_2}{\sigma/\sqrt{n}}, \ R\right) - Q_1\left(\nu, \ t_{1-\alpha, n-1}, \ \frac{\mu - \mu_0 - \delta_1}{\sigma/\sqrt{n}}, \ R\right)
\end{align*}
$$

其中 $Q_1(\cdot)$ 表示 [第一类 Owen's Q 函数](../../appendix/owenq.md#owen-q-first-type)。

!!! quote "参考文献"

    1. Chow S C, Shao J, Wang H, et al. Sample size calculations in clinical research[M]. chapman and hall/CRC, 2017.

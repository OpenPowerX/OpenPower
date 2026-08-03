# Owen's Q 函数

非中心 $t$ 分布的累计分布函数如下：

$$
\operatorname{Pr}(T \leqslant t| \delta) = \frac{1}{\Gamma\left(\frac{\nu}{2}\right) 2^{\frac{\nu-2}{2}}} \int_0^{+\infty} \Phi\left(\frac{tx}{\sqrt{\nu}} - \delta\right) x^{\nu-1} e^{-\frac{x^2}{2}} dx
$$

以 $R$ 为分界点，将上述积分分成两部分计算：

$$
\operatorname{Pr}(T \leqslant t| \delta) = Q_1(\nu, t, \delta, R) + Q_2(\nu, t, \delta, R)
$$

## 第一类 Owen's Q 函数 {#owen-q-first-type}

$$
Q_1(\nu, t, \delta, R) = \frac{1}{\Gamma\left(\frac{\nu}{2}\right) 2^{\frac{\nu-2}{2}}} \int_0^R \Phi\left(\frac{tx}{\sqrt{\nu}} - \delta\right) x^{\nu-1} e^{-\frac{x^2}{2}} dx
$$

!!! note "极高自由度下的数值积分算法"

    当 $\nu$ 极高时，被积函数中的 $x^{\nu-1}$ 极易溢出，此时可使用变量代换 $y = \ln x$：

    $$
    \begin{align*}
        Q_1(\nu, t, \delta, R)
    & = \frac{1}{\Gamma\left(\frac{\nu}{2}\right) 2^{\frac{\nu-2}{2}}} \int_0^R \Phi\left(\frac{tx}{\sqrt{\nu}} - \delta\right) x^{\nu-1} e^{-\frac{x^2}{2}} dx \\
    & = \frac{1}{\Gamma\left(\frac{\nu}{2}\right) 2^{\frac{\nu-2}{2}}} \int_{-\infty}^{\ln R} \Phi\left(\frac{te^y}{\sqrt{\nu}} - \delta\right) (e^y)^{\nu-1} e^{-\frac{e^{2y}}{2}} e^y dy \\
    & = \frac{1}{\Gamma\left(\frac{\nu}{2}\right) 2^{\frac{\nu-2}{2}}} \int_{-\infty}^{\ln R} \Phi\left(\frac{te^y}{\sqrt{\nu}} - \delta\right) e^{\nu y - \frac{e^{2y}}{2}} dy
    \end{align*}
    $$

    做指数变换：

    $$
    Q_1(\nu, t, \delta, R) = e^{g(y)}
    $$

    $$
    g(y) = \int_{-\infty}^{\ln R} C + \ln\left[\Phi\left(\frac{te^y}{\sqrt{\nu}} - \delta\right)\right] + \nu y - \frac{e^{2y}}{2} dy
    $$

    $$
    C = \ln\left[\frac{1}{\Gamma\left(\frac{\nu}{2}\right) 2^{\frac{\nu-2}{2}}}\right] = -\ln\left[\Gamma\left(\frac{\nu}{2}\right)\right] - \frac{\nu - 2}{2} \ln 2
    $$

    随着 $\nu$ 的增大，$g(y)$ 中被积函数的大小主要由 $h(y) = C + \nu y - \frac{e^{2y}}{2}$，可求出 $h(y)$ 的最大值：

    $$
    h'(y) = \nu - e^{2y} = 0 \ \Rightarrow \ y = \frac{1}{2} \ln \nu \ \Rightarrow \ y_{max} = h\left(\frac{1}{2} \ln \nu\right) = C + \frac{\nu}{2} (\ln \nu - 1) = M
    $$

    为避免当 $\nu$ 极高时被积函数值太高导致的数值积分精度问题，将被积函数限制在近似最大值 $M$ 内：

    $$
    g(y) = \int_{-\infty}^{\ln R} C + \ln\left[\Phi\left(\frac{te^y}{\sqrt{\nu}} - \delta\right)\right] + \nu y - \frac{e^{2y}}{2} - M dy + M
    $$

    将 $Q_1$ 改写为如下形式：

    $$
    Q_1(\nu, t, \delta, R) = e^M \cdot e^{g(y) - M}
    $$

## 第二类 Owen's Q 函数 {#owen-q-second-type#}

$$
Q_2(\nu, t, \delta, R) = \frac{1}{\Gamma\left(\frac{\nu}{2}\right) 2^{\frac{\nu-2}{2}}} \int_R^{+\infty} \Phi\left(\frac{tx}{\sqrt{\nu}} - \delta\right) x^{\nu-1} e^{-\frac{x^2}{2}} dx
$$

## 双变量非中心 $t$ 分布的累计概率

设随机变量 $T_1 \sim t(v, \delta_1)$，$T_2 \sim t(v, \delta_2)$，且有：

$$
T_1 = \frac{X + \delta_1}{Y}
$$

$$
T_2 = \frac{X + \delta_2}{Y}
$$

设 $T_1$ 的临界值为 $t_1$，$T_2$ 的临界值为 $t_2$，则由 $t_1$ 和 $t_2$ 可将二维空间划分为四个象限。

定义临界交点 $R$ 为：

$$
R = \frac{\delta_1 - \delta_2}{A_1 - A_2}，\ 其中 \ A_1 = \frac{t_1}{\sqrt{\nu}}，A_2 = \frac{t_2}{\sqrt{\nu}}
$$

双变量非中心 $t$ 分布在四个象限的累积概率如下：

=== "$t_1 > t_2$ 且 $\delta_1 > \delta_2$"

    $$
    \begin{align}
    & Pr(T_1 \leqslant t_1 \cap T_2 \leqslant t_2) =     Q_1(\nu, t_1, \delta_1, R) + Q_2(\nu, t_2, \delta_2, R) \\
    & Pr(T_1 \leqslant t_1 \cap T_2 \geqslant t_2) =     Q_2(\nu, t_1, \delta_1, R) + Q_2(\nu, t_2, \delta_2, R) \\
    & Pr(T_1 \geqslant t_1 \cap T_2 \geqslant t_2) = 1 - Q_2(\nu, t_1, \delta_1, R) + Q_1(\nu, t_2, \delta_2, R) \\
    & Pr(T_1 \geqslant t_1 \cap T_2 \leqslant t_2) =     Q_1(\nu, t_2, \delta_2, R) - Q_1(\nu, t_1, \delta_1, R)
    \end{align}
    $$

    上述 4 个公式可记为 $O_1 \sim O_4$。

=== "$t_1 > t_2$ 且 $\delta_1 < \delta_2$"

    $$
    P_1 = Pr(T_1 \leqslant t_1), \ P_2 = Pr(T_2 \leqslant t_2)
    $$

    $$
    \begin{align}
    & Pr(T_1 \leqslant t_1 \cap T_2 \leqslant t_2) = P_2 \\
    & Pr(T_1 \leqslant t_1 \cap T_2 \geqslant t_2) = P_1 - P_2 \\
    & Pr(T_1 \geqslant t_1 \cap T_2 \geqslant t_2) = 1 - P_1 \\
    & Pr(T_1 \geqslant t_1 \cap T_2 \leqslant t_2) = 0
    \end{align}
    $$

!!! quote "参考文献"

    1. Owen D B. A special case of a bivariate non-central t-distribution[J]. Biometrika, 1965, 52(3/4): 437-446.

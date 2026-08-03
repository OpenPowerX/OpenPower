# 两独立样本均值等效性检验

样本均值用 $\hat{\mu}_1$ 和 $\hat{\mu}_2$ 表示，总体均值用 $\mu_1$ 和 $\mu_2$ 表示。

样本标准差用 $s_1$ 和 $s_2$ 表示，总体标准差用 $\sigma_1$ 和 $\sigma_2$ 表示。

下等效界值用 $\delta_1$ 表示，上等效界值用 $\delta_2$ 表示，$\delta_1 < 0$，$\delta_2 > 0$。

$$
\begin{align*}
H_{01} &: \mu_1 - \mu_2 \leqslant \delta_1 \;\text{或}\; H_{02}: \mu_1 - \mu_2 \geqslant \delta_2 \\
H_1 \  &: \delta_1 < \mu_1 - \mu_2 < \delta_2
\end{align*}
$$

以下推导过程在边界条件 $\mu_1 - \mu_2 = \delta_1$ 和 $\mu_1 - \mu_2 = \delta_2$ 下进行。

## _z_ 检验 {#z-test}

### 假设两组方差相等 {#z-test-equal-var}

令 $\sigma = \sigma_1 = \sigma_2$，则：

$$
\operatorname{E}(\hat{\mu}_1 - \hat{\mu}_2) = \mu_1 - \mu_2, \
\operatorname{SD}(\hat{\mu}_1 - \hat{\mu}_2) = \sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}
$$

在 $H_{01}$ 成立时，可构建 $z_1$ 统计量：

$$
z_1 = \frac{\hat{\mu}_1 - \hat{\mu}_2 - \delta_1}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim N(0, 1)
$$

在 $H_{02}$ 成立时，可构建 $z_2$ 统计量：

$$
z_2 = \frac{\hat{\mu}_1 - \hat{\mu}_2 - \delta_2}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim N(0, 1)
$$

在 $H_1$ 成立时，可构建 $z'$ 、$z'_1$ 和 $z'_2$ 统计量：

$$
z' = \frac{(\hat{\mu}_1 - \hat{\mu}_2) - (\mu_1 - \mu_2)}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim N\left(0, 1\right)
$$

$$
z'_1 = \frac{\hat{\mu}_1 - \hat{\mu}_2 - \delta_1}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim N\left(\frac{\mu_1 - \mu_2 - \delta_1}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}, 1\right)
$$

$$
z'_2 = \frac{\hat{\mu}_1 - \hat{\mu}_2 - \delta_2}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim N\left(\frac{\mu_1 - \mu_2 - \delta_2}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}, 1\right)
$$

计算检验效能：

$$
\begin{align*}
    \text{Power}
& = \operatorname{Pr}(z'_1 > z_{1-\alpha} \ \cap \ z'_2 < z_{\alpha}) \\
& = \operatorname{Pr}\left(\frac{\hat{\mu}_1 - \hat{\mu}_2 - \delta_1}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} > z_{1-\alpha} \ \cap \ \frac{\hat{\mu}_1 - \hat{\mu}_2 - \delta_2}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} < z_{\alpha}\right) \\
& = \operatorname{Pr}\left(z_{1-\alpha} + \frac{\delta_1}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} < \frac{\hat{\mu}_1 - \hat{\mu}_2}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} < z_{\alpha} + \frac{\delta_2}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}\right) \\
& = \operatorname{Pr}\left(z_{1-\alpha} + \frac{\delta_1 - (\mu_1 - \mu_2)}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} < \frac{(\hat{\mu}_1 - \hat{\mu}_2) - (\mu_1 - \mu_2)}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} < z_{\alpha} + \frac{\delta_2 - (\mu_1 - \mu_2)}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}\right) \\
& = \operatorname{Pr}\left(z_{1-\alpha} - \frac{\mu_1 - \mu_2 - \delta_1}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} < z' < z_{\alpha} - \frac{\mu_1 - \mu_2 - \delta_2}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}\right) \\
& = \Phi\left(z_{\alpha} - \frac{\mu_1 - \mu_2 - \delta_2}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}\right) - \Phi\left(z_{1-\alpha} - \frac{\mu_1 - \mu_2 - \delta_1}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}\right)
\end{align*}
$$

### 假设两组方差不等 {#z-test-unequal-var}

$$
\operatorname{E}(\hat{\mu}_1 - \hat{\mu}_2) = \mu_1 - \mu_2, \
\operatorname{SD}(\hat{\mu}_1 - \hat{\mu}_2) = \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}
$$

在 $H_{01}$ 成立时，可构建 $z_1$ 统计量：

$$
z_1 = \frac{\hat{\mu}_1 - \hat{\mu}_2 - \delta_1}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} \sim N(0, 1)
$$

在 $H_{02}$ 成立时，可构建 $z_2$ 统计量：

$$
z_2 = \frac{\hat{\mu}_1 - \hat{\mu}_2 - \delta_2}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} \sim N(0, 1)
$$

在 $H_1$ 成立时，可构建 $z'$ 、$z'_1$ 和 $z'_2$ 统计量：

$$
z' = \frac{(\hat{\mu}_1 - \hat{\mu}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} \sim N\left(0, 1\right)
$$

$$
z'_1 = \frac{\hat{\mu}_1 - \hat{\mu}_2 - \delta_1}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} \sim N\left(\frac{\mu_1 - \mu_2 - \delta_1}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}, 1\right)
$$

$$
z'_2 = \frac{\hat{\mu}_1 - \hat{\mu}_2 - \delta_2}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} \sim N\left(\frac{\mu_1 - \mu_2 - \delta_2}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}, 1\right)
$$

计算检验效能：

$$
\begin{align*}
    \text{Power}
& = \operatorname{Pr}(z'_1 > z_{1-\alpha} \ \cap \ z'_2 < z_{\alpha}) \\
& = \operatorname{Pr}\left(\frac{\hat{\mu}_1 - \hat{\mu}_2 - \delta_1}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} > z_{1-\alpha} \ \cap \ \frac{\hat{\mu}_1 - \hat{\mu}_2 - \delta_2}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} < z_{\alpha}\right) \\
& = \operatorname{Pr}\left(z_{1-\alpha} + \frac{\delta_1}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} < \frac{\hat{\mu}_1 - \hat{\mu}_2}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} < z_{\alpha} + \frac{\delta_2}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}\right) \\
& = \operatorname{Pr}\left(z_{1-\alpha} + \frac{\delta_1 - (\mu_1 - \mu_2)}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} < \frac{(\hat{\mu}_1 - \hat{\mu}_2) - (\mu_1 - \mu_2)}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} < z_{\alpha} + \frac{\delta_2 - (\mu_1 - \mu_2)}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}\right) \\
& = \operatorname{Pr}\left(z_{1-\alpha} - \frac{\mu_1 - \mu_2 - \delta_1}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}} < z' < z_{\alpha} - \frac{\mu_1 - \mu_2 - \delta_2}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}\right) \\
& = \Phi\left(z_{\alpha} - \frac{\mu_1 - \mu_2 - \delta_2}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}\right) - \Phi\left(z_{1-\alpha} - \frac{\mu_1 - \mu_2 - \delta_1}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}\right)
\end{align*}
$$

## _t_ 检验 {#t-test}

### 假设两组方差相等 {#t-test-equal-var}

当两组总体方差相等时，即 $\sigma_1^2 = \sigma_2^2$ 时，可计算合并方差 $s_c^2$ ：

$$
s_c^2 = \frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}
$$

$$
\operatorname{E}(\hat{\mu}_1 - \hat{\mu}_2) = \mu_1 - \mu_2, \
\operatorname{SD}(\hat{\mu}_1 - \hat{\mu}_2) = s_c \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}
$$

在 $H_{01}$ 成立时，可构建 $t_1$ 统计量：

$$
t_1 = \frac{\hat{\mu}_1 - \hat{\mu}_2 - \delta_1}{s_c \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim t(n_1 + n_2 - 2)
$$

在 $H_{02}$ 成立时，可构建 $t_2$ 统计量：

$$
t_2 = \frac{\hat{\mu}_1 - \hat{\mu}_2 - \delta_2}{s_c \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim t(n_1 + n_2 - 2)
$$

在 $H_1$ 成立时，可构建 $t'_1$ 和 $t'_2$ 统计量：

$$
t'_1 = \frac{\hat{\mu}_1 - \hat{\mu}_2 - \delta_1}{s_c \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim t\left(n_1 + n_2 - 2, \frac{\mu_1 - \mu_2 - \delta_1}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}\right)
$$

$$
t'_2 = \frac{\hat{\mu}_1 - \hat{\mu}_2 - \delta_2}{s_c \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}} \sim t\left(n_1 + n_2 - 2, \frac{\mu_1 - \mu_2 - \delta_2}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}\right)
$$

计算检验效能：

$$
\begin{align*}
    \text{Power}
& = P(t'_1 > t_{1-\alpha, n_1 + n_2 - 2} \ \cap \ t'_2 < t_{\alpha, n_1 + n_2 - 2}) \\
& = \begin{aligned}[t]
        & Q_1\left(n_1 + n_2 - 2, \ t_{\alpha, n_1 + n_2 - 2}, \ \frac{\mu_1 - \mu_2 - \delta_2}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}, \ R\right) \\
    - \ & Q_1\left(n_1 + n_2 - 2, \ t_{1-\alpha, n_1 + n_2 - 2}, \ \frac{\mu_1 - \mu_2 - \delta_1}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}, \ R\right)
    \end{aligned}
\end{align*}
$$

其中 $Q_1(\cdot)$ 表示 [第一类 Owen's Q 函数](../../appendix/owenq.md#owen-q-first-type)，$R$ 的表达式如下：

$$
R = \frac{\theta_1 - \theta_2}{A_1 - A_2}
$$

其中：

$$
\theta_1 = \frac{\mu_1 - \mu_2 - \delta_1}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}, \
\theta_2 = \frac{\mu_1 - \mu_2 - \delta_2}{\sigma \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}, \
A_1 = \frac{t_{1-\alpha, n_1 + n_2 - 2}}{\sqrt{n_1 + n_2 - 1}}, \
A_2 = \frac{t_{\alpha, n_1 + n_2 - 2}}{\sqrt{n_1 + n_2 - 1}}
$$

### 假设两组方差不等 {#t-test-unequal-var}

$$
\operatorname{E}(\hat{\mu}_1 - \hat{\mu}_2) = \mu_1 - \mu_2, \
\operatorname{SD}(\hat{\mu}_1 - \hat{\mu}_2) = \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}
$$

当两总体方差不相等时，即 $\sigma_1^2 \ne \sigma_2^2$ 时，可使用以下近似 $t$ 检验进行推导。

#### _Welch_ 近似 _t_ 检验 {#t-test-unequal-var-welch}

_Welch_ 对自由度进行校正：

$$
\nu' = \frac{\left(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}\right)^2}{\frac{s_1^4}{n_1^2(n_1 + 1)} + \frac{s_2^4}{n_2^2(n_2 + 1)}} - 2
$$

--8<-- [start:t-unequal-welch-algorithm]

在 $H_{01}$ 成立时，可构建 $t_1$ 统计量：

$$
t_1 = \frac{\hat{\mu}_1 - \hat{\mu}_2 - \delta_1}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}} \sim t(\nu')
$$

在 $H_{02}$ 成立时，可构建 $t_2$ 统计量：

$$
t_2 = \frac{\hat{\mu}_1 - \hat{\mu}_2 - \delta_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}} \sim t(\nu')
$$

在 $H_1$ 成立时，可构建 $t'_1$ 和 $t'_2$ 统计量：

$$
t'_1 = \frac{\hat{\mu}_1 - \hat{\mu}_2 - \delta_1}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}} \sim t\left(\nu', \frac{\mu_1 - \mu_2 - \delta_1}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}\right)
$$

$$
t'_2 = \frac{\hat{\mu}_1 - \hat{\mu}_2 - \delta_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}} \sim t\left(\nu', \frac{\mu_1 - \mu_2 - \delta_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}\right)
$$

计算检验效能：

$$
\begin{align*}
    \text{Power}
& = P(t'_1 > t_{1-\alpha, \nu'} \ \cap \ t'_2 < t_{\alpha, \nu'}) \\
& = Q_1\left(\nu', \ t_{\alpha, \nu'}, \ \frac{\mu_1 - \mu_2 - \delta_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}, \ R\right) - Q_1\left(\nu', \ t_{1-\alpha, \nu'}, \ \frac{\mu_1 - \mu_2 - \delta_1}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}, \ R\right)
\end{align*}
$$

其中 $Q_1(\cdot)$ 表示 [第一类 Owen's Q 函数](../../appendix/owenq.md#owen-q-first-type)，$R$ 的表达式如下：

$$
R = \frac{\theta_1 - \theta_2}{A_1 - A_2}
$$

其中：

$$
\theta_1 = \frac{\mu_1 - \mu_2 - \delta_1}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}, \
\theta_2 = \frac{\mu_1 - \mu_2 - \delta_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}, \
A_1 = \frac{t_{1-\alpha, \nu'}}{\sqrt{\nu'}}, \
A_2 = \frac{t_{\alpha, \nu'}}{\sqrt{\nu'}}
$$

--8<-- [end:t-unequal-welch-algorithm]

#### _Satterthwaite_ 近似 _t_ 检验 {#t-test-unequal-var-satterthwaite}

_Satterthwaite_ 对自由度进行校正：

$$
\nu' = \frac{\left(\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}\right)^2}{\frac{s_1^4}{n_1^2(n_1 - 1)} + \frac{s_2^4}{n_2^2(n_2 - 1)}}
$$

--8<-- "docs/algorithms/mean/independent/equivalence.md:t-unequal-welch-algorithm"

!!! quote "参考文献"

    1. Chow S C, Shao J, Wang H, et al. Sample size calculations in clinical research[M]. chapman and hall/CRC, 2017.

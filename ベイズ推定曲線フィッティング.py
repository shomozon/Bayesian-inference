#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# # ベイズ推定

# 正規分布
# $$
#     \mathcal N(x | \mu , \sigma^{2}) = \frac{1}{\sqrt{2\pi \sigma^{2}}}
#     \exp\left\{ -\frac{1}{2\sigma^{2}}(x - \mu)^{2}\right\}
# $$

# ベイズの定理
# $$
#     \mathrm P(\mu | \mathbf x) = \frac{\mathrm P(\mathbf x | \mu) \mathrm P(\mu)}{\mathrm P(\mathbf x)} = 
#     \frac{\mathrm P(\mathbf x | \mu)}{\int_{\mu} \mathrm P(\mathbf x | \mu)} \mathrm P(\mu) \quad \cdots (1)
# $$

# 尤度
# $$
#     \mathrm P(\mathbf x | \mu) = \prod_{ n=1 }^{N} \mathcal N(x_{n} | \mu, \beta^{-1}) = 
#     (\frac{\beta}{2\pi})^{\frac{1}{2}} \exp\{-\frac{\beta}{2} \sum_{n=1}^{N} (x_{n} - \mu)^{2}\}
# $$

# 事前確率
# $$
#     \mathrm P(\mu) = \mathcal N(\mu | \mu_{0}, \beta_{0}^{-1})
# $$

# (1)の分母はμには依存しない値なので、μの確率として、
# $$
#     \mathrm P(\mu | \mathbf x) \propto \mathrm P(\mathbf x | \mu)\mathrm P(\mu) \propto 
#     \exp\{-\frac{\beta}{2} \sum_{n=1}^{N} (x_{n} - \mu)^{2} - \frac{\beta_{0}}{2}(\mu - \mu_{0})^{2} \} \quad \cdots (2)
# $$

# (2)の値を最大にするμの値を見つける。
# $$
# \begin{eqnarray}
#     -\frac{\beta}{2} \sum_{n=1}^{N} (x_{n} - \mu)^{2} - \frac{\beta_{0}}{2}(\mu - \mu_{0})^{2} &=&
#     -\frac{1}{2}\left[(N\beta + \beta_{0})\mu^{2} - 2(\beta \sum_{n}^{N} x_{n} + \beta_{0}\mu_{0})\mu + Const\right] \\ &=&
#     -\frac{1}{2}\left[(N\beta + \beta_{0})\left\{ \mu - \frac{\beta \sum_{n}^{N} x_{n} + \beta_{0}\mu_{0}}{N\beta + \beta_{0}}\right\}^{2}  + Const \right] \\
# \end{eqnarray}
# $$

# $$
#     \therefore \mathrm P(\mu | \mathbf x) = Const  \times  \exp 
#     \left[
#         -\frac{1}{2}\underbrace{(N\beta + \beta_{0})}_{\beta_{N}}
#         \left\{ \mu - \underbrace{\frac{\beta \sum_{n}^{N} x_{n} + \beta_{0}\mu_{0}}{N\beta + \beta_{0}}}_{\mu_{N}}
#         \right\}^{2}
#     \right]
# $$

# $$
#     \therefore \mathrm P(\mu | \mathbf x) = \mathcal N(\mu | \mu_{N}, \beta_{N}^{-1})
# $$

# $$
#     \mu_{N} = \frac{\beta \frac{1}{N}\sum_{n}^{N} x_{n} + \beta_{0}\mu_{0}\frac{1}{N}}{\frac{1}{N}(N\beta + \beta_{0})} =
#     \frac{\beta \mu_{ML} + \frac{\beta_{0}}{N} \mu_{0}}{\beta + \frac{\beta_{0}}{N}} \quad
#     (\mu_{ML} = \frac{1}{N} \sum_{n=1}^{N} x_{n}) \quad, \quad \beta_{N} = \beta_{0} + N\beta
# $$

# ---

# ## よりベイズ的アプローチ

# 新しいデータのxを予測する

# $$
# \begin{eqnarray}
#     \mathrm P(x_{0} | \mathbf x) &=& \int P(\mu | \mathbf x)\mathcal N (x_{0} | \mu , \beta^{-1}) d \mu \\
#     &=& \int \mathcal N (\mu | \mu_{N}, \beta_{N}^{-1})\mathcal N (x_{0} | \mu , \beta^{-1}) d \mu 
# \end{eqnarray}
# $$

# ---

# $$
# \begin{eqnarray}
#     \mathrm P &=& \int_{-\infty}^{\infty} \mathcal N (\mu | \mu_{N}, \beta_{N}^{-1})\mathcal N (x_{0} | \mu , \beta^{-1}) d \mu \\
#     &=& \frac{\sqrt{\beta_{N} \beta}}{2 \pi} \int_{-\infty}^{\infty} \exp \left[ \underbrace{-\frac{\beta_{N}}{2}(\mu - \mu_{N})^{2} -\frac{\beta}{2}(\mu - x_{0})^{2}}_{\mathrm I}\right] d \mu
# \end{eqnarray}
# $$

# $$
# \begin{eqnarray}
#     \mathrm I &=& -\frac{\beta_{N}}{2}(\mu - \mu_{N})^{2} -\frac{\beta}{2}(\mu - x_{0})^{2} \\
#     &=& -\frac{\beta_{N}}{2}(\mu^{2} - 2\mu\mu_{N} + \mu_{N}^{2}) -\frac{\beta}{2}(\mu^{2} - 2\mu x_{0} + x_{0}^{2}) \\
#     &=& -\frac{\beta_{N} + \beta}{2}\mu^{2} + (\beta_{N}\mu_{N} + \beta x_{0})\mu -\frac{1}{2}(\beta_{N}\mu_{N}^{2} + \beta x_{0}^{2}) \\
#     &=& -\frac{\beta_{N} + \beta}{2}\left\{ \mu - \frac{\beta_{N}\mu_{N} + \beta x_{0}}{\beta_{N} + \beta}\right\}^{2} + \frac{(\beta_{N}\mu_{N} + \beta x_{0})^{2}}{2(\beta_{N} + \beta)} -\frac{1}{2}(\beta_{N}\mu_{N}^{2} + \beta x_{0}^{2})
# \end{eqnarray}
# $$

# $$
#     \therefore \mathrm P = \frac{\sqrt{\beta_{N} \beta}}{2 \pi} \exp \left[ \frac{(\beta_{N}\mu_{N} + \beta x_{0})^{2}}{2(\beta_{N} + \beta)} -\frac{1}{2}(\beta_{N}\mu_{N}^{2} + \beta x_{0}^{2}) \right] \times \underbrace{\int_{-\infty}^{\infty} \exp \left[ -\frac{\beta_{N} + \beta}{2}\left\{ \mu - Const \right\}^{2} \right] d\mu}_{\sqrt{\frac{2\pi}{\beta_{N} + \beta}}}
# $$

# $$
#     \therefore ガウス積分 \\
#     \int_{-\infty}^{\infty} e^{-\alpha x^{2}} d x = \sqrt{\frac{\pi}{\alpha}} \\
#     拡張して　\\
#     \int_{-\infty}^{\infty} \exp \left[ -(ax^{2} + bx + c) \right] dx = 
#     \exp \left[ \frac{b^{2}}{4a} - c \right] \sqrt{\frac{\pi}{\alpha}}
# $$

# $$
#     よって、 \\
# \begin{eqnarray}
#     \int_{-\infty}^{\infty} \exp \left[ -\frac{\beta_{N} + \beta}{2}\left\{ \mu - \frac{\beta_{N}\mu_{N} + \beta x_{0}}{\beta_{N} + \beta} \right\}^{2} \right] d\mu 
#     &=&
#     \int_{-\infty}^{\infty} \exp \left[ -\left\{ \frac{\beta_{N} + \beta}{2}\mu^{2} - (\beta_{N}\mu_{N} + \beta x_{0})\mu + \frac{(\beta_{N}\mu_{N} + \beta x_{0})^{2}}{2(\beta_{N} + \beta)} \right\} \right] d \mu \\
#     &=& 
#     \exp \left[ \frac{(\beta_{N}\mu_{N} + \beta x_{0})^{2}}{2(\beta_{N} + \beta)} - \frac{(\beta_{N}\mu_{N} + \beta x_{0})^{2}}{2(\beta_{N} + \beta)} \right] \sqrt{\frac{2\pi}{\beta_{N} + \beta}} \\
#     &=&
#     \sqrt{\frac{2\pi}{\beta_{N} + \beta}}
# \end{eqnarray}
# $$

# $$
#     \therefore \mathrm P = Const \ \times \ \exp \left[ \underbrace{ \frac{(\beta_{N}\mu_{N} + \beta x_{0})^{2}}{2(\beta_{N} + \beta)} -\frac{1}{2}(\beta_{N}\mu_{N}^{2} + \beta x_{0}^{2})}_{\mathrm J}\right]
# $$

# $$
# \begin{eqnarray}
#     \mathrm J &=& \frac{1}{2}\left(\underbrace{\beta - \frac{\beta^{2}}{\beta_{N} + \beta}}_{\frac{\beta_{N}\beta}{\beta_{N} + \beta}}\right)x_{0}^{2} + \frac{\beta\beta_{N}\mu_{N}}{\beta_{N} + \beta}x_{0} + Const \ (indep \ of \ x_{0}) \\
#     &=& -\frac{\beta_{N}\beta}{2(\beta_{N} + \beta)}\{ x_{0} - \mu_{N} \}^{2} + Const\ (\ indep \ of \ x_{0})
# \end{eqnarray}
# $$

# $$
#     \therefore \mathrm P = Const \ \times \ \exp\left[ -\frac{\left( \frac{1}{\beta} + \frac{1}{\beta_{N}} \right)^{2}}{2} (x_{0} - \mu_{N})^{2}\right]
# $$

# $$
#     これは、\mathrm Pが平均\mu_{N}、分散(\frac{1}{\beta} + \frac{1}{\beta_{N}})の正規分布であることを示している。 \\
#     \therefore \mathrm P = \mathcal N \left(x_{0} | \mu_{N}, \left(\frac{1}{\beta} + \frac{1}{\beta_{N}}\right)\right)
# $$

# ---

# In[ ]:





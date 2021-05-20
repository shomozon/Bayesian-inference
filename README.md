# Bayesian-inference
＊Please do not start the translation software.*
## 正規分布
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cmathcal+N%28x+%7C+%5Cmu+%2C+%5Csigma%5E%7B2%7D%29+%3D+%5Cfrac%7B1%7D%7B%5Csqrt%7B2%5Cpi+%5Csigma%5E%7B2%7D%7D%7D%0A++++%5Cexp%5Cleft%5C%7B+-%5Cfrac%7B1%7D%7B2%5Csigma%5E%7B2%7D%7D%28x+-+%5Cmu%29%5E%7B2%7D%5Cright%5C%7D" 
alt="\mathcal N(x | \mu , \sigma^{2}) = \frac{1}{\sqrt{2\pi \sigma^{2}}}
    \exp\left\{ -\frac{1}{2\sigma^{2}}(x - \mu)^{2}\right\}">
## ベイズの定理
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cmathrm+P%28%5Cmu+%7C+%5Cmathbf+x%29+%3D+%5Cfrac%7B%5Cmathrm+P%28%5Cmathbf+x+%7C+%5Cmu%29+%5Cmathrm+P%28%5Cmu%29%7D%7B%5Cmathrm+P%28%5Cmathbf+x%29%7D+%3D+%0A++++%5Cfrac%7B%5Cmathrm+P%28%5Cmathbf+x+%7C+%5Cmu%29%7D%7B%5Cint_%7B%5Cmu%7D+%5Cmathrm+P%28%5Cmathbf+x+%7C+%5Cmu%29%7D+%5Cmathrm+P%28%5Cmu%29+%5Cquad+%5Ccdots+%281%29" 
alt="\mathrm P(\mu | \mathbf x) = \frac{\mathrm P(\mathbf x | \mu) \mathrm P(\mu)}{\mathrm P(\mathbf x)} = 
    \frac{\mathrm P(\mathbf x | \mu)}{\int_{\mu} \mathrm P(\mathbf x | \mu)} \mathrm P(\mu) \quad \cdots (1)">
### 尤度
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle++%5Cmathrm+P%28%5Cmathbf+x+%7C+%5Cmu%29+%3D+%5Cprod_%7B+n%3D1+%7D%5E%7BN%7D+%5Cmathcal+N%28x_%7Bn%7D+%7C+%5Cmu%2C+%5Cbeta%5E%7B-1%7D%29+%3D+%0A++++%28%5Cfrac%7B%5Cbeta%7D%7B2%5Cpi%7D%29%5E%7B%5Cfrac%7B1%7D%7B2%7D%7D+%5Cexp%5C%7B-%5Cfrac%7B%5Cbeta%7D%7B2%7D+%5Csum_%7Bn%3D1%7D%5E%7BN%7D+%28x_%7Bn%7D+-+%5Cmu%29%5E%7B2%7D%5C%7D" 
alt=" \mathrm P(\mathbf x | \mu) = \prod_{ n=1 }^{N} \mathcal N(x_{n} | \mu, \beta^{-1}) = 
    (\frac{\beta}{2\pi})^{\frac{1}{2}} \exp\{-\frac{\beta}{2} \sum_{n=1}^{N} (x_{n} - \mu)^{2}\}">
### 事前確率
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cmathrm+P%28%5Cmu%29+%3D+%5Cmathcal+N%28%5Cmu+%7C+%5Cmu_%7B0%7D%2C+%5Cbeta_%7B0%7D%5E%7B-1%7D%29" 
alt="\mathrm P(\mu) = \mathcal N(\mu | \mu_{0}, \beta_{0}^{-1})"> \
(1)の分母はμには依存しない値なので、μの確率として、 \
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cmathrm+P%28%5Cmu+%7C+%5Cmathbf+x%29+%5Cpropto+%5Cmathrm+P%28%5Cmathbf+x+%7C+%5Cmu%29%5Cmathrm+P%28%5Cmu%29+%5Cpropto+%0A++++%5Cexp%5C%7B-%5Cfrac%7B%5Cbeta%7D%7B2%7D+%5Csum_%7Bn%3D1%7D%5E%7BN%7D+%28x_%7Bn%7D+-+%5Cmu%29%5E%7B2%7D+-+%5Cfrac%7B%5Cbeta_%7B0%7D%7D%7B2%7D%28%5Cmu+-+%5Cmu_%7B0%7D%29%5E%7B2%7D+%5C%7D+%5Cquad+%5Ccdots+%282%29" 
alt="\mathrm P(\mu | \mathbf x) \propto \mathrm P(\mathbf x | \mu)\mathrm P(\mu) \propto 
    \exp\{-\frac{\beta}{2} \sum_{n=1}^{N} (x_{n} - \mu)^{2} - \frac{\beta_{0}}{2}(\mu - \mu_{0})^{2} \} \quad \cdots (2)"> \
(2)の値を最大にするμの値を見つける。 \
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Beqnarray%7D%0A++++-%5Cfrac%7B%5Cbeta%7D%7B2%7D+%5Csum_%7Bn%3D1%7D%5E%7BN%7D+%28x_%7Bn%7D+-+%5Cmu%29%5E%7B2%7D+-+%5Cfrac%7B%5Cbeta_%7B0%7D%7D%7B2%7D%28%5Cmu+-+%5Cmu_%7B0%7D%29%5E%7B2%7D+%26%3D%26%0A++++-%5Cfrac%7B1%7D%7B2%7D%5Cleft%5B%28N%5Cbeta+%2B+%5Cbeta_%7B0%7D%29%5Cmu%5E%7B2%7D+-+2%28%5Cbeta+%5Csum_%7Bn%7D%5E%7BN%7D+x_%7Bn%7D+%2B+%5Cbeta_%7B0%7D%5Cmu_%7B0%7D%29%5Cmu+%2B+Const%5Cright%5D+%5C%5C+%26%3D%26%0A++++-%5Cfrac%7B1%7D%7B2%7D%5Cleft%5B%28N%5Cbeta+%2B+%5Cbeta_%7B0%7D%29%5Cleft%5C%7B+%5Cmu+-+%5Cfrac%7B%5Cbeta+%5Csum_%7Bn%7D%5E%7BN%7D+x_%7Bn%7D+%2B+%5Cbeta_%7B0%7D%5Cmu_%7B0%7D%7D%7BN%5Cbeta+%2B+%5Cbeta_%7B0%7D%7D%5Cright%5C%7D%5E%7B2%7D++%2B+Const+%5Cright%5D+%5C%5C%0A%5Cend%7Beqnarray%7D" 
alt="\begin{eqnarray}
    -\frac{\beta}{2} \sum_{n=1}^{N} (x_{n} - \mu)^{2} - \frac{\beta_{0}}{2}(\mu - \mu_{0})^{2} &=&
    -\frac{1}{2}\left[(N\beta + \beta_{0})\mu^{2} - 2(\beta \sum_{n}^{N} x_{n} + \beta_{0}\mu_{0})\mu + Const\right] \\ &=&
    -\frac{1}{2}\left[(N\beta + \beta_{0})\left\{ \mu - \frac{\beta \sum_{n}^{N} x_{n} + \beta_{0}\mu_{0}}{N\beta + \beta_{0}}\right\}^{2}  + Const \right] \\
\end{eqnarray}"> \
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Ctherefore+%5Cmathrm+P%28%5Cmu+%7C+%5Cmathbf+x%29+%3D+Const++%5Ctimes++%5Cexp+%0A++++%5Cleft%5B%0A++++++++-%5Cfrac%7B1%7D%7B2%7D%5Cunderbrace%7B%28N%5Cbeta+%2B+%5Cbeta_%7B0%7D%29%7D_%7B%5Cbeta_%7BN%7D%7D%0A++++++++%5Cleft%5C%7B+%5Cmu+-+%5Cunderbrace%7B%5Cfrac%7B%5Cbeta+%5Csum_%7Bn%7D%5E%7BN%7D+x_%7Bn%7D+%2B+%5Cbeta_%7B0%7D%5Cmu_%7B0%7D%7D%7BN%5Cbeta+%2B+%5Cbeta_%7B0%7D%7D%7D_%7B%5Cmu_%7BN%7D%7D%0A++++++++%5Cright%5C%7D%5E%7B2%7D%0A++++%5Cright%5D" 
alt="\therefore \mathrm P(\mu | \mathbf x) = Const  \times  \exp 
    \left[
        -\frac{1}{2}\underbrace{(N\beta + \beta_{0})}_{\beta_{N}}
        \left\{ \mu - \underbrace{\frac{\beta \sum_{n}^{N} x_{n} + \beta_{0}\mu_{0}}{N\beta + \beta_{0}}}_{\mu_{N}}
        \right\}^{2}
    \right]"> \
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Ctherefore+%5Cmathrm+P%28%5Cmu+%7C+%5Cmathbf+x%29+%3D+%5Cmathcal+N%28%5Cmu+%7C+%5Cmu_%7BN%7D%2C+%5Cbeta_%7BN%7D%5E%7B-1%7D%29" 
alt="\therefore \mathrm P(\mu | \mathbf x) = \mathcal N(\mu | \mu_{N}, \beta_{N}^{-1})"> \
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cmu_%7BN%7D+%3D+%5Cfrac%7B%5Cbeta+%5Cfrac%7B1%7D%7BN%7D%5Csum_%7Bn%7D%5E%7BN%7D+x_%7Bn%7D+%2B+%5Cbeta_%7B0%7D%5Cmu_%7B0%7D%5Cfrac%7B1%7D%7BN%7D%7D%7B%5Cfrac%7B1%7D%7BN%7D%28N%5Cbeta+%2B+%5Cbeta_%7B0%7D%29%7D+%3D%0A++++%5Cfrac%7B%5Cbeta+%5Cmu_%7BML%7D+%2B+%5Cfrac%7B%5Cbeta_%7B0%7D%7D%7BN%7D+%5Cmu_%7B0%7D%7D%7B%5Cbeta+%2B+%5Cfrac%7B%5Cbeta_%7B0%7D%7D%7BN%7D%7D+%5Cquad%0A++++%28%5Cmu_%7BML%7D+%3D+%5Cfrac%7B1%7D%7BN%7D+%5Csum_%7Bn%3D1%7D%5E%7BN%7D+x_%7Bn%7D%29+%5Cquad%2C+%5Cquad+%5Cbeta_%7BN%7D+%3D+%5Cbeta_%7B0%7D+%2B+N%5Cbeta" 
alt="\mu_{N} = \frac{\beta \frac{1}{N}\sum_{n}^{N} x_{n} + \beta_{0}\mu_{0}\frac{1}{N}}{\frac{1}{N}(N\beta + \beta_{0})} =
    \frac{\beta \mu_{ML} + \frac{\beta_{0}}{N} \mu_{0}}{\beta + \frac{\beta_{0}}{N}} \quad
    (\mu_{ML} = \frac{1}{N} \sum_{n=1}^{N} x_{n}) \quad, \quad \beta_{N} = \beta_{0} + N\beta">
## よりベイズ的アプローチ
新しいデータのxを予測する　\
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Beqnarray%7D%0A++++%5Cmathrm+P%28x_%7B0%7D+%7C+%5Cmathbf+x%29+%26%3D%26+%5Cint+P%28%5Cmu+%7C+%5Cmathbf+x%29%5Cmathcal+N+%28x_%7B0%7D+%7C+%5Cmu+%2C+%5Cbeta%5E%7B-1%7D%29+d+%5Cmu+%5C%5C%0A++++%26%3D%26+%5Cint+%5Cmathcal+N+%28%5Cmu+%7C+%5Cmu_%7BN%7D%2C+%5Cbeta_%7BN%7D%5E%7B-1%7D%29%5Cmathcal+N+%28x_%7B0%7D+%7C+%5Cmu+%2C+%5Cbeta%5E%7B-1%7D%29+d+%5Cmu+%0A%5Cend%7Beqnarray%7D%0A" 
alt="\begin{eqnarray}
    \mathrm P(x_{0} | \mathbf x) &=& \int P(\mu | \mathbf x)\mathcal N (x_{0} | \mu , \beta^{-1}) d \mu \\
    &=& \int \mathcal N (\mu | \mu_{N}, \beta_{N}^{-1})\mathcal N (x_{0} | \mu , \beta^{-1}) d \mu 
\end{eqnarray}
"> \
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Beqnarray%7D%0A++++%5Cmathrm+P+%26%3D%26+%5Cint_%7B-%5Cinfty%7D%5E%7B%5Cinfty%7D+%5Cmathcal+N+%28%5Cmu+%7C+%5Cmu_%7BN%7D%2C+%5Cbeta_%7BN%7D%5E%7B-1%7D%29%5Cmathcal+N+%28x_%7B0%7D+%7C+%5Cmu+%2C+%5Cbeta%5E%7B-1%7D%29+d+%5Cmu+%5C%5C%0A++++%26%3D%26+%5Cfrac%7B%5Csqrt%7B%5Cbeta_%7BN%7D+%5Cbeta%7D%7D%7B2+%5Cpi%7D+%5Cint_%7B-%5Cinfty%7D%5E%7B%5Cinfty%7D+%5Cexp+%5Cleft%5B+%5Cunderbrace%7B-%5Cfrac%7B%5Cbeta_%7BN%7D%7D%7B2%7D%28%5Cmu+-+%5Cmu_%7BN%7D%29%5E%7B2%7D+-%5Cfrac%7B%5Cbeta%7D%7B2%7D%28%5Cmu+-+x_%7B0%7D%29%5E%7B2%7D%7D_%7B%5Cmathrm+I%7D%5Cright%5D+d+%5Cmu%0A%5Cend%7Beqnarray%7D%0A" 
alt="\begin{eqnarray}
    \mathrm P &=& \int_{-\infty}^{\infty} \mathcal N (\mu | \mu_{N}, \beta_{N}^{-1})\mathcal N (x_{0} | \mu , \beta^{-1}) d \mu \\
    &=& \frac{\sqrt{\beta_{N} \beta}}{2 \pi} \int_{-\infty}^{\infty} \exp \left[ \underbrace{-\frac{\beta_{N}}{2}(\mu - \mu_{N})^{2} -\frac{\beta}{2}(\mu - x_{0})^{2}}_{\mathrm I}\right] d \mu
\end{eqnarray}
"> \
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Beqnarray%7D%0A++++%5Cmathrm+I+%26%3D%26+-%5Cfrac%7B%5Cbeta_%7BN%7D%7D%7B2%7D%28%5Cmu+-+%5Cmu_%7BN%7D%29%5E%7B2%7D+-%5Cfrac%7B%5Cbeta%7D%7B2%7D%28%5Cmu+-+x_%7B0%7D%29%5E%7B2%7D+%5C%5C%0A++++%26%3D%26+-%5Cfrac%7B%5Cbeta_%7BN%7D%7D%7B2%7D%28%5Cmu%5E%7B2%7D+-+2%5Cmu%5Cmu_%7BN%7D+%2B+%5Cmu_%7BN%7D%5E%7B2%7D%29+-%5Cfrac%7B%5Cbeta%7D%7B2%7D%28%5Cmu%5E%7B2%7D+-+2%5Cmu+x_%7B0%7D+%2B+x_%7B0%7D%5E%7B2%7D%29+%5C%5C%0A++++%26%3D%26+-%5Cfrac%7B%5Cbeta_%7BN%7D+%2B+%5Cbeta%7D%7B2%7D%5Cmu%5E%7B2%7D+%2B+%28%5Cbeta_%7BN%7D%5Cmu_%7BN%7D+%2B+%5Cbeta+x_%7B0%7D%29%5Cmu+-%5Cfrac%7B1%7D%7B2%7D%28%5Cbeta_%7BN%7D%5Cmu_%7BN%7D%5E%7B2%7D+%2B+%5Cbeta+x_%7B0%7D%5E%7B2%7D%29+%5C%5C%0A++++%26%3D%26+-%5Cfrac%7B%5Cbeta_%7BN%7D+%2B+%5Cbeta%7D%7B2%7D%5Cleft%5C%7B+%5Cmu+-+%5Cfrac%7B%5Cbeta_%7BN%7D%5Cmu_%7BN%7D+%2B+%5Cbeta+x_%7B0%7D%7D%7B%5Cbeta_%7BN%7D+%2B+%5Cbeta%7D%5Cright%5C%7D%5E%7B2%7D+%2B+%5Cfrac%7B%28%5Cbeta_%7BN%7D%5Cmu_%7BN%7D+%2B+%5Cbeta+x_%7B0%7D%29%5E%7B2%7D%7D%7B2%28%5Cbeta_%7BN%7D+%2B+%5Cbeta%29%7D+-%5Cfrac%7B1%7D%7B2%7D%28%5Cbeta_%7BN%7D%5Cmu_%7BN%7D%5E%7B2%7D+%2B+%5Cbeta+x_%7B0%7D%5E%7B2%7D%29%0A%5Cend%7Beqnarray%7D" 
alt="\begin{eqnarray}
    \mathrm I &=& -\frac{\beta_{N}}{2}(\mu - \mu_{N})^{2} -\frac{\beta}{2}(\mu - x_{0})^{2} \\
    &=& -\frac{\beta_{N}}{2}(\mu^{2} - 2\mu\mu_{N} + \mu_{N}^{2}) -\frac{\beta}{2}(\mu^{2} - 2\mu x_{0} + x_{0}^{2}) \\
    &=& -\frac{\beta_{N} + \beta}{2}\mu^{2} + (\beta_{N}\mu_{N} + \beta x_{0})\mu -\frac{1}{2}(\beta_{N}\mu_{N}^{2} + \beta x_{0}^{2}) \\
    &=& -\frac{\beta_{N} + \beta}{2}\left\{ \mu - \frac{\beta_{N}\mu_{N} + \beta x_{0}}{\beta_{N} + \beta}\right\}^{2} + \frac{(\beta_{N}\mu_{N} + \beta x_{0})^{2}}{2(\beta_{N} + \beta)} -\frac{1}{2}(\beta_{N}\mu_{N}^{2} + \beta x_{0}^{2})
\end{eqnarray}"> \
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Ctherefore+%5Cmathrm+P+%3D+%5Cfrac%7B%5Csqrt%7B%5Cbeta_%7BN%7D+%5Cbeta%7D%7D%7B2+%5Cpi%7D+%5Cexp+%5Cleft%5B+%5Cfrac%7B%28%5Cbeta_%7BN%7D%5Cmu_%7BN%7D+%2B+%5Cbeta+x_%7B0%7D%29%5E%7B2%7D%7D%7B2%28%5Cbeta_%7BN%7D+%2B+%5Cbeta%29%7D+-%5Cfrac%7B1%7D%7B2%7D%28%5Cbeta_%7BN%7D%5Cmu_%7BN%7D%5E%7B2%7D+%2B+%5Cbeta+x_%7B0%7D%5E%7B2%7D%29+%5Cright%5D+%5Ctimes+%5Cunderbrace%7B%5Cint_%7B-%5Cinfty%7D%5E%7B%5Cinfty%7D+%5Cexp+%5Cleft%5B+-%5Cfrac%7B%5Cbeta_%7BN%7D+%2B+%5Cbeta%7D%7B2%7D%5Cleft%5C%7B+%5Cmu+-+Const+%5Cright%5C%7D%5E%7B2%7D+%5Cright%5D+d%5Cmu%7D_%7B%5Csqrt%7B%5Cfrac%7B2%5Cpi%7D%7B%5Cbeta_%7BN%7D+%2B+%5Cbeta%7D%7D%7D" 
alt="\therefore \mathrm P = \frac{\sqrt{\beta_{N} \beta}}{2 \pi} \exp \left[ \frac{(\beta_{N}\mu_{N} + \beta x_{0})^{2}}{2(\beta_{N} + \beta)} -\frac{1}{2}(\beta_{N}\mu_{N}^{2} + \beta x_{0}^{2}) \right] \times \underbrace{\int_{-\infty}^{\infty} \exp \left[ -\frac{\beta_{N} + \beta}{2}\left\{ \mu - Const \right\}^{2} \right] d\mu}_{\sqrt{\frac{2\pi}{\beta_{N} + \beta}}}"> \
∴ ガウス積分 \
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cint_%7B-%5Cinfty%7D%5E%7B%5Cinfty%7D+e%5E%7B-%5Calpha+x%5E%7B2%7D%7D+d+x+%3D+%5Csqrt%7B%5Cfrac%7B%5Cpi%7D%7B%5Calpha%7D%7D" 
alt="\int_{-\infty}^{\infty} e^{-\alpha x^{2}} d x = \sqrt{\frac{\pi}{\alpha}}"> \
拡張して \
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cint_%7B-%5Cinfty%7D%5E%7B%5Cinfty%7D+%5Cexp+%5Cleft%5B+-%28ax%5E%7B2%7D+%2B+bx+%2B+c%29+%5Cright%5D+dx+%3D+%0A++++%5Cexp+%5Cleft%5B+%5Cfrac%7Bb%5E%7B2%7D%7D%7B4a%7D+-+c+%5Cright%5D+%5Csqrt%7B%5Cfrac%7B%5Cpi%7D%7B%5Calpha%7D%7D" 
alt="\int_{-\infty}^{\infty} \exp \left[ -(ax^{2} + bx + c) \right] dx = 
    \exp \left[ \frac{b^{2}}{4a} - c \right] \sqrt{\frac{\pi}{\alpha}}"> \
よって \
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Beqnarray%7D%0A++++%5Cint_%7B-%5Cinfty%7D%5E%7B%5Cinfty%7D+%5Cexp+%5Cleft%5B+-%5Cfrac%7B%5Cbeta_%7BN%7D+%2B+%5Cbeta%7D%7B2%7D%5Cleft%5C%7B+%5Cmu+-+%5Cfrac%7B%5Cbeta_%7BN%7D%5Cmu_%7BN%7D+%2B+%5Cbeta+x_%7B0%7D%7D%7B%5Cbeta_%7BN%7D+%2B+%5Cbeta%7D+%5Cright%5C%7D%5E%7B2%7D+%5Cright%5D+d%5Cmu+%0A++++%26%3D%26%0A++++%5Cint_%7B-%5Cinfty%7D%5E%7B%5Cinfty%7D+%5Cexp+%5Cleft%5B+-%5Cleft%5C%7B+%5Cfrac%7B%5Cbeta_%7BN%7D+%2B+%5Cbeta%7D%7B2%7D%5Cmu%5E%7B2%7D+-+%28%5Cbeta_%7BN%7D%5Cmu_%7BN%7D+%2B+%5Cbeta+x_%7B0%7D%29%5Cmu+%2B+%5Cfrac%7B%28%5Cbeta_%7BN%7D%5Cmu_%7BN%7D+%2B+%5Cbeta+x_%7B0%7D%29%5E%7B2%7D%7D%7B2%28%5Cbeta_%7BN%7D+%2B+%5Cbeta%29%7D+%5Cright%5C%7D+%5Cright%5D+d+%5Cmu+%5C%5C%0A++++%26%3D%26+%0A++++%5Cexp+%5Cleft%5B+%5Cfrac%7B%28%5Cbeta_%7BN%7D%5Cmu_%7BN%7D+%2B+%5Cbeta+x_%7B0%7D%29%5E%7B2%7D%7D%7B2%28%5Cbeta_%7BN%7D+%2B+%5Cbeta%29%7D+-+%5Cfrac%7B%28%5Cbeta_%7BN%7D%5Cmu_%7BN%7D+%2B+%5Cbeta+x_%7B0%7D%29%5E%7B2%7D%7D%7B2%28%5Cbeta_%7BN%7D+%2B+%5Cbeta%29%7D+%5Cright%5D+%5Csqrt%7B%5Cfrac%7B2%5Cpi%7D%7B%5Cbeta_%7BN%7D+%2B+%5Cbeta%7D%7D+%5C%5C%0A++++%26%3D%26%0A++++%5Csqrt%7B%5Cfrac%7B2%5Cpi%7D%7B%5Cbeta_%7BN%7D+%2B+%5Cbeta%7D%7D%0A%5Cend%7Beqnarray%7D" 
alt="\begin{eqnarray}
    \int_{-\infty}^{\infty} \exp \left[ -\frac{\beta_{N} + \beta}{2}\left\{ \mu - \frac{\beta_{N}\mu_{N} + \beta x_{0}}{\beta_{N} + \beta} \right\}^{2} \right] d\mu 
    &=&
    \int_{-\infty}^{\infty} \exp \left[ -\left\{ \frac{\beta_{N} + \beta}{2}\mu^{2} - (\beta_{N}\mu_{N} + \beta x_{0})\mu + \frac{(\beta_{N}\mu_{N} + \beta x_{0})^{2}}{2(\beta_{N} + \beta)} \right\} \right] d \mu \\
    &=& 
    \exp \left[ \frac{(\beta_{N}\mu_{N} + \beta x_{0})^{2}}{2(\beta_{N} + \beta)} - \frac{(\beta_{N}\mu_{N} + \beta x_{0})^{2}}{2(\beta_{N} + \beta)} \right] \sqrt{\frac{2\pi}{\beta_{N} + \beta}} \\
    &=&
    \sqrt{\frac{2\pi}{\beta_{N} + \beta}}
\end{eqnarray}"> \
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Ctherefore+%5Cmathrm+P+%3D+Const+%5C+%5Ctimes+%5C+%5Cexp+%5Cleft%5B+%5Cunderbrace%7B+%5Cfrac%7B%28%5Cbeta_%7BN%7D%5Cmu_%7BN%7D+%2B+%5Cbeta+x_%7B0%7D%29%5E%7B2%7D%7D%7B2%28%5Cbeta_%7BN%7D+%2B+%5Cbeta%29%7D+-%5Cfrac%7B1%7D%7B2%7D%28%5Cbeta_%7BN%7D%5Cmu_%7BN%7D%5E%7B2%7D+%2B+%5Cbeta+x_%7B0%7D%5E%7B2%7D%29%7D_%7B%5Cmathrm+J%7D%5Cright%5D" 
alt="\therefore \mathrm P = Const \ \times \ \exp \left[ \underbrace{ \frac{(\beta_{N}\mu_{N} + \beta x_{0})^{2}}{2(\beta_{N} + \beta)} -\frac{1}{2}(\beta_{N}\mu_{N}^{2} + \beta x_{0}^{2})}_{\mathrm J}\right]"> \
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cbegin%7Beqnarray%7D%0A++++%5Cmathrm+J+%26%3D%26+%5Cfrac%7B1%7D%7B2%7D%5Cleft%28%5Cunderbrace%7B%5Cbeta+-+%5Cfrac%7B%5Cbeta%5E%7B2%7D%7D%7B%5Cbeta_%7BN%7D+%2B+%5Cbeta%7D%7D_%7B%5Cfrac%7B%5Cbeta_%7BN%7D%5Cbeta%7D%7B%5Cbeta_%7BN%7D+%2B+%5Cbeta%7D%7D%5Cright%29x_%7B0%7D%5E%7B2%7D+%2B+%5Cfrac%7B%5Cbeta%5Cbeta_%7BN%7D%5Cmu_%7BN%7D%7D%7B%5Cbeta_%7BN%7D+%2B+%5Cbeta%7Dx_%7B0%7D+%2B+Const+%5C%C2%A0%28indep+%5C+of+%5C+x_%7B0%7D%29+%5C%5C%0A++++%26%3D%26+-%5Cfrac%7B%5Cbeta_%7BN%7D%5Cbeta%7D%7B2%28%5Cbeta_%7BN%7D+%2B+%5Cbeta%29%7D%5C%7B+x_%7B0%7D+-+%5Cmu_%7BN%7D+%5C%7D%5E%7B2%7D+%2B+Const%5C+%28%5C+indep+%5C+of+%5C+x_%7B0%7D%29%0A%5Cend%7Beqnarray%7D" 
alt="\begin{eqnarray}
    \mathrm J &=& \frac{1}{2}\left(\underbrace{\beta - \frac{\beta^{2}}{\beta_{N} + \beta}}_{\frac{\beta_{N}\beta}{\beta_{N} + \beta}}\right)x_{0}^{2} + \frac{\beta\beta_{N}\mu_{N}}{\beta_{N} + \beta}x_{0} + Const(indep \ of \ x_{0}) \\
    &=& -\frac{\beta_{N}\beta}{2(\beta_{N} + \beta)}\{ x_{0} - \mu_{N} \}^{2} + Const(indep \ of \ x_{0})
\end{eqnarray}"> \
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Ctherefore+%5Cmathrm+P+%3D+Const+%5C%C2%A0%5Ctimes+%5C+%5Cexp%5Cleft%5B+-%5Cfrac%7B%5Cleft%28+%5Cfrac%7B1%7D%7B%5Cbeta%7D+%2B+%5Cfrac%7B1%7D%7B%5Cbeta_%7BN%7D%7D+%5Cright%29%5E%7B2%7D%7D%7B2%7D+%28x_%7B0%7D+-+%5Cmu_%7BN%7D%29%5E%7B2%7D%5Cright%5D" 
alt="\therefore \mathrm P = Const \ \times \ \exp\left[ -\frac{\left( \frac{1}{\beta} + \frac{1}{\beta_{N}} \right)^{2}}{2} (x_{0} - \mu_{N})^{2}\right]"> \
これは、Pが平均<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cmu_%7BN%7D" 
alt="\mu_{N}">、分散<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Cfrac%7B1%7D%7B%5Cbeta%7D+%2B+%5Cfrac%7B1%7D%7B%5Cbeta_%7BN%7D%7D" 
alt="\frac{1}{\beta} + \frac{1}{\beta_{N}}">の正規分布であることを示している。 \
<img src=
"https://render.githubusercontent.com/render/math?math=%5Cdisplaystyle+%5Ctherefore+%5Cmathrm+P+%3D+%5Cmathcal+N+%5Cleft%28x_%7B0%7D+%7C+%5Cmu_%7BN%7D%2C+%5Cleft%28%5Cfrac%7B1%7D%7B%5Cbeta%7D+%2B+%5Cfrac%7B1%7D%7B%5Cbeta_%7BN%7D%7D%5Cright%29%5Cright%29" 
alt="\therefore \mathrm P = \mathcal N \left(x_{0} | \mu_{N}, \left(\frac{1}{\beta} + \frac{1}{\beta_{N}}\right)\right)">

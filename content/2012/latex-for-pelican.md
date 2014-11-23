Title: Pelican 的 LaTeX 集成
Date: 2012-02-18 05:48
Category: Technique
Tags: LaTeX, Pelican, MathJax
Slug: latex-pelican
Mathjax: true

本文主要用于测试 Pelican 与 MathJax 配合显示数学公式

## 为 Pelican 添加 MathJax 支持
鉴于并非每篇文章都会有数学公式，而`MathJax.js`的资源加载在国内并不稳定，因此只在需要显示数学公式的 HTML 文件里才添加`MathJax CDN`。一个简单的方法是在需要公式显示的文章里加入`mathjax=true`的元数据声明：
```text
Markdown
Mathjax: true
reST
:mathjax: true
HTML
< meta name="mathjax" content="true" />
```

然后还需要在 Pelican 的主题文件添加判断是否需要启用 MathJax 的`Jinja`代码，将以下代码保存在空文件`THEME/templates/mathjax.html`中：
```jinja
{# LaTeX mathjax support
    If the post has metadata "mathjax=true", then add mathjax cdn support
#}
{% if article.mathjax %}
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['$','$'], ["\\(","\\)"] ],
      processEscapes: true
    }
  });
</script>
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
{% endif %}
```

加速国内访问可以使用 [www.freecdn.cn](http://www.freecdn.cn/) 或者`GitCafe`上的地址：
```html
<script src="http://libs.cncdn.cn/mathjax/2.3/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/javascript" src="http://pkuwwt.gitcafe.com/MathJax/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
```
在需要判断是否开启 MathJax 的模板文件中（比如`index.html`、`article.html`等）的合适位置添加`{% include "mathjax.html" %}`

## 公式编辑
### HTML 文档
`MathJax.js`的作用是把 HTML 源文件中的公式 Block 转换为 CSS 的字体和位置控制代码
。公式块的声明有三种：
```LaTeX
\( ... Inline Equation ... \)

\[ ... Displayed Equation ... \]

$$ ... Displayed Equation ... $$
```
默认唯独不支持`$ ... Inline Equation ... $`方式（可手动设置）。

洛伦兹方程：
```text
$$\begin{aligned}
\dot{x} = \sigma(y-x) \\
\dot{y} = \rho x - y - xz \\
\dot{z} = -\beta z + xy
\end{aligned}$$
```

$$\begin{aligned}
\dot{x} = \sigma(y-x) \\
\dot{y} = \rho x - y - xz \\
\dot{z} = -\beta z + xy
\end{aligned}$$

Cauchy-Schwarz不等式：
```text
\\[ \left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right) \\]
```

\\[ \left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right) \\]


### 标记语言文档
应该注意到标记语言需要先转换为 HTML 文档，此过程中需要控制特殊字符`\`，因此用非 
HTML 的标记语言写作时必须写成`\\`的格式转换为 HTML 时才会得到正确的`\`，比如在
`Markdown`中。

## 测试
毕达哥拉斯定理：\\(a^2+b^2=c^2\\)

正态分布：$$f\left(x\right)=\frac{1}{\sqrt{2\pi}\sigma}exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

傅里叶变换：
\\[F\left(\omega\right)=\mathcal{F}\left[f(t)\right]=\int_{-\infty}^{\infty}e^{-i\omega
T}dt\\]

傅里叶逆变换：
\\[f\left(t\right)=\mathcal{F}^{-1}\left[F\left(\omega\right)\right]=\frac{1}{2\pi}\int_{-\infty}^{\infty}F\left(\omega\right)e^{i\omega t}d\omega\\]

MathJax的语法基本与latex一致，可以参考wikipedia的latex书写语法规范[Help:数学公式](http://zh.wikipedia.org/wiki/Help:%E6%95%B0%E5%AD%A6%E5%85%AC%E5%BC%8F)

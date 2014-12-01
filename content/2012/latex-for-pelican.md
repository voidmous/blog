Title: Pelican 的 LaTeX 集成
Date: 2012-02-18 05:48
Category: Technique
Tags: LaTeX, Pelican, MathJax, Markdown, Python
Slug: latex-pelican
Mathjax: true

本文主要用于测试 Pelican 与 MathJax 配合显示数学公式。

## 为 Pelican 添加 MathJax 支持

鉴于并非每篇文章都会有数学公式，而`MathJax.js`的资源加载在国内并不稳定，因此只在需要显示数学公式的 HTML 文件里才添加`MathJax CDN`。一个简单的方法是在需要公式显示的文章里加入`mathjax=true`的元数据声明：
```text
Markdown Style
Mathjax: true

reST Style
:mathjax: true

HTML Style
< meta name="mathjax" content="true" />
```

然后还需要在 Pelican 的主题模板文件中添加判断是否需要启用 MathJax 的`Jinja`代码，将以下代码保存在空文件`THEME/templates/mathjax.html`中：
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

官方的CDN国内无法稳定地加载，加速国内访问可以使用 [www.freecdn.cn](http://www.freecdn.cn/) 或者`GitCafe`上的地址：
```html
<script src="http://libs.cncdn.cn/mathjax/2.3/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/javascript" src="http://pkuwwt.gitcafe.com/MathJax/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
```
在需要判断是否开启 MathJax 的模板文件中（比如`index.html`、`article.html`等可能需要显示公式的模板）的合适位置添加`{% include "mathjax.html" %}`

## 公式编辑

### HTML 文档

`MathJax.js`的作用是把 HTML 源文件中的公式 Block 转换为 CSS 的字体和位置控制代码
。公式块的声明有三种：
```LaTeX
\( ... Inline Equation ... \)

\[ ... Displayed Equation ... \]

$$ ... Displayed Equation ... $$
```
默认唯独不支持`$ ... Inline Equation ... $`方式（可手动设置，见上）。

### Markdown
Markdown 文本首先需要被转换为 HTML 文档，而后在浏览器中渲染时`MathJax.js`才会寻找定义
的公式块。由于 Markdown 无法识别 MathJax 定义的公式块，因此公式块内的文本都会被当成普通文本处理，一些特殊符号尤其需要特别注意，比如`\`和`_`、`*`这几个字符，前一个为 Markdown 转义符，后两个为强调指示符。

由于 Pelican 使用的 Markdown 解析器是[Python-Markdown](https://pythonhosted.org/Markdown/index.html)，而它默认禁用了[下划线强调规则](https://pythonhosted.org/Markdown/#differences)，因此公式中的`_`一般情况都不会被转换为`<em></em>`，但`*`和`\`解析的麻烦仍然存在。

一个`*`解析的示例：
```text
$$ x*y*z=100 $$
```
Markdown 转换为 HTML 的结果为：
```html
<p>$$ x<em>y</em>z=100 $$</p>
```
此处作为乘号的两个`*`被识别成强调指示符，正确的代码应为：
```text
$$ x\*y\*z=100 $$
```
渲染结果如下：
$$ x\*y\*z=100 $$

`\`解析问题以洛伦兹方程为例：
```text
\[\begin{aligned}
\dot{x} & = \sigma(y-x) \\
\dot{y} & = \rho x - y - xz \\
\dot{z} & = -\beta z + xy
\end{aligned}\]
```
Markdown 转换为 HTML 的结果如下：
```text
<p>[\begin{aligned}
\dot{x} = \sigma(y-x) \
\dot{y} = \rho x - y - xz \
\dot{z} = -\beta z + xy
\end{aligned}]</p>
```
注意`\a-z`的解析不受影响，而$\LaTeX$的换行代码`\\`被转换为`\`，
`\[`被转换为`[`，显然这不是想要的结果。为了得到正确的解析结果，公式代码必须改为：
```text
\\[\begin{aligned}
\dot{x} & = \sigma(y-x) \\\\
\dot{y} & = \rho x - y - xz \\\\
\dot{z} & = -\beta z + xy
\end{aligned}\\]
```
显示结果如下：
\\[\begin{aligned}
\dot{x} & = \sigma(y-x) \\\\
\dot{y} & = \rho x - y - xz \\\\
\dot{z} & = -\beta z + xy
\end{aligned}\\]

通过上面的例子可见通过添加 Markdown 转义符`\`可以有效解决各种转换问题，手工调整的方法虽然繁琐，但不失简单直接，如果公式不多不复杂这样做成本很低。对于强迫症患者或者要求较高的童鞋，还可以参考[这里的方法](http://gohugo.io/tutorials/mathjax/)
。它可以解决所有特殊符号解析的难题，只要保证`CSS`和`MathJax`设置一致，使用其它 Markdown
解析器处理也不会有问题。其思路是将公式写入 Markdown 不处理的`verbatim`环境中，在 MathJax
 设置中加入对`code`标签内容的渲染并设置一个合适的式样。

此外，我们也可以使用 Python-Markdown 的扩展 [python-markdown-mathjax](https://github.com/mayoff/python-markdown-mathjax)，
缺点是安装以及设置较麻烦，而且个人支持难以长久，未来可能需要自己修改代码。

目前个人使用最朴实的方案，只要书写时稍作注意即可。

Cauchy-Schwarz不等式：
```text
\\[ \left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right) \\]
```

\\[ \left( \sum_{k=1}^n a_k b_k \right)^2 \leq \left( \sum_{k=1}^n a_k^2 \right) \left( \sum_{k=1}^n b_k^2 \right) \\]


### reST

## 测试
毕达哥拉斯定理：`\\(a^2+b^2=c^2\\)`，\\(a^2+b^2=c^2\\)

正态分布：
```text
$$f\left(x\right)=\frac{1}{\sqrt{2\pi}\sigma}exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$
```
$$f\left(x\right)=\frac{1}{\sqrt{2\pi}\sigma}exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)$$

傅里叶变换：
```text
\\[F\left(\omega\right)=\mathcal{F}\left[f(t)\right]=\int_{-\infty}^{\infty}e^{-i\omega T}dt\\]
```
\\[F\left(\omega\right)=\mathcal{F}\left[f(t)\right]=\int_{-\infty}^{\infty}e^{-i\omega T}dt\\]

傅里叶逆变换：
```text
\\[f\left(t\right)=\mathcal{F}^{-1}\left[F\left(\omega\right)\right]=\frac{1}{2\pi}\int_{-\infty}^{\infty}F\left(\omega\right)e^{i\omega t}d\omega\\]
```
\\[f\left(t\right)=\mathcal{F}^{-1}\left[F\left(\omega\right)\right]=\frac{1}{2\pi}\int_{-\infty}^{\infty}F\left(\omega\right)e^{i\omega t}d\omega\\]

MathJax的语法基本与latex一致，可以参考wikipedia的latex书写语法规范[Help:数学公式](http://zh.wikipedia.org/wiki/Help:%E6%95%B0%E5%AD%A6%E5%85%AC%E5%BC%8F)

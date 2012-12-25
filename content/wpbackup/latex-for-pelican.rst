LaTeX for Pelican 测试
############################
:date: 2012-02-18 05:48
:category: IT技术
:tags: LaTeX, 测试
:slug: latex-pelican

本文主要用于测试Pelican与MathJax配合显示数学公式

毕达哥拉斯定理： :math:`a^2+b^2=c^2`

正态分布： :math:`f\left(x\right)=\frac{1}{\sqrt{2\pi}\sigma}exp\left(-\frac{(x-\mu)^2}{2\sigma^2}\right)`

傅里叶变换： :math:`F\left(\omega\right)=\mathcal{F}\left[f(t)\right]=\int_{-\infty}^{\infty}e^{-i\omega
t}dt`

傅里叶逆变换： :math:`f\left(t\right)=\mathcal{F}^{-1}\left[F\left(\omega\right)\right]=\frac{1}{2\pi}\int_{-\infty}^{\infty}F\left(\omega\right)e^{i\omega t}d\omega`

MathJax的语法基本与latex一致，可以参考wikipedia的latex书写语法规范\ `Help:数学公式`_

.. _`Help:数学公式`: http://zh.wikipedia.org/wiki/Help:%E6%95%B0%E5%AD%A6%E5%85%AC%E5%BC%8F

Title: Markdown语法笔记
Date: 2013-03-27 00:22
Author: voidmous
Catogery: none
Tags: markdown
Status: draft

这是我自己学习Markdown语法的一个备忘，主要是一些难以理解或者易错的地方。更详细的可以参考 [Markdown快速入门](http://wowubuntu.com/markdown/basic.html )和 [Markdown语法说明](http://wowubuntu.com/markdown/basic.html ) 


### 基本语法 ###

HTML标签可以直接在md文本中书写，不必区分。某些区块元素标签比如`<table>,<pre>`需要前后空行且开始结尾不能缩进。HTML标签和md语法互相嵌套的情况比较复杂，不过这种需求比较少。

Markdown对`<`和`&`字符的处理比较智能，会自动根据所处的位置做相应的转换，对于作者而言是很自然的，按照习惯书写即可。

Markdown以空行分段且段落不需要手工缩进。

两种标题语法Setext和atx都支持，如何选择合适的标题层次？

区块引用使用`>`，类比gmail的回复引用。

在列表中空行会导致每个项目都被`<p>`标签包起来。

连续的缩进行或者段落会被当作代码块处理，注意前后空行。

链接、图片都有行内和参考两种形式。参考标记可以是数字或者字符甚至空白和标点符号，不区分大小写。参考链接或图片的定义推荐放在引用段落的后面，方便查看。参考式链接的有点在于增强了去除正文的链接内容，使之更具可读性。
 
目前Markdown无法指定图片宽高，需要普通的`<img>`标签。

反斜杠作为逃逸符？





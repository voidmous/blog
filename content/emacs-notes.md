Title: Emacs笔记
Author: voidmous
Date: 2013-04-05 01:17
Category: emacs
Tags: 
Status: draft
Slug: emacs-notes
Summery:

## 安装Emacs24

Github上很多新项目默认支持emacs24,里面许多项目都很有前途，比如el-get，低版本当然也都兼容，不过安装起来不那么方便，因此推荐用最新版本。Debian下可以自行编译，更方便的是用第三方维护的软件源（<http://emacs.naquadah.org/>）。

首先安装APT key：

~~~bash
wget -q -O - http://emacs.naquadah.org/key.gpg | sudo apt-key add -
~~~

添加软件源，把以下代码写入`/etc/apt/sources.list`:

~~~text
deb http://emacs.naquadah.org/ unstable/
deb-src http://emacs.naquadah.org/ unstable/
~~~

现在就可以安装了：

如何重载`.emacs`？

推荐用`M-x load-file`,还有一些其他方式如`M-x eval-buffer`，有什么区别?
参考<http://stackoverflow.com/questions/2580650/how-can-i-reload-emacs-after-changing-it>


## 常用package

### YASnippet

YASnippet是一个模板系统，利用它可以把一个缩写词快速扩展成一句话、一个函数甚至一篇文章，而且扩展的内容支持参数。这么说并不直观，你可以观看 [此视频](http://yasnippet.googlecode.com/files/yasnippet.avi ) 来理解。

项目主页： <https://github.com/capitaomorte/yasnippet>
文档主页： <http://capitaomorte.github.io/yasnippet/>部分内容过时。

yasnippet的snippet加载路径在变量`yas-snippet-dirs`中设置，你可以通过`C-h v RET yas-snippet-dirs RET`来查看说明。如果利用el-get的默认recipe安装那么路径包括`~/.emacs.d/snippets`和`~/.emacs.d/el-get/yasnippet/snippets`。你自定义的snippets可以放到前一个目录下，它会覆盖后一个目录下同名的snippet。

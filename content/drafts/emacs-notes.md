Title: Emacs笔记
Author: voidmous
Date: 2013-04-05 01:17
Category:
Tags:
Status: draft
Slug: emacs-notes
Summery:

## 安装Emacs24

Github上很多新项目默认支持emacs24,里面许多项目都很有前途，比如el-get，低版本当然也都兼容，不过安装起来不那么方便，因此推荐用最新版本。Debian下可以自行编译，更方便的是用第三方维护的软件源（<http://emacs.naquadah.org/>）。首先安装APT key：

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

参考<http://stackoverflow.com/questions/2580650/how-can-

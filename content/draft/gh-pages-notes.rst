============
Gh-pages笔记
============

:date: 2012-12-26 00:38
:slug: gh-pages-note
:author: voidmous
:status: draft
:tag: gh-pages


最佳方案
--------

使用jekyll引擎：
创建username.github.com这个repo，并且把post源代码以及其它附加文件都放在master branch中，这样gh-pages会自动生成相应的静态网页。

不使用jekyll
用一个repo（比如blog）的master branch存放post源文件，该repo的gh-pages branch存放静态博客生成器生成的静态网页。利用ghp-import可以实现gh-pages的分支管理。

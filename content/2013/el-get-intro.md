Title: El-get——emacs包管理利器
Author: voidmous
Date: 2013-04-07 15:38
Category: Technique
Tags: el-get, Emacs
Slug: el-get-intro
Summary:
Status: published

[TOC]

## El-get vs ELPA

Emacs24已经集成了`package.el`，可以安装多个源下的宏包。不过El-get宣称支持多种安装方式，ELPA方法只是其中一种。从我使用的情况来看，el-get似乎速度更快。另外，el-get安装的包不再需要手动`(require 'somepackage)`，它会自动管理所有安装包的加载和初始化，当然配置还是需要的，不过这已经方便不少了。我个人ELPA用得较少，就不比较了，有时间再把两者比较一下。

## 安装el-get

el-get现在处于活跃的开发阶段，因此推荐使用更新维护更活跃的`master branch`，安装只需要把如下命令拷贝到emacs的`*scrach*`buffer，然后`C-j`或者`M-x eval-print-last-exp`运行，el-get就会自动下载安装了。

~~~~.scheme
;; So the idea is that you copy/paste this code into your *scratch* buffer,
;; hit C-j, and you have a working developper edition of el-get.
(url-retrieve
 "https://raw.github.com/dimitri/el-get/master/el-get-install.el"
 (lambda (s)
   (let (el-get-master-branch)
     (goto-char (point-max))
     (eval-print-last-sexp))))
~~~~

安装完毕，如果要手动安装package，可以`M-x el-get-install RET packagename`，喝口茶的功夫估计就好啦。

## 配置el-get

将下列代码加入配置文件，emacs每次启动时就会检查el-get是否已经安装，未安装则自动下载安装。

~~~~.scheme
(add-to-list 'load-path "~/.emacs.d/el-get/el-get")

(unless (require 'el-get nil 'noerror)
  (with-current-buffer
      (url-retrieve-synchronously
       "https://raw.github.com/dimitri/el-get/master/el-get-install.el")
    (let (el-get-master-branch)
      (goto-char (point-max))
      (eval-print-last-sexp))))

(el-get 'sync)
~~~~

想要自动检测并安装需要的宏包，可以使用下面这段代码：

~~~~.scheme
(setq my-el-get-packages
'(
	el-get
	auto-complete
	yasnippet
	auctex
	emacs-w3m
	markdown-mode
	color-theme
	;; Any package you like))

(el-get 'sync my-el-get-packages)
~~~~

## Github同步

如果想要在不同电脑上共享同样的emacs配置，那么你可以选择dropbox或者更开放的github同步。为了便于git的管理，需要把所有配置文件都放到`.emacs.d`目录下，这样只需要`ln -s`把该目录链接到用户主目录即可。如果你使用`.emacs`配置文件，那么可以把它原封不动地迁徙一下即可：`mv .emacs .emacs.d/init.el`。

## 参考文章

[el-get@Github](https://github.com/dimitri/el-get ) 

[Package Management in Emacs: The Good, the Bad and the Ugly](http://batsov.com/articles/2012/02/19/package-management-in-emacs-the-good-the-bad-and-the-ugly/)

[GNU Emacs的终极扩展管理工具 — el-get](http://emacser.com/el-get.htm ) 


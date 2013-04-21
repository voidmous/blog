Title: cygwin安装jekyll
Date: 2012-09-24
Tags: cygwin,jekyll
Category: Technique
Slug: cygwin-install-jekyll

## 卸载已安装的ruby
用对应的包管理器卸载
如果是rvm安装的，直接删除目录`~/.rvm`，然后删除`.zshrc`和`.zlogin`文件，去掉`.profile`和`.bash_profile`中关于rvm的语句即可。

## 安装rvm
[安装指南](https://rvm.io/rvm/install/)

    :::bash
    curl -L https://get.rvm.io | bash -s stable --ruby

检测rvm安装

    :::bash
    type rvm | head -n 1

此时会显示`rvm:not found`，不用紧，还需要一步：

    :::bash
    source ~/.rvm/scripts/rvm
	type rvm | head -n 1

现在显示`rvm is a function`，说明rvm安装成功。
查看是否还有依赖问题：

    :::bash
    rvm requirements

## 管理ruby环境
下面这几步其实不必要了，只是展示一下安装的过程，你也可以安装其它的ruby版本。

    :::bash
    rvm list known
    rvm install 1.9.3
    rvm use 1.9.3 --default

查看安装的版本号和路径

    :::bash
    ruby -v
    gem -v
    which ruby
    which gem

## 安装jekyll
用gem安装：

    :::bash
    gem update --system
    gem list
    gem install jekyll

如果出现`spawn.h`的错误，这是由于`posix-spawn`的bug引起的，需要自己编译安装：
	
    :::bash
    gem install rake-compiler -v 0.7.6
    git clone git://github.com/rtomayko/posix-spawn.git
    cd posix-spawn
    rake gem
    gem install pkg/posix-spawn-0.3.6

再`gem install jekyll`就没问题啦。

## 参考页面
[Windows,Cygwin and Jekyll](http://matt.scharley.me/2012/03/10/windows-cygwin-and-jekyll.html)

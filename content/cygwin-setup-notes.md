Title: Cygwin安装设置笔记
Date: 2013-03-25 23:12
Tags: cygwin,
Category: Technique
Slug: cygwin-setup-notes
Author: voidmous
Status: draft
Summary: Installation notes for cygwin.

[TOC]

## 基本Cygwin系统安装

下载最新的[setup.exe](http://cygwin.com/setup.exe )运行之。

选择安装目录，推荐D:\cygwin（路径中最好不要带空格，cygwin是绿色的，重装后仍然可以使用，需要[配置用户](http://hi.baidu.com/hawk_kt/item/2d2e2f6faeb470167cdecc73 )）,注意选择一个较快的源。

安装完成后将setup.exe放到cygwin目录下，以后要安装什么可能还会用到。

在cygwin下创建一个packages子目录，用于存放下载下来的安装包（可选，apt-cyg和setup.exe的下载目录不同）

安装默认基本包,注意额外安装subversion和wget，为安装apt-cyg做准备。Xorg什么的先不用装，可用性不高，需要了再装上不迟。

## 安装编译环境

cygwin自带的安装工具使用起来太繁琐，于是就有了类似apt-get的包管理器[apt-cyg](https://code.google.com/p/apt-cyg/ apt-cyg google code)，实乃广大cygwin玩家的福音。安装apt-cyg:

    :::bash
    $ svn --force export http://apt-cyg.googlecode.com/svn/trunk/ /bin/
    $ chmod+x /bin/apt-cyg
    $ apt-cyg --help
    $ apt-cyg -m mirrorurl  % 设置apt-cyg使用的镜像地址
	
安装一些必备的工具：

    :::sh
    apt-cyg install openssl openssh
    apt-cyg install git mercurial % 源代码管理工具
    git config --global user.name "Your Name Comes Here"
    git config --global user.email you@yourdomain.example.com

安装binutils、gcc4、gdb、make以及vim

~~~.bash
apt-cyg install binutils gcc4 gdb make vim
~~~

查看安装是否成功

~~~.bash
gcc -v
gdb -v
make -v
~~~

## 基本设置

### bash设置

编辑~/.bashrc，加入以下内容(根据自己的喜好配置)：

~~~.bash
alias ls='ls --color=auto'
PS1="\[\e[32m\]\u:\[\e[33m\]\w\[\e[0m\]\$ "
LANG=en_US.UTF-8
~~~

### vim设置

~~~.vimrc
"Cygwin相关设置
set backspace=indent,eol,start
~~~

### mintty设置

在终端标题栏右键选择“Options”就可以设置mintty的显示效果，主要修改几个方面：
字体，推荐[Inconsolata](http://levien.com/type/myfonts/inconsolata.html )或者其它的[编程字体](http://www.lowing.org/fonts/ )，这些字体保证可以清晰地区别0和“o”。
终端窗口大小，按照屏幕大小自己调整。
透明度，high级别在win7下看着比较舒服。
如果想恢复默认设置，只需要清空~/.minttyrc中的内容。
mintty快捷键：
shift+insert 粘贴
alt+Enter 全屏
深蓝色难以阅读的问题：

~~~.bash
echo 'Blue=127,127,255' >> ~/.minttyrc
echo 'BoldBlue=191,191,255' >> ~/.minttyrc
~~~

## 安装其它工具

[cyg-hotkey](http://riverslee.com/project/cyg-hotkey/ )使mintty变成一个类似tilda的呼叫式终端，默认用快捷键F7来调出和隐藏mintty，使用起来还是很顺手的。

~~~.bash
hg clone https://bitbucket.org/riverscn/cyg-hotkey
cd cyg-hotkey
make all
make install
~~~

将cyg-hotkey的快捷方式放到开始菜单的启动目录里，让它开机自动启动。如果要更换快捷键，可以修改源码重新编译。

安装python easy_install：

~~~.bash
wget http://peak.telecommunity.com/dist/ez_setup.py
python ez_setup.py
~~~

推荐安装pip，具体见[这里](http://stackoverflow.com/questions/3220404/why-use-pip-over-easy-install)

```bash
$ curl -O https://raw.github.com/pypa/pip/master/contrib/get-pip.py
$ [sudo] python get-pip.py
$ pip install Markdown
```

## 其它有用工具

util-linux(more)，bash-completion，procps(top)，inetutils(telnet)

cygcheck

## 常见问题

### [Rebase](http://cygwin.wikia.com/wiki/Rebaseall ) 

在更新或者安装了某些包以后，如果出现问题，可能需要rebase来解决。

### cygcheck

如果apt-cyg安装过程中断，再安装时会发生与dll相关的错误，这时可以用cygcheck命令追踪问题

## Cygwin/X配置

我个人用cygwin/X主要是想用emacs的GUI，此外小程序的GUI也会用到，但是cygwin/X目前虽然可以调出windows的输入法却无法输入中文，目前可用的方案也许只有[这个](http://cn.bbs.comp.linux.narkive.com/JrQG9Hge/cygwin-x )（未测试）。

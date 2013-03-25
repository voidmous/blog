Title: Cygwin安装设置笔记
Date: 2013-03-25 23:12
Tags: cygwin,
Category: uncategoriezed
Slug: cygwin-setup-notes
Author: voidmous
Summary: Installation notes for cygwin.

## 基本Cygwin系统安装

下载最新的[setup.exe](http://cygwin.com/setup.exe )

选择安装目录，推荐D:\cygwin（路径中最好不要带空格，cygwin是绿色的？）

将setup.exe放到该目录下（推荐），以后要安装什么可能还会用到。

创建一个packages子目录，用于存放下载下来的安装包（可选，用apt-cyg的话和setup.exe貌似不用同一个目录）

安装默认基本包,注意额外安装subversion和wget，为安装apt-cyg做准备。X什么的先不用装，可用性不高，需要了再装上不迟。

## 安装编译环境

安装apt-cyg(cygwin下的类似apt-get包管理工具):

```bash
svn --force export http://apt-cyg.googlecode.com/svn/trunk/ /bin/
chmod+x /bin/apt-cyg
apt-cyg --help
apt-cyg -m mirrorurl  % 设置apt-cyg使用的镜像地址
apt-cyg install openssl
apt-cyg install git mercurial % 源代码管理工具
git config --global user.name "Your Name Comes Here"
git config --global user.email you@yourdomain.example.com
```

安装binutils、gcc4、gdb、make以及vim
```bash
apt-cyg install binutils gcc4 gdb make vim
```
查看安装是否成功
```bash
gcc -v
gdb -v
make -v
```

## 基本设置
bash设置：
编辑~/.bashrc，加入以下内容：
```bash
alias ls='ls --color=auto'
PS1="\[\e[32m\]\u:\[\e[33m\]\w\[\e[0m\]\$ "
LANG=en_US.UTF-8
```
vimrc设置：

```bash
"开启语法高亮
syntax on
"依文件类型设置自动缩进
filetype indent plugin on
"显示当前的行号列号：
set ruler
"在状态栏显示正在输入的命令
set showcmd
"关闭/打开配对括号高亮 有问题？？？
"NoMatchParen
"DoMatchParen
"为深色背景调整配色
set background=dark
"显示行号：
set number
"为方便复制，用<F2>开启/关闭行号显示:
nnoremap <F2> :set nonumber!<CR>:set foldcolumn=0<CR>
"""""""""""""""""""""""""""""""""""
"Python相关配置
" 自动检测文件类型并加载相应的设置
filetype plugin indent on
autocmd FileType python setlocal et sta sw=4 sts=4
"""""""""""""""""""""""""""""""""""
"Cygwin相关设置
set backspace=indent,eol,start
```
安装openssh：
```
apt-cyg install openssh
```

mintty设置
在终端标题栏右键选择“Options”就可以设置mintty的显示效果，主要修改几个方面：
字体，推荐[Inconsolata](http://levien.com/type/myfonts/inconsolata.html )或者其它的[编程字体](http://www.lowing.org/fonts/ )，这些字体保证可以清晰地区别0和“o”。
终端窗口大小，按照屏幕大小自己调整。
透明度，high级别在win7下看着比较舒服。
如果想恢复默认设置，只需要清空~/.minttyrc中的内容。
mintty快捷键：
shift+insert 粘贴
alt+Enter 全屏
深蓝色难以阅读的问题：
```bash
echo 'Blue=127,127,255' >> ~/.minttyrc
echo 'BoldBlue=191,191,255' >> ~/.minttyrc
```

## 安装其它工具

编译安装[cyg-hotkey](http://riverslee.com/project/cyg-hotkey/ ) 
cyg-hotkey用以呼出cygwin默认的mintty终端，实现类似linux下的tilda下拉终端功能，使用起来还是很顺手的。默认快捷键为F7。
```bash
hg clone https://bitbucket.org/riverscn/cyg-hotkey
cd cyg-hotkey
make all
make install
```
以后就可以用安装目录下的cyg-hotkey来调出终端。

安装git
可能需要rebase

安装python easy_install：
```bash
wget http://peak.telecommunity.com/dist/ez_setup.py
python ez_setup.py
```
安装python-markdown：
```bash
easy_install ElementTree
easy_install Markdown
```

## 其它有用工具

util-linux(more)，bash-completion，procps(top)，inetutils(telnet)

cygcheck

Title: Cygwin 安装配置笔记
Author: Joshz
Date: 2014-12-02
Modified:
Category: Technique
Tags: Cygwin
Slug: cygwin-cfg-note

[TOC]

# 安装

Cygwin 的安装过程并不难，但还是比较繁琐，如果你想快速拥有一个配置好的 Cygwin 环境或者仅仅想试用一下，那我推荐使用 [Babun](https://babun.github.io/ )，它是一个基于 Cygwin 的 Shell 环境，自带包管理工具`pact`（基于`apt-cyg`），预装了众多工具以及自定义配置。对于想长期使用的童靴，我还是推荐官方原配。

## 基本系统

下载 [setup-x86.exe](http://cygwin.com/setup-x86.exe)  或者 [setup-x86_64.exe](https://cygwin.com/setup-x86_64.exe )  丢到安装目录`D:\cygwin`（建议）下。它是默认的图形包管理器，双击运行，设置包下载目录为`D:\cygwin\packages`。推荐的国内源地址：

```
; 网易
http://mirrors.163.com/cygwin/
; 中科大
http://mirrors.ustc.edu.cn/cygwin/
; 搜狐
http://mirrors.sohu.com/cygwin/
```

安装时注意选上`subversion`和`wget`，为安装`apt-cyg`做准备。

## 安装第三方包管理工具
`cygwin`自带的图形包管理器需要重复一些配置操作，而且需要搜索包名安装，实在是不方便。[`apt-cyg`](http://code.google.com/p/apt-cyg/ )（或者[cyg-apt](http://code.google.com/p/cyg-apt/ )）则提供了类似`debian`下`apt-get`相同的功能，非常方便包管理，强烈推荐安装。首先用默认包管理器安装好`subversion`和`wget`，启动`Cygwin Terminal`，输入如下命令：

```bash
$ svn --force export http://apt-cyg.googlecode.com/svn/trunk/ /bin/
$ chmod+x /bin/apt-cyg
$ apt-cyg -m http://mirrors.163.com/cygwin/  # 设置apt-cyg的源地址
```
```text
apt-cyg: Installs and removes Cygwin packages.
  "apt-cyg install <package names>" to install packages
  "apt-cyg remove <package names>" to remove packages
  "apt-cyg update" to update setup.ini
  "apt-cyg show" to show installed packages
  "apt-cyg find <patterns>" to find packages matching patterns
  "apt-cyg describe <patterns>" to describe packages matching patterns
  "apt-cyg packageof <commands or files>" to locate parent packages
Options:
  --mirror, -m <url> : set mirror
  --cache, -c <dir>  : set cache
  --file, -f <file>  : read package names from file
  --noupdate, -u     : don't update setup.ini from mirror
  --help
  --version
```

一些必备的软件：git、openssh、openssl、binutils，
有用的工具：util-linux(more)、bash-completion（经测试可能影响终端启动性能）、procps(top)、inetutils(telnet)、bind-utils(dig)。

## 安装编译环境

随着 Cygwin 的更新，目前越来越多的软件可以在 Cygwin 下通过编译，但是比起 Linux 系统，出问题的概率仍然较高，而且有些编译和运行的需求是 Cygwin 平台无法满足的。因此普通用户应当优先使用二进制包，在最不利的情况下才应该尝试自己编译软件。
```bash
$ apt-get install gcc4-core gcc4-g++ gdb make autoconf automake
$ gcc --version
$ g++ --version
```

# 配置

## 配置 Bash

鉴于 Cygwin 下大部分的配置都和 Linux 相同，因此，为了免除维护两份配置文件的麻烦，可以在`~/.bashrc`中写入：
```bash
if [[ "$OSTYPE" == "linux-gnu" ]]; then
    echo "Linux-gnu environment detected."
elif [[ "$OSTYPE" == "cygwin" ]]; then
    echo "Cygwin environment detected."
    if [ -f "${HOME}/.bashrc.cygwin" ]; then
        source "${HOME}/.bashrc.cygwin"
    fi
else
    echo "Unknown Platform"
fi
```
这样所有 cygwin 下特定的配置都可以写入到 `~/.bashrc.cygwin` 了。

## 配置 mintty
在终端标题栏右键选择“Options”就可以设置mintty的显示效果，主要修改几个方面：

* 字体，我个人喜欢 [Inconsolata](http://levien.com/type/myfonts/inconsolata.html )，或者你可以从[这里](http://www.lowing.org/fonts/  )挑一个。
* 终端窗口大小，可按照屏幕大小自己调整。
* 透明度，medium 级别在 win7 下看着比较舒服。

Mintty 默认设置下深蓝色不够显眼，看着很吃力，我建议大家使用 [mintty-color-schemes](https://github.com/oumu/mintty-color-schemes )  的主题，我个人最偏爱对比度较高的`base16-shapeshifter-mod-lighten`。

如果想恢复默认设置，只需要清空`~/.minttyrc`中的内容。

我的`~/.minttyrc`：

```bash
BoldAsFont=no
Font=Monaco
FontHeight=10
Transparency=medium
CursorType=block
CursorBlinks=no
Scrollbar=right
Columns=120
Rows=26
BackspaceSendsBS=yes
Locale=zh_CN
Charset=UTF-8
 
# base16-shapeshifter-mod-lighten theme
# from: https://github.com/oumu/mintty-color-schemes
ForegroundColour=171,171,171
BackgroundColour=0,0,0
CursorColour=253,157,79
Black=0,0,0
BoldBlack=52,52,52
Red=233,47,47
BoldRed=240,116,116
Green=14,216,57
BoldGreen=64,243,102
Yellow=221,221,19
BoldYellow=240,240,78
Blue=59,72,227
BoldBlue=125,135,236
Magenta=249,150,226
BoldMagenta=253,222,246
Cyan=35,237,218
BoldCyan=107,243,230
White=171,171,171
BoldWhite=249,249,249
```
更多配置请参考`man mintty`。

### 下拉式 mintty
mintty本身并非下拉式终端，即不能通过热键来呼出或隐藏，参考了网友所写的 [cyg-hotkey](https://bitbucket.org/riverscn/cyg-hotkey/ )，我用`AHK`写了个小工具 [PUF](https://github.com/voidmous/PUF/tree/ahk-devel )，可以实现任意窗口程序的热键呼出。如果要使用 cyg-hotkey，可运行下列命令：
```bash
$ hg clone https://bitbucket.org/riverscn/cyg-hotkey   # 需安装mercurial
$ cd cyg-hotkey
$ make all && make install
```
cyg-hotkey 默认使用快捷键 F7，运行`cyg-hotkey.exe`后即可使用 F7 来呼出/隐藏 mintty 窗口。
 
### mintty的常用快捷键
* Shift+Insert    粘贴
* Alt+Enter       全屏
* Alt+F2           开启一个新 mintty 终端
* Ctrl+Tab        在不同终端间切换

### mintty 运行 DOS 命令乱码问题
虽然 cygwin 已经提供了很完备的命令行工具，但涉及到 Windows 配置的个别命令仍然需要到 cmd.exe 下运行（比如`ipconfig`，`taskkill`，`set`等），能不能让这些命令也在`mintty`下运行呢？答案是肯定的，可以运行，但是并不完美，中文系统运行会出现乱码。原因就在于 cmd.exe 默认的`Code Page`为`cp 936 ANSI/OEM 简体中文 936`（在 cmd.exe 窗口右键——属性——选项中可查看），而我们默认设置的 cygwin 编码为 UTF-8，于是 DOS 命令输出的中文一概会变成方框。可选的解决方案有以下几种：

* 改变 cmd.exe 的默认输出编码。通过修改注册表更改系统默认设置，见 [How to make Unicode charset in cmd.exe by default?](https://stackoverflow.com/questions/14109024/how-to-make-unicode-charset-in-cmd-exe-by-default )。此方法非常危险，会导致系统无法启动，请不要轻易尝试。
* 改变 cygwin 和 mintty 的编码。将 cygwin 的 locale 全部改成 zh_CN.GBK，mintty 的 CharSet 也设置为 GBK 即可。但是在大部分软件都以 UTF-8 作为默认输入和输出编码的环境下，这样做会干扰许多软件，比如此时 Vim 中文显示就全是乱码，因此此方案也不推荐。
* [临时改变 cmd.exe 的输出编码](https://cygwin.com/faq-nochunks.html#faq.using.weirdchars)。在`bash.rc`中添加`cmd /c chcp 65001`，这样就可以让 mintty 执行 DOS 命令时输出 UTF 编码。不过让人蛋疼的是，`cmd.exe`本身如果变成 UTF-8 输出（运行`chcp 65001`可临时改变输出编码，见 [Unicode characters in Windows command line - how?](https://stackoverflow.com/questions/388490/unicode-characters-in-windows-command-line-how/388500#388500 )）时，不仅提示全变为英文，且不再支持中文目录（具体原因不详）。幸好在 mintty 下，中文目录没有问题，只是只有英文提示参考，算是变相地解决了乱码的问题。

## 替换 mintty

虽然 mintty 也还不错，但也有其自身的限制（详细信息可参考其 Manual），从我使用的过程来看，`ConEmu`是不错的替代者。

* [Upgrade Cygwin to Console2 and Improve Windows Productivity](https://blog.openshift.com/upgrade-cygwin-to-console2-and-improve-the-productivity-of-openshifts-rhc-client-tools-on-wind/ )，本人测试不成功，UI有问题
* [How do I configure ConEmu to run Cygwin Bash?](https://superuser.com/questions/591206/how-do-i-configure-conemu-to-run-cygwin-bash)，测试成功，界面不错，功能也很多，但`tmux`无法运行。
* [Windows下的各类 Command Prompt](http://alternativeto.net/software/conemu/ )

## 配置 Vim

Cygwin 下运行 Vim 必要的配置，加入到`~/.vimrc`：

```vim
"Cygwin相关设置
set nocompatible
set backspace=indent,eol,start
```

## 使用 Emacs

Emacs 是神器，但不是普通人能玩得转的，偶尔拿来写点文字还不错，做为 IDE 的话门槛太高，我们作为普通用户还是不要跳这个坑了。关于 Emacs 和 Cygwin 配合使用
的讨论有很多，比如 [How to best integrate Emacs and Cygwin?](https://stackoverflow.com/questions/2075504/how-to-best-integrate-emacs-and-cygwin )，其中比较实用的方案如下：

* 文字终端 Emacs，输入`apt-cyg install emacs`即可安装，没有图形界面，适合高级 Emacs 用户。
* Emacs-X11，输入`apt-cyg install emacs-X11`安装，启动时需要`XServer`，由于 Cygwin/X 本身的局限（见下文），不推荐此方案。
* Emacs-w32，输入`apt-cyg install emacs-w32`安装，其实它使用的是 Windows GUI，我个人最推荐的方式。
* 让外部 Emacs 识别 Cygwin shell。在 Windows 下安装 Emacs，然后让 Emacs 启动时自动识别 Cygwin shell，需要编写复杂的设置脚本，门槛较高。

Mintty 有一个很好用的特性：在 mintty 中后台运行的非终端程序在 mintty 进程结束后仍然可以继续运行。比如输入`emacs-w32.exe 1>/dev/null 2>/dev/null &`启动 Emacs，然后输入`exit`关闭 mintty，此时 Emacs 不会随之关闭，对于 Emacs 常驻党应该很有帮助。


# Cygwin/X

## 安装
```bash
$ apt-cyg install xorg-server xinit xorg-docs
# xorg-server 是 windows 下的 Xserver， xinit 包括各种启动命令如 xinit,startx,startwin
# xorg-docs 可选
```

## 中文支持
Cygwin/X 的一个问题是没有对中文输入法的支持，虽然可以安装`fcitx`并在 Cygwin/X 中运行（我测试未成功），但只能在单窗口模式下启动。
官方早有支持IME-XIM转换的想法，却迟迟没出成果（见 [Development - To-Do List](http://x.cygwin.com/devel/todo.html )）。总之，现阶段在 Cygwin/X 下输入
中文是很蛋疼的事情，因此它对我们而言还只能是一个玩物。

# 技巧

## 文件共享
Cygwin 让人爱不释手的原因之一就是和 Windows 的无缝文件共享：Cygwin可以直接访问Windows下的所有文件，Windows也可以访问 Cygwin 下的文本文件。
Windows 下的盘符`C:\`对应为 Cygwin 下的目录`/cygdrive/c/`，所有的 Cygwin 工具可以直接对该目录操作。另外，Windows 下路径名如`C:\Program Files\`，
cygwin下的路径则形如`/etc/rc.d/`，因此两者之间需要进行转换。Cygwin 提供了命令行工具[`cygpath`](http://www.cygwin.com/cygwin-ug-net/using-utils.html#cygpath )来进行 Windows 风格和 POSIX 风格的路径名互转。

## 剪贴板共享
Cygwin 下操作剪贴板最方便的方式是访问设备`/dev/clipboard`，比如：

```bash
$ diff file1 file2 > /dev/clipboard
$ cat < /dev/clipboard
```
第一条命令`diff`得到的结果被发送到剪贴板上，直接粘贴即可。

## 搜索软件包

常用的软件我们用`apt-cyg find packagename`一般都可以找到，但是以下两种情况此命令却帮不上什么忙：

1. 某些命令行工具被集成到一个大包里，比如`dig.exe`，`telnet.exe`
2. 编译软件时常见的`libXXX.so.X`找不到的问题

这时我们可以上 [Cygwin package list](http://cygwin.com/packages/) 更精确地查找，注意打开链接查看是否包含需要的文件。或者也可以使用内置命令`cygcheck -p dig.exe`(需要网络连接，[说明](http://www.cygwin.com/cygwin-ug-net/using-utils.html#cygcheck ))，利用此方法一般都可以确定需要下载的包，更加快捷。

## 打开当前目录
此代码来自博客 [Pragmatistic Guy](http://oldratlee.com/post/2012-12-22/stunning-cygwin)，特此致谢。

`xpl`加参数可用于打开目录或者文件，默认无参数打开当前目录：

```bash
#!/bin/bash
 
cygwin=false;
case "`uname`" in
    CYGWIN*) cygwin=true ;;
esac
 
if [ "$1" = "" ]; then
    XPATH=. # 缺省是当前目录
else
    XPATH=$1
    if $cygwin; then
        XPATH="$(cygpath -C ANSI -w "$XPATH")";
    fi
fi
 
explorer $XPATH
```

也可写入到`.bashrc.cygwin`中，修改如下：

```bash
function xpl {
     if [ "$1" = "" ]; then
         XPATH=.   # 缺省是当前目录
     else
         XPATH=$1
         XPATH="$(cygpath -C ANSI -w "$XPATH")";
     fi
     explorer $XPATH
 }
```

`xpf`用于 explorer 跳转到指定目录或文件并选中：
```bash
#!/bin/bash
 
cygwin=false;
case "`uname`" in
    CYGWIN*) cygwin=true ;;
esac
 
if [ "$1" = "" ]; then
    XPATH=. # 缺省是当前目录
else
    XPATH=$1
    if $cygwin; then
        XPATH="$(cygpath -C ANSI -w "$XPATH")";
    fi
fi
 
explorer '/select,' $XPATH
```

使用说明，以`xpl`为例：

```bash
$ xpl # explorer打开当前目录
$ xpl /usr/bin/  # explorer打开指定目录
$ xpl video.avi  # 使用 Windows 默认程序打开文件
```

## 隐藏启动终端

有时我们想在 Windows 下启动 Cygwin 中的程序或命令行，比如`D:\cygwin\bin\mintty.exe /usr/bin/emacs-w32.exe`可以启动 Emacs-w32，
但是同时也会启动一个碍事的终端窗口，如何隐藏它呢？我们可以使用官方提供的工具`run.exe`：
```dos
D:\cygwin\bin\run.exe /usr/bin/emacs-w32.exe
```

# 参考资料
* [惊艳的cygwin——Windows下的Linux命令行环境的配置和使用](http://oldratlee.com/post/2012-12-22/stunning-cygwin  )
* [为Windows创建一个下拉式类Unix终端 - 川叶 :: 时间河](https://bitbucket.org/riverscn/cyg-hotkey/overview  )
* [Cygwin User's Guide](http://cygwin.com/cygwin-ug-net.html  )
* [Cygwin/X User's Guide](http://x.cygwin.com/docs/ug/ )
* [官方推荐技巧](https://code.google.com/p/mintty/wiki/Tips  )

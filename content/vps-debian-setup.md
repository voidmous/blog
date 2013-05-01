Title: VPS Debian 系统设置
Date: 2013-04-28 23:04
Author: voidmous
Category: Technique
Tags: VPS, Debian,
Lang: cn
Slug: vps-debian-setup
Summary: 
Status: draft

## 修改源

* 备份原来的`/etc/apt/sources.list`
* 使用在线的 [Debian Sources List Generator](http://debgen.simplylinux.ch/ ) 生成合适的sources.list，当然也可以手工编辑
* `apitude update`

我现在使用的源列表：

```
deb http://ftp.us.debian.org/debian stable main #contrib non-free
deb http://security.debian.org/ squeeze/updates main #contrib non-free
```

## 安装编译环境

```
# aptitude install build-essential automake autoconf
```

## 用户管理

添加新账户new，用于ssh登陆与管理。

```
# groupadd new
# useradd -m -g new -s /bin/bash new
# passwd new
```

以后可以使用`su root`为普通账户提权，或者用`visudo`为用户添加sudo权限。

## SSH配置

一般服务器已经默认安装好了opensshd，所以只需要修改配置文件。为了安全，一般修改两个设置，一是默认端口，二是禁止root登陆（注意先添加好普通账户）。修改默认端口后登录时要指定新端口。

```
# vi /etc/ssh/sshd_config
# service ssh restart
```

两处设置分别为`Port 2222`和`PermitRootLogin no`。

### SSH密钥登录

参考 [SSH密钥登录让Linux VPS/服务器更安全](http://www.vpser.net/security/linux-ssh-authorized-keys-login.html ) 

## 更新python

服务器系统往往软件比较老，python可能是2.5或2.6版的，有强迫症的孩子可以手动更新到新版本。

## 安装lnmp

参考 <lnmp.org>













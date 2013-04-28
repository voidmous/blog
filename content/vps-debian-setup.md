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

## 安装编译环境

```
$ aptitude install build-essential automake autoconf
```

## 更新python

服务器系统往往软件比较老，python可能是2.5或2.6版的，有强迫症的孩子可以手动更新到新版本。

## 安装lnmp

参考<lnmp.org>













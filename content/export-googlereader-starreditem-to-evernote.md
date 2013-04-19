Title: 导出Google Reader加星条目到Evernote
Date: 2013-04-18 19:13
Author: voidmous
Category: Internet
Tags: Google Reader, Evernote
Lang: cn
Slug: export-googlereader-starreditem-to-evernote
Summary: 总结了导出GR加星标条目的方案，推荐了export2enex.py脚本
Status: published

Google Reader即将离我们而去，这个决定目前看来没有挽回的可能。我个人对Google的服务也很依赖，Google Reader更是常驻在书签栏，不过与其把力气花在谴责Google的作为，不如寻找更好的替代品和抓紧时间备份积累的订阅源和文章。目前离7月1日尚早，其它在线阅读器还有很长的时间打磨产品，所以替代品的筛选还不急于一时。倒是收藏的文章（加星标的条目）怎么导出似乎没有引起大家的关注，我把自己搜索整理的一些导出方案记录下来并作个比较，虽然没有一一测试，希望我的判断能有些参考价值。

## 导出方案思路 ##

目前网上可以搜集到的方案有这么几种：

* [Google Reader的条目转发](http://blog.vsharing.com/ligongzi/A1472320.html)。手工转发当然是很蛋疼的，配合ifttt转发对已经加上星标的又没作用，需要更自动化的工具。
* [基于html页面脚本或AHK脚本](http://m.blog.csdn.net/blog/chief1985/6689805)。这种方法大多是用脚本刷新页面直接打印为PDF，显然处理过程不怎么“漂亮”，而且输出也丢失了扩展性。
* 基于第三方服务。目前似乎只有[为知](http://blog.wiz.cn/google-reader.html)可以方便快捷地下载加星标的文章，但程序好像也不怎么给力。feedly貌似也可以直接导入加星标条目。
* [RSS](http://www.36kr.com/p/201886.html )导出。这种方式貌似可以导出订阅源的所有条目，即便该博客已经不存在了。。。这种方法适合导出一个订阅源的所有文章，但缺点还是自动化程度太低。
* 基于GoogleTakeout的导出数据。虽然关闭了Reader，但是Google对用户还是尽到了自己的责任，提供了一个强大而完备的备份工具，只不过导出的是比较另类的`.json`文件。对它们做进一步处理可以得到组织良好的html文件。
 1. [GR2Evernote — 将Google Reader的分享内容导入Evernote](http://mescoda.com/2011/12/gr2evernote/ ) ，[导出和备份google阅读器喜欢星标评论等历史内容到evernote或者wiz](http://blog.sina.com.cn/s/blog_4afc0d8201017ah3.html ) （未测试）
 2. [ConvertJSON – 转换 Google Reader 导出数据为网页](http://www.appinn.com/convertjson/ ) （未测试）

我个人更喜欢最后一种思路，因为Google提供的备份文件组织良好，而且保留了重要的由用户操作过的文档数据（加星、分享等）而非全部备份文档数据，这使得导出的数据不会很大同时保留住了精华。这里我要推荐一个python脚本`export_gr2evernote`，它的作用是处理`json`文件得到Evernote自家的笔记本格式`.enex`（也可以得到html格式），这样就可以导入到Evernote中，而Evernote虽小，似乎比Google要有良心一些^-^。

## export_gr2evernote ##

[@Github](https://github.com/kerchen/export_gr2evernote )

目前该项目仍然处在改进中，现在已经有了三种导入处理方式：

* `export2HTMLFiles`，每篇文章都输出为单独的html文件。
* `export2enex`，导出为`enex`文件，所有转换都在本地完成，对`json`文件大小无限制。
* `export_gr2evernote`，利用邮件发送功能导入Evernote，脚本不会进行任何的格式优化，所以在Evernote中显示的效果可能很丑陋，不推荐。

作者本人推荐用前两种方式之一。从我个人测试的情况来看，导入的`enex`笔记完全保存了GR中文章的样式，图片、视频都能正常显示和观看，最重要的是整个流程十分简单快捷。

处理流程（以Windows下`export2enex`为例）：

* 首先确保系统安装了python
* 用GoogleTakeout导出Reader数据，下载压缩包解压。
* 将脚本丢到解压目录，`Win+r cmd <RET>`运行Dos窗口， `cd`到该目录，运行`export2enex.py starred.json > starred.enex`，很快目录下就会出现`starred.enex`
* Evernote导入`starred.enex`文件，注意选择**本地笔记本**，尤其是文章数很多的情况。

`export2enex.py`这个脚本有个小bug，就是对文章的链接url中的`&`字符处理不当（应该转换为`&amp;`的形式），导致导出的`enex`文件无法被正确导入到Evernote，需要加入如下代码到合适位置：

~~~~.python
if '&' in msg_url:
    msg_url=msg_url.replace('&', '&amp;')
~~~~







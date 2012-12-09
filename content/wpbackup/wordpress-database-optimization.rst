wordpress数据库优化记录
#######################
:date: 2012-08-30 20:02
:category: IT技术
:tags: WordPress, 优化, 数据库

前段时间发现备份的数据库大小日渐庞大，对一个几乎长草的博客而言实在很诡异，所以抽空进行了一次后台大扫除。这里把基本的流程记录下来，供对数据库操作没有经验的朋友参考。

基本流程如下：

1、备份。做任何数据库操作前，做一个临时备份都是必要的。使用phpmyadmin按默认设置导出sql文件下载到本地即可。

2、删除不必要的插件。不必要的插件应当越少越好，尤其是会写入数据库或者查询数据库的插件。比如我之前使用过的\ `statpresscn`_\ ，这个插件会在数据库中建立一个庞大的wp\_statpresscn表，虽然没有前台查询，不过它造成的数据库冗余带来的坏处可远远大于统计功能带来的便利，所以还是删了吧。

3、删除垃圾数据表。功能比较复杂的插件可能会在数据库中建立新表，删除插件一般不会把这些表顺带删除，所以手动排查垃圾数据表也是必要的。为了防止误删，请一定对照WP
Codex的\ `数据库描述`_\ 进行修改。

删除akismet垃圾数据。关于akismet如何产生这些数据可以参考\ `wp\_commentmeta是否正在拖慢你的blog`_\ 。

.. code-block:: sql

   delete from wp_commentmeta where meta_key='akismet_as_submitted' or meta_key='akismet_history' or meta_key='akismet_rechecking' or meta_key='akismet_result' or meta_key='akismet_user' or meta_key='akismet_user_result

wp\_options数据表清理。主要有两部分垃圾数据：其一、已删除的插件选项。大部分插件都不提供完全的删除功能，主要就是针对数据表而言。由于不清楚数据和插件的对应关系，最好不要盲目删除，如果一定要清理，可以尝试用\ `clean
options`_\ 插件，注意备份！其二、没用的RSS Feed
Cache。以“\_transient”开头的数据都是因为用了RSS小工具产生的，作用不大，体积却不小。可以用下面的SQL语句删除：

.. code-block:: sql

   DELETE FROM wp_options WHERE option_name REGEXP "_transient_

4、优化数据表。最后还要利用phpmyadmin执行优化数据表，体积还会有所减小。

.. _statpresscn: http://www.6psp.cn/20100917/statpresscn%E6%8F%92%E4%BB%B6%E9%80%A0%E6%88%90%E5%8D%9A%E5%AE%A2%E9%80%9F%E5%BA%A6%E5%8F%98%E6%85%A2%EF%BC%8C%E8%B5%B6%E5%BF%AB%E5%88%A0%E9%99%A4.html
.. _数据库描述: http://codex.wordpress.org/zh-cn:%E6%95%B0%E6%8D%AE%E5%BA%93%E6%8F%8F%E8%BF%B0
.. _wp\_commentmeta是否正在拖慢你的blog: http://www.solagirl.net/wp-commentmeta-slowing-down-your-blog.html
.. _clean options: http://www.mittineague.com/dev/co.php

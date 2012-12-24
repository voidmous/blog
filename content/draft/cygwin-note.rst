==============
CYGWIN使用笔记
==============
:Author: voidmous
:Time: 2012-12-24-20:28
:Status: draft
:Tags: cygwin

* 用户主目录被篡改

这种情况一般发生在安装heroku bundle类似的软件时，此时用户的系统变量HOME被修改了，可以改回自己想要的目录，然后执行：

.. code:: bash

  mkpasswd -l -d -p $(cygpath -H)  > /etc/passwd
  mkgroup -l -d > /etc/group 

参考网页：
http://stackoverflow.com/questions/1494658/how-can-i-change-my-cygwin-home-folder-after-installation
http://cygwin.com/faq/faq-nochunks.html#faq.setup.home

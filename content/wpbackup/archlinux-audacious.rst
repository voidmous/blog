Archlinux下编译Audacious(cue、ape支持)
######################################
:date: 2012-03-20 16:25
:category: IT技术
:tags: Archlinux, audacious, 编译

- 首先安装需求：

Glib 2, GTK+ 2, Pango, Cairo, libmcs(AUR), libmowgli(AUR)

- 为了支持cue，还需要安装libcue 

- 下载audacious源码包与插件包： `下载地址`_

- 解压audacious源码包，然后常规三步曲

.. code-block:: bash

  $ ./configure
  $ sudo make && make install

- 再解压audacious插件源码包

此时直接configure会出错，错误提示：

::

   checking for AUDACIOUS... no
   configure: error: Cannot find Audacious 3.2; have you installed Audacious yet?

根据google到的方法： 

.. code-block:: bash

   export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig:$PKG_CONFIG_PATH 
   export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH

后续问题：
ape不支持，dts不支持

.. _下载地址: http://audacious-media-player.org/download

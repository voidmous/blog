============
Pelican简介
============

:author: voidmous
:date: 2012-12-25 11:18
:category: Programming
:tags: pelican
:status: draft
:slug: pelican-intro

Pelican是什么
-------------

Pelican是一个静态博客生成器，



安装Pelican
-----------

推荐在Linux或者Cygwin下使用Pelican，首先保证系统安装有python和 `pip <http://www.pip-installer.org>`_ 。官方文档推荐在virtualenv下安装Pelican，不过如果你没有用python开发的需求或者和我一样嫌麻烦，也可以直接安装：

.. code:: bash

   $ pip install pelican
   $ pip install Markdown


编辑文章
--------

常用元数据：

.. code:: text

   :title:
   :author:
   :date:
   :category:
   :tags:
   :slug: use this to specify url
   :summary: Short summary 
   :status: draft/hidden/published



代码高亮：

pelican使用pygments来处理代码高亮

* reST格式高亮

reST格式可以采用`code-block`原语，编辑时注意前后空行以及缩进与必要的空格（python在这方面很严格）

.. code-block:: rest

    .. code-block:: identifier

       <indented code block goes here>

输出的html代码为：

.. code-block:: html

    <div class="highlight"><pre><span class="p">..</span> <span class="ow">code-block</span><span class="p">::</span> identifier

       &lt;indented code block goes here&gt;
    </pre></div>

注意这里CSS类是`highlight`。

* Markdown高亮

Markdown需要经过python-markdown处理，并且需要codehilite扩展的支持，示例如下：

方案一：

.. code-block:: markdown

    Some text.

        :::python
	def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

输出的html代码为：

.. code-block:: html

    <p>Some text.</p>
    <div class="codehilite"><pre>
    </pre></div>

方案二：

.. code-block:: markdown

    Some text.

    ```python
    def factorial(n):
    if n == 0:
	return 1
    else:
	return n * factorial(n - 1)
    ```

两种方案输出的CSS类都是`codehilite`而不是`highlight`，另外第一种方案必须缩进，第二种则不必。

常见问题
--------

* 如何改变post链接地址？

* 如何快速同步到gh-pages?

首先安装ghp-import

.. code-block:: bash

   pip install ghp-import

Pelican自带的Makefile已经添加了ghp-import支持，只需要执行以下命令即可：

.. code:: bash

  make html
  make github

参考资源
--------


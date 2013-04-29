:title: Pelican简介
:author: voidmous
:date: 2012-12-25 11:18
:category: Programming
:tags: pelican,
:status: draft
:slug: pelican-intro

.. contents::
   :depth: 2

Pelican是什么
-------------

Pelican是一个静态博客生成器，具有常见博客系统如WordPress的基本功能，在功能、速度、开放性上更符合Geek们的口味。

静态博客的优点：

* No-SQL。原始文章再也不是数据库表中的一个值，而是实实在在可以用任意编辑器编辑的纯文本文件，撰写、修改文章都不再依赖专门工具。
* 源文件支持多种标记语言（与转换引擎相关），简化文章编辑。
* 速度快。不再需要查询数据库，直接读取静态html，因此速度飞快。
* 本地（同步）备份网站，网站迁移部署更灵活。

静态博客的缺点：

* 评论依赖外部服务。依赖第三方评论系统。
* 修改设置，修改、发表文章大部分情况下需要编译整个网站。
* 通常依赖命令行工具，具有一定技术门槛。

Pelican的功能与特点：

* 基于python环境，如Jinja2、pygments
* 标记语言支持：reStructuredText、Markdown、AsciiDoc，支持自定义
* 命令行操作
* 主题/插件自定义
* 文章可发布多种语言版本
* Atom/RSS订阅
* 多种常用第三方服务集成：Github、Disqus、Google Analytics、Twitter

安装Pelican
-----------

推荐在Linux或者Cygwin下使用Pelican，首先保证系统安装有python和 `pip <http://www.pip-installer.org>`_ 。官方文档推荐在virtualenv下安装Pelican，不过如果你没有用python开发的需求或者和我一样嫌麻烦，也可以直接安装：

.. code:: bash

   $ pip install pelican
   $ pip install Markdown

启动博客
--------

首先创建一个博客目录用于存放所有的文件，比如 :code:`~/pelicanblog` ，然后执行 :code:`pelican-quickstart` 回答几个基本的问题，执行完毕在目录下就生成了基础的文件和目录如下：

* content/，默认posts文档（\*.rst \*.md \*.html等等）存放目录
* output/，默认静态网站编译输出目录，把该目录下文件拷贝到任意开启HTTPServer的目录下并绑定好设置的域名即可访问。
* Makefile，pelican使用make进行基本操作，请仔细阅读该文件，了解常用的make选项。
* pelicanconf.py，pelican配置文件
* publishconf.py，发布博客的配置文件，由make调用，可以自行设置
* develop_server.sh，测试pelican的脚本，由make调用，一般不需修改

常用的make选项：

* make html，用pelican生成静态网页
* make remove，删除输出目录的文件
* make serve，用 :code:`python -m SimpleHTTPServer` 在输出目录运行HTTP服务，可以从 :code:`localhost:8000` 访问。
* make regenerate，自动检测文件更新并重新生成html
* make devserver，运行HTTP服务并检测文件更新，一旦更新就重新生成html
* make publish，发布静态网站
* make github，发布到 :code:`gh-pages`


编辑文章
--------

Meta-data
---------

常用元数据(reST)：

.. code:: text

   :title: the post title
   :author: author of the post
   :date: publishing date/time, e.g. 2013-04-14 21:00
   :category: life/programming
   :tags: blog, tag
   :slug: use this to specify url of post, i.e. slug.html
   :summary: Short summary, displayed as a short description of post at index.html
   :status: draft/hidden/published

处于draft状态的文章也会被转换为html但是会输出到 :code:`outputdir/drafts/` 而且不会出现在输出的任何页面中。当然你自己仍然可以通过地址 :code:`http://domainname.com/drafts/slug.html` 来访问。

Markdown也采用同样的元数据，不过形式为 :code:`Title: title` 。


代码高亮
^^^^^^^^

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

内链
^^^^


基本设置
--------

绝对链接
^^^^^^^^


使用主题
^^^^^^^^

下载网友分享的自定义主题：

.. code-block:: bash

   $ git clone https://github.com/getpelican/pelican-themes BLOGDIR/themes

在 :code:`pelicanconf.py` 中添加 :code:`THEME = "./themes/THEMENAME`
      

从其它博客导入
--------------

多语言
------



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


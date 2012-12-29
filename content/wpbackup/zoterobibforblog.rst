利用Zotero为博文添加参考文献
############################
:date: 2012-06-29 19:15
:category: 科研学术
:tags: style, Zotero, 博文, 参考文献, 源码
:slug: zotero-bib-blog

对于技术类文章而言，添加必要的参考文献体现的是对他人劳动成果的尊重。即便你不会全文转载别人的文章而不标明出处，但是严格的说，学习了别人的方法或者观点也不能据为己有，标注参考文献就是向原创致敬的方法之一。目前而言，许多加了参考文献的文章都是怎么简单怎么来，没有个统一的格式，也不方便读者查阅。其实规范并不是没有，许多学术期刊对引用网页这样的媒体都有说明，我国\ `参考文献标准`_\ 也有说明。从我较短的使用过程来看，GB/T 7714-2005标准设计得比较简洁紧凑，适合中文、英文以及混排的情况，看上去比较舒服。

收集、管理文献的工具我首推Zotero，主要就在于它和Firefox结合得很好，对国际国内各大学术期刊数据库都支持得不错，和Google
Scholar搭配堪称完美。关于Zotero的使用可以看这篇文章：《\ `文献管理软件Zotero的一点使用感受`_\ 》。

利用Zotero的导出功能实际已经可以生成很好的参考文献了，不过美中不足的是导出的只是纯文本，没有任何格式化，所以读者仍然要自己手动去查找参考文献，这可不是我这样的懒人想干的事，于是干脆自己动手写了下面这个style，基本功能已经实现，在外观和功能上可能还有提升的空间。

Blogit是我基于\ `Chinese Std GB/T 7714-2005
(numeric)`_\ 这个style文件，参考\ `radiopaedia`_\ 鼓捣出来的一个结合体。一方面保留了国标的规范，同时加上了源网页和DOI（\ `hdx.doi.org`_\ ）或者ISBN（\ `www.worldcat.org`_\ ）的超链接，方便在网页上直接跳转查看，不用复制粘贴再搜索这么麻烦了。利用此style配合Zotero导出的代码包含超链接，可以直接粘贴到文章源代码上。

Blogit源代码：\ `Blogit20120627`_

Zotero的style文件为\ `CSL`_\ 格式，其实质为xml，所以自己看看就可以摸到些门道。Windows下直接用Notepad++即可编辑，不推荐直接用记事本编辑，因为CSL是Unix文本格式，所以用记事本查看会没有换行。编辑过程中可以直接在Firefox标签页\ `chrome://zotero/content/tools/cslpreview.xul`_\ 中预览，当前选中的文献在所有可用的style作用下生成的参考文献代码都可以看到，方便比较和进一步修改。修改编辑后一定要用\ `验证工具`_\ 验证是否有错，推荐用在线的\ `csl-validator.js`_\ 。验证无误后即可用Zotero导入该style，如果已经导入那么覆盖原有文件即可。

几点说明：

1、一般来说，源网页和DOI、ISBN指向的网页很可能是同一个，所以如果你嫌太多超链接很难看，那么也可以去除源网页的链接，只要在Zotero设置Citation
Option里去掉Include URLs of paper articles in references前面的钩即可。

2、Chinese Std GB/T 7714-2005 (numeric)
sytle文件的一个小问题：如果插入多篇文献时上标顺序是从大到小而不是标准的从小到大，那么应该把citation-number这个宏中的sort
从descending改为ascending。 

参考文献示例： 

[1] 陈永春编. `MATLAB
M语言高级编程`_\ [M]. 清华大学出版社, 2004. `ISBN: 9787302075141`_. 

[2]
`Matlab自定义函数的五种方法`_\ [EB/OL]. [2012-06-27]. 

[3] Shampine L F,
Thompson S. `Solving DDEs in Matlab`_\ [J]. Applied Numerical
Mathematics, 2001, 37(4): 441–458. `doi:10.1016/S0168-9274(00)00055-6`_.

[4] L.F. Shampine, S. Thompson. `Solving Delay Differential Equations
with dde23`_\ [J]. . 

[5] 陈丽安. `输出高品质 MATLAB
图形的方法与技巧`_\ [J]. 计算机应用研究, 2002, 19(1): 154–155.

.. _参考文献标准: http://gradschool.ustc.edu.cn/ylb/material/xw/wdxz/19.pdf
.. _文献管理软件Zotero的一点使用感受: http://blog.yesmryang.net/zotero-usage/
.. _Chinese Std GB/T 7714-2005 (numeric): http://www.zotero.org/styles/chinese-gb7714-2005-numeric
.. _radiopaedia: http://www.zotero.org/styles/radiopaedia
.. _hdx.doi.org: http://dx.doi.org/
.. _www.worldcat.org: http://www.worldcat.org/wcpa/isbn/
.. _Blogit20120627: ./img/Blogit20120627.rar
.. _CSL: http://citationstyles.org/
.. _`chrome://zotero/content/tools/cslpreview.xul`: chrome://zotero/content/tools/cslpreview.xul
.. _验证工具: https://github.com/citation-style-language/styles/wiki/Validation
.. _csl-validator.js: http://simonster.github.com/csl-validator.js/
.. _MATLAB M语言高级编程: http://book.douban.com/subject/1151443/
.. _`ISBN: 9787302075141`: http://www.worldcat.org/wcpa/isbn/9787302075141
.. _Matlab自定义函数的五种方法: http://www.360doc.com/content/11/0301/09/4539198_97069216.shtml
.. _Solving DDEs in Matlab: http://www.sciencedirect.com/science/article/pii/S0168927400000556
.. _`doi:10.1016/S0168-9274(00)00055-6`: http://dx.doi.org/10.1016/S0168-9274(00)00055-6
.. _Solving Delay Differential Equations with dde23: http://scholar.google.com/scholar?hl=zh-CN&q=Solving+Delay+Differential+Equations+with+dde23&btnG=%E6%90%9C%E7%B4%A2&lr=&as_ylo=&as_vis=0
.. _输出高品质 MATLAB 图形的方法与技巧: http://202.204.193.237/cupbbs/accessory/93/cb00d031-6df1-417b-a9e0-71c1aabff823.pdf

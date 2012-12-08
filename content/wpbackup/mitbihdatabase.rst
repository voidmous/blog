MIT-BIH开放数据库使用指南
################
:date: 2012-06-15 21:14
:category: 科研学术
:tags: Matlab, MIT-BIH, PhysioBank, WFDB, 入门, 心电, 指南, 数据库

最近因为项目任务要分析心电图数据，采用的是\ `MIT-BIH`_\ 开放数据库（或称PhysioBank数据库）。这个数据库不仅提供了经过筛选的各方面的生理数据集\ `PhysioBank`_\ ，而且也提供了开源的数据处理和可视化工具\ `PhysioToolkit`_\ 。对我这样的非医学类学生而言，光是看见那些医学术语就够头痛的了，还要掌握这样一套专门的基于Linux的工具，确实是个不小的挑战。好在我要完成的部分不需要很深入，所以马马虎虎也摸着些门道。不敢说会用，但是起码碰到问题方向在哪我已经清楚了，这里把这个数据库的使用简单介绍一下，方便新来的同学快速上手。当然如果你英语好的话，大可以自己慢慢翻文档，这也是要深入了解的惟一途径。
首先说说数据库。你可以到\ `分类页面`_\ 查找有没有自己感兴趣的数据集，上面都有比较详细的介绍。找到合适的数据后在对应页面直接将文件另存为就可以下载，当然这是比较笨的办法。推荐使用wget或者rsync来下载。wget可以用于下载单独的数据集，这样速度较快也比较快捷。例如下载mitdb：
[bash]wget -r -np http://physionet.org/physiobank/database/mitdb/[/bash]
中间的\ *physionet.org*\ 可以替换成离你最近的\ `镜像`_\ 地址（好像西交的挂了，直接用原镜像吧），\ *mitdb*\ 替换成你要下载的数据集缩写名称（可以用\ `PhysioBank
ATM`_\ 查看数据集对应缩写）。rsync用来下载所有数据也是非常方便的，方法看\ `这里`_\ ，当然这样做似乎没多大必要。
对应这套数据集维护人员也开发了相应的工具包\ `WFDB`_,包括三个部分：WFDB库、WFDB命令行工具和WAVE，主要用于读取、分析和可视化数据，一些常用的算法如FFT和熵都已经实现。WFDB库用于在C、C++或者Fortran中读写WFDB兼容格式文件，命令行用于直接处理数据，WAVE可以看做其图形化前端，需要xview支持。软件应该是C语言编写，Linux原生支持，Windows需要Cygwin支持，安装文档都写得很详细了。这套工具很强大，同时也很复杂，文档在\ `这里`_\ ，当然需要你对命令行和研究对象都比较熟悉。如果要快速找到自己需要的命令或工具，可以看看这个\ `工具目录`_\ ，很有帮助。
如果没有那么高的要求或者不想碰命令行，那么它提供的\ `MATLAB软件包`_\ 还是可以一用，不过功能就差点意思了，只能做基本的数据I/O，后续的算法都要自己实现，只能将就着用。这个页面除了官方发布的工具其实还有一些第三方编写的程序实现附加的功能，因为都是开源的，所以可以一看，对自己动手的朋友会有帮助。
这套数据库确实组织得非常好，甚至还开发了在线数据导出工具。如果你被前面各种软件名词吓到，那么下面这个东东估计就是你所需要的：\ `PhysioBank
ATM`_\ ，它的作用就是用浏览器可视化地预览或者导出数据，如图示，左边选择数据设置参数，右边微调选择输出模式。利用它，你就可以远离那些繁琐工具的困扰，点几下鼠标就可以方便地查看数据，然后将理想的数据段导出即可。这个方法适合新手使用，直观、快速才不会拒人于千里之外，哈哈。

.. figure:: http://i1078.photobucket.com/albums/w482/voidmous/blog/Science/20120615201304.png
   :align: center
   :alt: PhysioBank ATM

   PhysioBank ATM
如果你使用了该数据库，并且准备要发文章，那么出于版权考虑，应当注意按照网站的要求进行引用，引用格式见\ `这里`_\ 。另外如果某些地方有特别注明，那么也应该按照要求进行引用。因为这个数据库有很强的研究背景，所以有许多论文基于该数据库发表，不妨看看\ `他人的成果`_\ 。

如果你在使用过程中还有什么问题，那么我推荐你先看\ `FAQ`_\ ，大部分问题在这都能找到答案，此外还有一些\ `教程`_\ ，涉及到方方面面，也可以看看。

关于该数据库中文的论文还是比较少，但不是没有，参考文献已经注明。网络上讨论的也不多，但这两篇文章不可不看：《\ `MIT-BIH
ECG 心电数据的下载和读取图解`_\ 》、《\ `MIT-BIH ECG
信号的数据读取方法和Matlab程序`_\ 》，对于文件数据格式有较详细的分析。

**参考文献**

[1] 唐文涛. MIT-BIH 生理信号管理及回放系统[D]. 济南: 山东师范大学, 2009.
[2] 宋喜国, 邓亲恺. MIT-BIH 心率失常数据库的识读及应用[J].
中国医学物理学杂志, 2004, 21(004): 230–232. [3] 徐效文, 曾超, 崔松野, et
al. `MIT-BIH数据库心电数据重采样研究`_\ [J]. 计算机工程与应用, , 47(8):
245–248. [4] 朱泽煌, 胡广书.
`MIT—BIH心电数据库的开发及用作检测标准`_\ [J]. 中国生物医学工程学报,
1993, 12(4): 244–249. [5] 张乾, 蒋式勤. PhysioBank 数据库及其应用[J].
中国生物医学工程进展——2007 中国生物医学工程联合学术年会论文集 (下册),
2007. [6] Goldberger A L, Amaral L A N, Glass L, et al. `PhysioBank,
PhysioToolkit, and PhysioNet: Components of a New Research Resource for
Complex Physiologic Signals`_\ [J]. Circulation, 2000, 101(23):
e215–e220. `doi:10.1161/01.CIR.101.23.e215`_. [7] 张玉霞. 基于 MATLAB 与
WFDB 的 PhysioBank 数据库读取[J]. 北京生物医学工程, 2011, 30(3):
318–320. [8] 梁伯虎, 张楠, 苏晓东.
`基于Matlab的MIT-BIH心电信号读取与波形显示的实现`_\ [J]. 中国电子商务,
(11): 113–113. [9] 宋春丽. `怎样识读MIT-BIH中的心电信号`_\ [J].
科技资讯, (9): 27–27.

.. raw:: html

   </p>

.. _MIT-BIH: http://ecg.mit.edu/
.. _PhysioBank: http://www.physionet.org/physiobank/
.. _PhysioToolkit: http://www.physionet.org/physiotools/
.. _分类页面: http://www.physionet.org/physiobank/database/
.. _镜像: http://www.physionet.org/mirrors/
.. _PhysioBank ATM: http://www.physionet.org/cgi-bin/atm/ATM
.. _这里: http://www.physionet.org/faq.shtml#downloading-databases
.. _WFDB: http://www.physionet.org/physiotools/wfdb.shtml
.. _这里: http://www.physionet.org/physiotools/manuals.shtml
.. _工具目录: http://www.physionet.org/physiotools/software-index.shtml
.. _MATLAB软件包: http://www.physionet.org/physiotools/matlab/
.. _PhysioBank ATM: http://www.physionet.org/cgi-bin/atm/ATM
.. _这里: http://www.physionet.org/citations.shtml
.. _他人的成果: http://physionet.org/pn-citations.shtml
.. _FAQ: http://www.physionet.org/faq.shtml
.. _教程: http://physionet.org/tutorials/
.. _MIT-BIH ECG 心电数据的下载和读取图解: http://blog.csdn.net/chenyusiyuan/article/details/2027887
.. _MIT-BIH ECG 信号的数据读取方法和Matlab程序: http://blog.csdn.net/chenyusiyuan/article/details/2040234
.. _MIT-BIH数据库心电数据重采样研究: http://www.cqvip.com/qk/91690x/201108/36940878.html
.. _MIT—BIH心电数据库的开发及用作检测标准: http://www.cqvip.com/qk/90680x/1993004/1245724.html
.. _`PhysioBank, PhysioToolkit, and PhysioNet: Components of a New Research Resource for Complex Physiologic Signals`: http://circ.ahajournals.org/content/101/23/e215
.. _`doi:10.1161/01.CIR.101.23.e215`: http://dx.doi.org/10.1161/01.CIR.101.23.e215
.. _基于Matlab的MIT-BIH心电信号读取与波形显示的实现: http://www.cqvip.com/qk/81625x/201111/39687170.html
.. _怎样识读MIT-BIH中的心电信号: http://www.cqvip.com/Main/Detail.aspx?id=33712105

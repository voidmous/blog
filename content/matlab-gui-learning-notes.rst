:title: Matlab GUI学习笔记
:date: 2013-04-15 19:47
:author: voidmous
:category: programming
:tags: matlab, gui 
:lang: cn
:slug: matlab-gui-learning-notes
:summary: 
:status: draft


基础知识
----------

* 常见的GUI组件包括菜单、工具条、按钮、列表和滑动条等等。
* 多数组件需要用户发出控制信号，然后才执行相应的命令，这个动作称为 :code:`callback` 。
* 常见的触发动作包括：按下按钮、按下鼠标按键、选择菜单项、输入数值或字符串、鼠标滑过组件上方等等。
* GUI程序为事件驱动型， :code:`callback` 函数的执行是异步的（外部信号触发）。
* 两种方式构建GUI程序：
  1. GUIDE(GUI开发环境)，一个交互式（图形的）构建工具。特点是会生成互相耦合的两个文件，其中fig文件储存大部分属性，m文件储存 :code:`callback` 和其它函数。优点是不需要手工指定大量的属性，容易上手。
  2. 基于代码文本的方式。只有一个m文件储存所有信息，fig文件运行时实时生成。
* 两种方式可以在一定程度上结合起来：先用GUIDE搭建图形框架，再修改属性和函数。

Learning by examples
--------------------

下面的内容是matlab GUI教程 `41 Complete GUI Examples <http://www.mathworks.com/matlabcentral/fileexchange/24861-41-complete-gui-examples>`_ 的学习笔记。

GUI1
----

:code:`figure` 命令创建一个空白窗口，:code:`uicontrol` 创建一个控件，并由 :code:`style` 属性控制控件类型。代码示例：

.. code-block:: matlab

   S.fh = figure('units','pixels',...
		'position',[500 500 200 260],...
		'menubar','none',...
		'name','GUI_1',...
		'numbertitle','off',...
		'resize','off');

   S.ls = uicontrol('style','list',...
		'unit','pix',...
                'position',[10 60 180 180],...
                'min',0,'max',2,...
                'fontsize',14,...
                'string',{'one';'two';'three';'four'});  

窗口或控件位置与大小由 :code:`position` 控制，例如： :code:`'position',[500 500 200 260]` ，其中前两个数控制窗口或空间的左下角坐标，后两个控制其大小。窗口位置总是相对于屏幕左下角计算的，而控件则相对窗口左下角计算。 控件的动作触发的函数由 :code:`callback` 属性定义，例如：:code:`'callback',{@pb_call,S}` 。

问题
^^^^

* 界面控件的数据结构是怎么组织的？
* varargin的用法
* :code:`get` 和 :code:`set` 的用法


GUI2
----





==================
Matlab GUI学习笔记
==================

:date: 2013-04-15 19:47
:author: voidmous
:category: programming
:tags: matlab, gui 
:lang: cn
:slug: matlab-gui-learning-notes
:summary: 
:status: draft

本文是matlab GUI教程 `41 Complete GUI Examples <http://www.mathworks.com/matlabcentral/fileexchange/24861-41-complete-gui-examples>`_ 的学习笔记。

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





用MATLAB分析Henon映射
#####################
:date: 2012-07-09 18:24
:category: 科研学术
:tags: Henon, Matlab, 分岔, 吸引子, 映射, 混沌

Henon映射是动力系统研究中很常见的离散映射，因为它具有的混沌特性而闻名。映射方程如下：

:math:`\left\{\begin{array}~x_{n+1}=y_n+1-a\times x_n^2 \\y_{n+1}=bx_n \\ \end{array} \right\`

不同的a、b参数下该映射具有不同的性质，可能出现混沌、断续或者收敛到周期轨道上不同的情况。取a=1.4，b=0.3时会产生著名的henon吸引子。

.. image:: http://img.voidmous.net/2012/07/henon1.png

Henon吸引子，横轴为x，纵轴为y，其实就是所有迭代的点产生的图案，形状比较怪异。

.. image:: http://img.voidmous.net/2012/07/henon2.png

b=0.3时的分岔图，不同a值下x可能在几个值间变化，也可能在许多值之间变化，即产生了混沌。顺便吐槽下Matlab生成的图片太不精细了，暂时还不知道用什么方法能提高图片细节。

Matlab源代码：

.. code-block:: matlab

   % By voidmous<voidmous@gmail.com> 
   % Henon map analysis 
   clear all;close all;clc 
   N=10000; 
   x=zeros(1,N); 
   y=zeros(1,N); 
   x(1)=0; 
   y(1)=0;
   a=1.4;b=0.3; 
   for i=2:N 
      x(i)=y(i-1)+1-a*x(i-1)^2; 
      y(i)=b*x(i-1); 
   end
   figure(1) 
   scatter(x,y,2) 
   xlabel('x');ylabel('y') 
   title('Henon Attractor') 
   figure(2) 
   L=round(0.97*N); 
   for a=1.0:0.001:1.5 
      for i=2:N
         x(i)=y(i-1)+1-a*x(i-1)^2; 
         y(i)=b*x(i-1); 
      end
      scatter(a*ones(1,N-L),x(1,L+1:N),2,'black','filled'); 
      hold on 
   end
   title('bifurcation for a') 
   xlabel('a') 
   ylabel('x')

参考文献

[1]Wikipedia contributors. `Hénon map`_\ [J]. Wikipedia, the free
encyclopedia, Wikimedia Foundation, Inc., 2012.

.. _Hénon map: http://en.wikipedia.org/w/index.php?title=H%C3%A9non_map&oldid=474794740

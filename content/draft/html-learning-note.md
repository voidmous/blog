Title: HTML learning note
Date: 2013-03-27 21:53
Category:Programming
Tags:HTML, CSS
Status: draft

## 基本html语法

### 代码结构

一个简单的html框架：

```html
<!DOCTYPE html>
<html>

	<head>
		<title>
		title
		</title>
		
	</head>
    <body>
        <p>par1</p>
        <p>par2</p>
    </body>

</html>
```

### 标签

有序列表(Ordered List)：

```html
<ol>
    <li>person 1</li>
    <li>person 2</li>
    <li>Matt Damon</li>
</ol>
```

无序列表标签是ul(Unordered List)。

注释代码：

```html
<!-- This is an example of comment -->
```

### 标签属性

`a`标签中的`href`或`img`标签中的`src`都是属性，一般形式可以这么写：

```html
<label attr="">content</label>
```

一些标签效果：

    :::html
    <p style = "color:red; font-size:20px; font-family:Garamond">some text</p>

输出:
<p style = "color:red; font-size:20px; font-family:Garamond">some text</p>

其它还有`background-color`,`text-align`


### 表格

`table`,`tr`,`td`,`thead`,`tbody`,`th`
`div`(Short for division)用于进行网页的块设置。
`span`用于改变某部分文字的属性。

## Cascading Style Sheets

为什么要将内容和表现分离？
* 对多个元素赋予同样的表现形式
* 对多个HTML文件用一个CSS文件统一格式化

CSS的插入方法：
1. 用`style`标签（放在`head`标签内）
2. 独立文件，并在`head`标签内加入：

    :::html
    <link type="text/css" rel="stylesheet" href="stylesheet.css" />

CSS三要素：`selector`,`property`,`value`

    :::css
    p {
        color: red;
    }

CSS注释：

    :::css
    /* This is an example comment */

任何html标签都可以成为CSS选择器！

选择器的种类：
* html元素选择器，支持嵌套和直连
* 通用（全局？universal）选择器
* 类选择器
* ID选择器

多重选择器：

如果html元素有嵌套，要选择内部元素就需要多重选择器。

全局选择器`*`

一个形象的比喻：
html文档就像一棵大树，`html`标签是树干，`head`和`body`是其上的两支，而`title`又是`head`的分支。每一个标签都是包围它的其它标签的*子孙*。

直连选择器：
用`>`选择两个直接嵌套的html元素，两者中间不能嵌套其它元素，比如这个示例：

```css
div > p {
    color: #7AC5CD;
}
```

选择器优先级

越特别的嵌套式选择器（通常更长）具有越高的优先级，它会覆盖已有的低优先级的选择器指定的属性。比嵌套式选择器更特殊的是类选择器和ID选择器。

### 类选择器

定义类

```css
<div class="square"></div>
<img class="square"/>
<td class="square"></td>
```

CSS指定类属性

```css
.square {
    height: 100px;
    width: 100px;
}
```

### ID选择器

用于对一个特别的元素指定不同的样式。

定义ID

```
<div id="first"></div>
<div id="second"></div>
<p id="intro"></p>
```

指定类属性

```
#first {
    height: 50px;
}

#second {
    height: 100px;
}

#intro {
    color: #FF0000;
}
```

### 伪类选择器Pseudo-Class

一个常见的应用是修改点击前和点击后以及鼠标悬停时超链接的不同样式，比如：

```css
a:hover {
	color: #cc0000;
	font-weight: bold;
	text-decoration: none;
}
```

链接的三个伪类选择器分别是`a:link`,`a:visited`,`a:hover`。

其它常用的伪类选择器还有`first-child`，`nth-child`。`first-child`表示它是“其父标签下的第一个子标签”，而不是“同类标签下的第一个”的意思，注意区分。`nth-child`含义类似，用法如下：

```css
p:nth-child(4) {
    font-size: 26px;
}
```
表示其父标签下第四个为`<p>`的子标签。

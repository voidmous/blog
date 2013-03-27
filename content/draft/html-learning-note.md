Title: HTML learning note
Date: 2013-03-27
Category:
Tags:
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

    :::html
    <!-- This is an example of comment -->

### 标签属性

`a`标签中的`href`或`img`标签中的`src`都是属性，一般形式可以这么写：

    :::html
    <label attr="">content</label>

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

    :::html
    p {
        color: red;
    }

CSS注释：

    :::html
    /* This is an example comment */



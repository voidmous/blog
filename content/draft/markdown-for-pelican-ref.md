Title: Markdown syntax for Pelican Quick Reference
Author: voidmous
Date: 2013-03-29 22:13
Category:
Tags: markdown, pelican
Slug: markdown-for-pelican-ref

[TOC]

This post is a simple markdown syntax reference for Pelican(the static blog generator that builds this blog), especially coupled with some features from Python-Markdown.

## Basic Syntax

### Headings

* `Setext` style:

## Extra Features

Default features supported by Python-Markdown, i.e. `extra` and `codehilite` extension function. Consult [here](http://pythonhosted.org/Markdown/ ) for more details. If you want to add more features, you should change the setting `MD_EXTENSIONS (['codehilite','extra'])`.

### Abbreviations

### Attribute Lists

### Definition Lists

	:::markdown
	Apple
	:   Pomaceous fruit of plants of the genus Malus in 
		the family Rosaceae.

	Orange
	:   The fruit of an evergreen tree of the genus Citrus.

Apple
:   Pomaceous fruit of plants of the genus Malus in 
    the family Rosaceae.

Orange
:   The fruit of an evergreen tree of the genus Citrus.

### Fenced Code Blocks

	:::html
	~~~~~~~~~~~~~~~~~~~~
	def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)
	~~~~~~~~~~~~~~~~~~~~


Output:

~~~~~~~~~~~~~~~~~~~~
def factorial(n):
if n == 0:
	return 1
else:
	return n * factorial(n - 1)
~~~~~~~~~~~~~~~~~~~~


	~~~~{.python}
	def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)
	~~~~


Output:

~~~~{.python}
def factorial(n):
if n == 0:
	return 1
else:
	return n * factorial(n - 1)
~~~~

	~~~~.html
	<p style="color: red">HTML Document</p>
	~~~~

Output:

~~~~.html
<p style="color: red">HTML Document</p>
~~~~

Github's tilde syntax:

	```python
	def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)
	```

Output:

```python
def factorial(n):
if n == 0:
	return 1
else:
	return n * factorial(n - 1)
```

### Footnotes

```html
Footnotes[^1] have a label[^label] and a definition[^!DEF].

[^1]: This is a footnote.
    Paragraph two of the definition.

    > A blockquote with
    > multiple lines.

        a code block

    A final paragraph.
    
[^label]: A footnote on "label"
[^!DEF]: The definition of a footnote.
```

Footnotes[^1] have a label[^label] and a definition[^!DEF].

[^1]: This is a footnote.
    Paragraph two of the definition.

    > A blockquote with
    > multiple lines.

        a code block

    A final paragraph.
    
[^label]: A footnote on "label"
[^!DEF]: The definition of a footnote.

### Tables

```html
First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell
```

First Header  | Second Header
------------- | -------------
Content Cell  | Content Cell
Content Cell  | Content Cell

### CodeHilite


### Metadata for post

	:::markdown
	Title: Blog Title
	Date: 2010-12-03 10:20
	Tags: thats, awesome
	Category: yeah
	Slug: my-super-post
	Author: authorname
	Summary: Short version for index and feeds
	Status: draft

	This is the content of my super blog post.

The slug metadata 

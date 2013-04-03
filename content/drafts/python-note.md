Title: Python笔记
Author: voidmous
Date: 2013-03-29 19:39
Category: 
Tags: python
Status: draft
Slug: python-note

* 优先级： `not`\> `and` \> `or`

* python没有switch，全部用if代替。

* PEP：Python Enhancement Proposals. PEP 20, "The Zen of Python". Try `import this` in the console!

* 三种导入module的方式：

```python
import math
print math.sqrt(25)
```

```python
from math import sqrt
print sqrt(25)
```

```python
from math import *
print sqrt(25)
```

比较三种的优劣，在不同情况下选择不同方式，第一种当然是最安全但最不方便的。

查看module内所有的函数：

```python
import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!
```


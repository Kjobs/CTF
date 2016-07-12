PHP - Local File Inclusion  
-------
---PHP本地文件包含漏洞

这里有篇介绍:-[PHP文件包含漏洞总结](http://drops.wooyun.org/tips/3827)

这是题目给出的php代码提示
```php
$filename = 'pages/'.(isset($_GET["file"])?$_GET["file"]:"welcome").'.html';
include $filename;
```

在乌云那篇文章中提到：有限制的文件包含
```php
<?php include("inc/" . $_GET['file'] . ".htm"); ?> 
```
可采用%00截断处理，获得.php文件，但有限制：  
* php版本小于5.3.4  
* php的magic_quotes_gpc为OFF状态  

不过对本题没有影响，题目给出php代码已经说明。


另一提示：  
There is a lot of important stuff in ../solution.php, so please include and execute this file for us.  
链接显示为lfi目录下的solution.php链接，但不能直接查看得到。所以得用文件包含得到信息，输入file参数解答题目：  
http://www.wechall.net/challenge/training/php/lfi/up/index.php?file=../../solution.php%00

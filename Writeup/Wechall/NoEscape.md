No Escape (Exploit, PHP, MySQL)
------
题目名没搞懂，就是一个投票，需要投到111票，但题目说投到100票的时候会重置。去按了几下（好像没啥用），  
但是在地址栏可以看到输入参数要求，这里有个vote_for=可以让我们得到一些帮助；  

题目给出了php源码，其中有一个函数；  
```php
function noesc_voteup($who)
{
        if ( (stripos($who, 'id') !== false) || (strpos($who, '/') !== false) ) {
                echo GWF_HTML::error('No Escape', 'Please do not mess with the id. It would break the challenge for others', false);
                return;
        }
 
        $db = noesc_db();
        $who = mysql_real_escape_string($who);
        $query = "UPDATE noescvotes SET `$who`=`$who`+1 WHERE id=1";
        if (false !== $db->queryWrite($query)) {
                echo GWF_HTML::message('No Escape', 'Vote counted for '.GWF_HTML::display($who), false);
        }
        
        noesc_stop100();
}
```  
根据代码可以看到，输入的参数who，用[mysql_real_escape_string()](http://www.php.net/mysql_real_escape_string)对很多字符串进行了转义,
也就是对输入进行了过滤，但是下一行出现的`字符却没有被过滤，于是得到启发，可在这里入手。这条语句给$who加1，说明$who就是用来计票数，
直接给某个人赋上111的票数应该就可以了！  

结合刚才的vote_for可以构造注入语句$who`=111，然后把后面的注释掉，把某个人的票数改成111就OK。这里的mysql注释需要注意一下（好吧，
作为小白的我在这里跌了跟头），我试了一下，这里用"#"注释好像不行，于是就换成"--",结果发现还是不行，真是奇（ri）了怪（gou）了！后来
才知道，mysql用"--"注释还需要加一个空格，即"-- "。照此输入，还是不行（崩溃！！！）。想到可能是空格被过滤了，于是把空格换成"%20",
成功！  

注入语句：http://www.wechall.net/challenge/no_escape/index.php?vote_for=bill`=111--%20

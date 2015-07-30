<?php
define ('HOSTNAME', 'localhost'); //数据库主机名
define ('USERNAME', 'root'); //数据库用户名
define ('PASSWORD', 'raspicn.com'); //数据库用户登录密码
define ('DATABASE_NAME', 'typecho'); //需要查询的数据库
$db = mysql_connect(HOSTNAME, USERNAME, PASSWORD) or
         die (mysql_error());
//连接不上，就会显示mysql出错的原因。
mysql_select_db(DATABASE_NAME);
$query =
"SELECT name,mail FROM typecho_users";
//上面这句的意思是从testdb中随机提取一条数据。
$result = mysql_query($query);
//以上执行查询
$row=mysql_fetch_row($result);
//以上查询结果赋给row数组
print_r($row);
$username=$row[0];
$mail=$row[1];
echo $username;
echo $mail;
//以上显示结果
mysql_free_result($result);
//释放结果
mysql_close();
//关闭连接
?>
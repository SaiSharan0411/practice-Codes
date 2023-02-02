<html>
<body>
<?php
$res=setcookie('abc','123',mktime(+86400));
echo "cookie created.<br>";
echo $res;
setcookie('abc',' ',mktime(-86400));
?>
</body>
</html>
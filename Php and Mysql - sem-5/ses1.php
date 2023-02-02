<html>
<body>
<?php
SESSION_START();
$_SESSION['un']='sai';
$_SESSION['pwd']='123';
if(isset($_SESSION['pwd']))
{
echo "the session is created successfully";
}
else
{
echo"not executed";
}
?>
</body>
</html>

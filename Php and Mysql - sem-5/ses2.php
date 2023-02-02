<html>
<body>
<?php
SESSION_START();
echo 'Login name: '.$_SESSION['un'].'<br>';
echo 'Password: '.$_SESSION['pwd'].'<br>';
$_SESSION['pwd']='hh';
?>
</body>
</html>